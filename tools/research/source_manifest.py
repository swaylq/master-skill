#!/usr/bin/env python3
"""source_manifest.py — shared Source Manifest reader + consistency rules.

Codex 3rd-audit P0 #1: quality_check, cold_detector, claim_verifier each had
their own way of reading `## Source Manifest` tables and reconciling the
agent-declared `bucket` against `source_verifier`'s URL classifier. Drift
between them led to the insurance prototype quietly accepting brand-domain
URLs (douban.com, notion.so, feed.xyzfm.space) as `verified_primary` even
though the auto-classifier would have called them `secondary`. The agent's
manifest "upgrade-only" promise lived in the prompts, not in code.

This module centralizes:

  parse_manifests(skill_dir) → list[ManifestRow]
  check_bucket_consistency(rows) → list[Mismatch]   # iter 26 enforcement
  primary_ratio(rows) → (first_hand_count, total, ratio, breakdown)

`check_bucket_consistency` is the Q1 quality gate that the codebase was
missing: agents may DOWNGRADE the auto bucket (call a verified domain
`reference` because the URL is a single tweet, etc.) but may only UPGRADE
to `surrogate_primary` (Q5 cold deep-mode policy), and even then the `note`
field must declare the surrogate type. Any other upgrade is a manifest
violation and item 13 / item 14 surfaces it.

Pure stdlib. macOS python3 out-of-the-box.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import source_verifier  # type: ignore

# ---------------------------------------------------------------------------
# Constants

# Manifest row regex — same as quality_check / cold_detector were duplicating.
_MANIFEST_ROW_RE = re.compile(
    r"^\|\s*(T\d{2}-S\d+|S\d+)\s*\|\s*([^\|]+?)\s*\|\s*"
    r"(verified_primary|secondary|reference|blacklisted|dead|surrogate_primary)\s*\|\s*"
    r"([^\|]*?)\s*\|\s*([^\|]*?)\s*\|\s*([^\|]*?)\s*\|",
    re.MULTILINE,
)

# Bucket order from "trust" highest to lowest. Used to detect upgrades.
_BUCKET_RANK: dict[str, int] = {
    "blacklisted": 0,
    "dead": 1,
    "reference": 2,
    "secondary": 3,
    "surrogate_primary": 4,   # only allowed UPGRADE target from secondary
    "verified_primary": 5,
}

# Buckets that count as "first-hand tier" for the primary-ratio metric.
FIRST_HAND_BUCKETS: frozenset[str] = frozenset({"verified_primary", "surrogate_primary"})


@dataclass
class ManifestRow:
    source_id: str
    url: str
    bucket: str
    last_checked: str
    author: str
    note: str
    file: str

    @property
    def auto_bucket(self) -> str:
        """The bucket source_verifier would auto-assign for this URL."""
        if not self.url or self.url.strip() in ("manifest:none", "—", "-"):
            return "secondary"  # No URL → no auto signal; treat as secondary
        bucket, _ = source_verifier.classify_url(self.url)
        return bucket


@dataclass
class Mismatch:
    row: ManifestRow
    reason: str
    severity: str  # "violation" | "warning"


# ---------------------------------------------------------------------------
# Parser


def parse_manifests(
    skill_dir: Path, warn: bool = False,
) -> list[ManifestRow]:
    """Walk research/*.md and extract every `## Source Manifest` table row.

    Iter 26 (codex 4-audit P0-1c): also detect malformed rows (lines that
    look like manifest table entries but don't fully match the schema) so
    they don't silently disappear. Set `warn=True` to print them to stderr.
    """
    research_dir = skill_dir / "references" / "research"
    if not research_dir.exists():
        return []
    rows: list[ManifestRow] = []
    malformed: list[tuple[str, str]] = []  # (file, line)
    # Loose detector: any `| TXX-SXXX | ... |` row that isn't matched by the
    # full schema regex.
    loose_re = re.compile(
        r"^\|\s*(T\d{2}-S\d+|S\d+)\s*\|.*\|\s*$",
        re.MULTILINE,
    )
    for f in sorted(research_dir.glob("*.md")):
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        m = re.search(
            r"^##\s+Source\s+Manifest\b(.*?)(?=^##\s|\Z)",
            text, re.MULTILINE | re.DOTALL,
        )
        if not m:
            continue
        body = m.group(1)
        full_matches = list(_MANIFEST_ROW_RE.finditer(body))
        full_match_lines: set[int] = {body[:fm.start()].count("\n") for fm in full_matches}
        for row in full_matches:
            rows.append(ManifestRow(
                source_id=row.group(1).strip(),
                url=row.group(2).strip(),
                bucket=row.group(3).strip(),
                last_checked=(row.group(4) or "").strip(),
                author=(row.group(5) or "").strip(),
                note=(row.group(6) or "").strip(),
                file=f.name,
            ))
        # Detect rows that have a source_id but don't match the full schema —
        # these are silent drops the agent should know about
        for loose in loose_re.finditer(body):
            line_no = body[:loose.start()].count("\n")
            if line_no in full_match_lines:
                continue
            malformed.append((f.name, loose.group(0).strip()))

    if malformed and warn:
        import sys as _sys
        for fname, line in malformed:
            print(
                f"source_manifest: malformed row in {fname}: {line[:120]!r} "
                f"(missing column? check 6 pipe-separated fields)",
                file=_sys.stderr,
            )
    return rows


def parse_manifests_with_diagnostics(skill_dir: Path) -> tuple[list[ManifestRow], list[str]]:
    """Like parse_manifests but also returns malformed-row warnings."""
    research_dir = skill_dir / "references" / "research"
    if not research_dir.exists():
        return [], []
    rows: list[ManifestRow] = []
    warnings: list[str] = []
    loose_re = re.compile(
        r"^\|\s*(T\d{2}-S\d+|S\d+)\s*\|.*\|\s*$",
        re.MULTILINE,
    )
    for f in sorted(research_dir.glob("*.md")):
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        m = re.search(
            r"^##\s+Source\s+Manifest\b(.*?)(?=^##\s|\Z)",
            text, re.MULTILINE | re.DOTALL,
        )
        if not m:
            continue
        body = m.group(1)
        full_matches = list(_MANIFEST_ROW_RE.finditer(body))
        full_match_lines: set[int] = {body[:fm.start()].count("\n") for fm in full_matches}
        for row in full_matches:
            rows.append(ManifestRow(
                source_id=row.group(1).strip(),
                url=row.group(2).strip(),
                bucket=row.group(3).strip(),
                last_checked=(row.group(4) or "").strip(),
                author=(row.group(5) or "").strip(),
                note=(row.group(6) or "").strip(),
                file=f.name,
            ))
        for loose in loose_re.finditer(body):
            line_no = body[:loose.start()].count("\n")
            if line_no in full_match_lines:
                continue
            warnings.append(f"{f.name}: malformed row {loose.group(0).strip()[:120]}")
    return rows, warnings


# ---------------------------------------------------------------------------
# Bucket consistency rule

# Surrogate types that can be declared in the `note` field. Whitelist because
# `surrogate_primary` is the only bucket the agent is allowed to upgrade to,
# so the note has to be specific enough to audit later.
SURROGATE_NOTE_KEYWORDS: tuple[str, ...] = (
    "协会",        # 行业协会 / association
    "association",
    "监管", "立法", "regulator", "regulatory",
    "syllabus", "课程", "lecture", "教材",
    "招聘", "JD", "job",
    "vendor docs", "supplier", "供应商",
    "user-provided", "user provided", "用户提供", "internal", "内部",
    "anonymized", "匿名",
    "私 podcast",
    # Professional certification / standards bodies publishing their own
    # syllabus, exam format, or method (e.g. WSET / Court of Master Sommeliers /
    # Institute of Masters of Wine / GuildSomm / CSW). First-hand for the
    # standard they originate; recurs in every licensed/certified profession.
    "certification body", "cert body", "认证机构",
    # Named critic / recognized authority's own publication or site (e.g.
    # jancisrobinson.com / Vinous / Tim Atkin / wineanorak). First-hand authored
    # content; the text equivalent of the existing "私 podcast" type.
    "critic own publication", "own publication", "own site", "自有博客",
    # Originator of a method / tool / dataset publishing about it (e.g. the
    # Wine Aroma Wheel official site, the Liv-ex index pages).
    "originator",
    # Recognized education-content vendor's own first-party material (e.g.
    # Wine Folly). Consistent with the existing "vendor docs" / "supplier" type.
    "education vendor",
    # iter43 (corporate-finance-cfo): a book publisher's own official product
    # page (mheducation.com / wiley.com / simonandschuster / 出版社官方书页).
    # First-hand for the book's existence, edition, publication date and ToC —
    # the canon track of EVERY industry produces these, so this is a generic
    # addition, not a finance-specific one. It is NOT an endorsement of the
    # book's claims (those still need the author's own text or academic review).
    "publisher", "出版社",
    # iter (perfumery): a standards-setting body publishing its own standard
    # (e.g. IFRA fragrance standards, ASTM, ISO TC). First-hand for the standard
    # it originates — the sibling of the existing "certification body" /
    # "association" / "regulator" types; recurs in every standards-governed field.
    "standards body",
    # iter (autonomous-driving 2026-09-06): a conference organiser's own agenda /
    # session list / sponsor list. `prompts/research/_source_id_manifest.md`
    # has listed "会议 sponsor list + sessions list" as an acceptable surrogate
    # type since iter24 and instructs agents to write 「会议 sponsor」 in the
    # note — but this tuple never carried the token, so every agent that
    # followed the prompt was marked a violation. Spec/code mismatch, generic
    # to every industry with a conference circuit.
    "会议 sponsor", "会议官方", "会议议程", "conference sponsor", "conference agenda",
    # iter (perfumery): a craft/vocational school publishing its own curriculum
    # or program (e.g. ISIPCA / GIP perfumery schools, culinary/sommelier schools).
    # First-party education material — same family as "syllabus" / "education vendor".
    "perfumery school",
)


def _note_declares_surrogate_type(note: str) -> bool:
    if not note:
        return False
    low = note.lower()
    for kw in SURROGATE_NOTE_KEYWORDS:
        if kw.lower() in low:
            return True
    return False


def check_bucket_consistency(rows: list[ManifestRow]) -> list[Mismatch]:
    """For each manifest row, compare declared bucket vs auto bucket.

    Iter 26 (codex 4-audit P0-1a hardening): when auto = blacklisted or dead,
    declared MUST equal auto — surrogate_primary with note is NOT enough to
    rescue a blacklisted URL. The whole point of blacklisting (zh-CN
    知乎 / 公众号 / G2 / Capterra etc.) is the source itself is unreliable;
    no `surrogate_type` label changes that.

    Allowed transitions:
      - declared == auto                            ✓
      - declared LOWER than auto                    ✓ (DOWNGRADE always OK)
        Special: declared `blacklisted`, auto != `blacklisted` → warning
      - declared `surrogate_primary`, auto in {secondary, reference} AND note
        declares type ✓ (upgrade allowed via Q5 cold-mode escape valve)

    Disallowed:
      - declared `surrogate_primary` (or any upgrade) when auto is `blacklisted`
        or `dead` (HARD RULE — codex 4-audit P0-1a)
      - declared > auto without surrogate_primary path
      - surrogate_primary without note explanation
    """
    out: list[Mismatch] = []
    for r in rows:
        auto = r.auto_bucket
        declared = r.bucket
        if declared == auto:
            continue

        # HARD RULE (iter 26): if auto says blacklisted / dead, the only
        # allowed declared bucket is the same. No surrogate escape.
        if auto in ("blacklisted", "dead") and declared != auto:
            out.append(Mismatch(
                row=r,
                reason=(
                    f"declared {declared!r} but auto-classifier says {auto!r}. "
                    f"Blacklisted/dead URLs cannot be rescued via `surrogate_primary` — "
                    f"replace the URL or remove this row from the manifest."
                ),
                severity="violation",
            ))
            continue

        # Downgrade (declared lower than auto) is fine — agent might know URL
        # is a single tweet rather than the channel root.
        if _BUCKET_RANK.get(declared, 99) < _BUCKET_RANK.get(auto, 99):
            if declared == "blacklisted" and auto != "blacklisted":
                out.append(Mismatch(
                    row=r,
                    reason=f"declared blacklisted but auto says {auto} — verify intent (agent test source?)",
                    severity="warning",
                ))
            continue

        # Upgrade: only surrogate_primary is allowed, and note must explain
        if declared == "surrogate_primary":
            if auto == "verified_primary":
                # Auto already says primary; surrogate downgrade-style label
                # is fine (e.g. user-provided primary, intentional)
                continue
            if not _note_declares_surrogate_type(r.note):
                out.append(Mismatch(
                    row=r,
                    reason=(
                        f"surrogate_primary requires note declaring surrogate type "
                        f"(协会/监管/syllabus/JD/vendor docs/cert body/critic own publication/"
                        f"originator/education vendor/user-provided), got: "
                        f"{r.note[:80]!r}"
                    ),
                    severity="violation",
                ))
            continue  # surrogate_primary with proper note is OK
        # Any other upgrade is a violation
        out.append(Mismatch(
            row=r,
            reason=f"manifest UPGRADE not allowed: declared {declared}, auto says {auto}. "
                   f"Use `surrogate_primary` with note explanation, or trust auto.",
            severity="violation",
        ))
    return out


# ---------------------------------------------------------------------------
# Primary ratio


@dataclass
class RatioBreakdown:
    total: int = 0
    verified_primary: int = 0
    surrogate_primary: int = 0
    secondary: int = 0
    reference: int = 0
    blacklisted: int = 0
    dead: int = 0

    @property
    def first_hand(self) -> int:
        return self.verified_primary + self.surrogate_primary

    @property
    def ratio(self) -> float:
        return self.first_hand / self.total if self.total else 0.0


def primary_ratio(rows: list[ManifestRow]) -> RatioBreakdown:
    rb = RatioBreakdown(total=len(rows))
    for r in rows:
        if r.bucket == "verified_primary":
            rb.verified_primary += 1
        elif r.bucket == "surrogate_primary":
            rb.surrogate_primary += 1
        elif r.bucket == "secondary":
            rb.secondary += 1
        elif r.bucket == "reference":
            rb.reference += 1
        elif r.bucket == "blacklisted":
            rb.blacklisted += 1
        elif r.bucket == "dead":
            rb.dead += 1
    return rb


# ---------------------------------------------------------------------------
# CLI for ad-hoc inspection


def _cli() -> int:
    import argparse
    import json
    p = argparse.ArgumentParser(description="Inspect a skill's Source Manifest tables.")
    p.add_argument("--skill-dir", required=True, type=Path)
    p.add_argument("--json", action="store_true")
    p.add_argument("--check-consistency", action="store_true",
                   help="Run bucket-consistency check (manifest vs auto-classifier)")
    args = p.parse_args()

    rows = parse_manifests(args.skill_dir)
    out = {
        "skill_dir": str(args.skill_dir),
        "total_rows": len(rows),
        "rows": [
            {
                "source_id": r.source_id, "url": r.url, "bucket": r.bucket,
                "auto_bucket": r.auto_bucket, "last_checked": r.last_checked,
                "file": r.file,
            }
            for r in rows
        ],
    }
    rb = primary_ratio(rows)
    out["ratio"] = {
        "total": rb.total,
        "first_hand": rb.first_hand,
        "verified_primary": rb.verified_primary,
        "surrogate_primary": rb.surrogate_primary,
        "ratio": round(rb.ratio, 4),
    }
    if args.check_consistency:
        mismatches = check_bucket_consistency(rows)
        out["mismatches"] = [
            {
                "source_id": m.row.source_id,
                "url": m.row.url,
                "declared": m.row.bucket,
                "auto": m.row.auto_bucket,
                "severity": m.severity,
                "reason": m.reason,
                "file": m.row.file,
            }
            for m in mismatches
        ]
    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"# Source Manifest — {args.skill_dir}\n")
        print(f"total: {rb.total}  first-hand (verified+surrogate): {rb.first_hand} = {rb.ratio*100:.1f}%")
        print(f"  verified_primary: {rb.verified_primary}")
        print(f"  surrogate_primary: {rb.surrogate_primary}")
        print(f"  secondary: {rb.secondary}")
        print(f"  reference: {rb.reference}")
        print(f"  blacklisted: {rb.blacklisted}")
        print(f"  dead: {rb.dead}")
        if args.check_consistency:
            mm = check_bucket_consistency(rows)
            v = sum(1 for x in mm if x.severity == "violation")
            w = sum(1 for x in mm if x.severity == "warning")
            print(f"\nconsistency: {v} violation / {w} warning")
            for m in mm:
                tag = "❌" if m.severity == "violation" else "⚠️ "
                print(f"  {tag} {m.row.source_id} [{m.row.file}] declared={m.row.bucket} auto={m.row.auto_bucket}")
                print(f"     {m.reason}")
    # Exit 1 if any violation
    if args.check_consistency and any(m.severity == "violation" for m in check_bucket_consistency(rows)):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
