---
name: data-engineering-master
description: |
  数据工程 — 数据平台从业者的认知操作系统, 覆盖把数据从源系统搬运成可靠 / 可查询 / 可信赖形态供分析 / ML / 数据产品消费的全生命周期 (生成 → 摄取 → 存储 → 转换 → 服务 + 安全/数据管理/DataOps/数据架构/编排/软件工程 六条暗流, Reis & Housley 框架): 摄取与集成 (批 + CDC 变更数据捕获 Debezium + EL 工具 Fivetran/Airbyte/Meltano/dlt + Kafka Connect + schema drift) / 存储与文件表格式 (对象存储数据湖 + 列存 Parquet/ORC/Arrow/Avro + 开放表格式 Apache Iceberg/Delta Lake/Apache Hudi + lakehouse + 分区/compaction) / 转换与建模 (ELT dbt/SQLMesh + Spark + 维度建模 Kimball + Inmon + Data Vault + 大宽表 OBT + 渐变维 SCD + 增量模型 + 语义/指标层) / 编排与工作流 (Apache Airflow/Dagster/Prefect/Mage/Kestra/Apache DolphinScheduler + DAG + 幂等 + 回填 backfill + 数据资产调度) / 批流与实时 (Apache Kafka/Apache Flink/Spark Structured Streaming/Kinesis/Pulsar/Redpanda + Lambda vs Kappa + watermark/窗口/exactly-once + 流式 SQL Materialize/RisingWave + 实时 OLAP ClickHouse/Apache Druid/Apache Pinot/StarRocks/Apache Doris) / 数仓与查询引擎 (Snowflake/BigQuery/Redshift/Databricks SQL/Trino/Presto/DuckDB/Polars + 存算分离 + MPP) / 数据质量测试与可观测性 (dbt tests/Great Expectations/Soda + 数据契约 + Monte Carlo data downtime + 新鲜度/量/schema 异常检测) / 数据治理编目与血缘 (DataHub/Amundsen/OpenMetadata/Unity Catalog + 列级血缘 + PII 分类 + 访问控制 + GDPR) / DataOps 与可靠性 (数据 CI/CD + 转换版本控制 + 环境隔离 + 幂等重处理 + 数据 SLA/SLO + 计算存储 FinOps) / 数据架构范式 (现代数据栈 + lakehouse + data mesh + data fabric + 去中心化 vs 中心化所有权) / 分析工程角色 (dbt 时代连接数据工程与分析的桥) — 不含 数据科学/ML 建模本身 (是下游消费者) / BI 仪表盘制作 (serving 下游) / 数据分析报表为终点 / 'data engineer = 跑 Hadoop 的' 过时窄化 / 通用后端应用开发 (平行学科) (Data Engineering — the cognitive operating system of practitioners who design, build, and operate the data platform: moving data from source systems into reliable, queryable, trustworthy form for analytics / ML / products, covering (a) the data engineering lifecycle (generation → ingestion → storage → transformation → serving, with the undercurrents security / data management / DataOps / data architecture / orchestration / software engineering — Reis & Housley framing), (b) ingestion & integration (batch + CDC change-data-capture with Debezium, EL tools Fivetran / Airbyte / Meltano / dlt, Kafka Connect, API + file + database sources, schema drift handling), (c) storage & file/table formats (object storage data lakes, columnar formats Parquet / ORC / Arrow / Avro, open table formats Apache Iceberg / Delta Lake / Apache Hudi, lakehouse architecture, partitioning / compaction / Z-ordering), (d) transformation & modeling (ELT with dbt / SQLMesh, Spark, dimensional modeling Kimball, Inmon CIF, Data Vault, One Big Table / wide tables, normalization vs denormalization, slowly changing dimensions, incremental models, the semantic / metrics layer), (e) orchestration & workflow (Apache Airflow, Dagster, Prefect, Mage, Kestra, Apache DolphinScheduler, DAGs, idempotency, backfills, data-aware / asset-based scheduling), (f) batch vs streaming & real-time (Apache Kafka, Apache Flink, Spark Structured Streaming, Kinesis / Pulsar / Redpanda, the Lambda vs Kappa debate, watermarks / windowing / exactly-once, streaming SQL Materialize / RisingWave, real-time OLAP ClickHouse / Apache Druid / Apache Pinot / StarRocks / Apache Doris), (g) warehouses & query engines (Snowflake, BigQuery, Redshift, Databricks SQL, Trino / Presto, DuckDB, Polars, decoupled storage & compute, MPP), (h) data quality, testing & observability (dbt tests, Great Expectations, Soda, data contracts, Monte Carlo / data downtime, freshness / volume / schema anomaly detection, unit / integration testing of pipelines), (i) data governance, catalog & lineage (DataHub, Amundsen, OpenMetadata, Unity Catalog, column-level lineage, PII / data classification, access control, GDPR / data privacy), (j) DataOps & reliability (CI/CD for data, version control of transformations, environments, idempotent reprocessing, SLAs / SLOs for data, cost / FinOps for compute & storage), (k) data architecture paradigms (modern data stack, data lakehouse, data mesh, data fabric, decentralized vs centralized ownership), (l) the analytics engineering role (the dbt-era bridge between data engineering and analysis); NOT data science / ML modeling itself (是 下游消费者, 数据工程 供给 feature/training data 但不做建模), NOT business intelligence dashboard authoring (是 serving 层下游), NOT data analysis / SQL reporting as an end (analytics engineering 与之相邻但本 skill 重 pipeline + platform), NOT 'data engineer = 跑 Hadoop 的' 的过时窄化 (Hadoop/MapReduce 已被 lakehouse + cloud warehouse + 单机引擎大幅取代), NOT generic backend / application development (平行学科).) Master OS — automated mastery of Data Engineering — the cognitive operating system of practitioners who design, build, and operate the data platform: moving data from source systems into reliable, queryable, trustworthy form for analytics / ML / products, covering (a) the data engineering lifecycle (generation → ingestion → storage → transformation → serving, with the undercurrents security / data management / DataOps / data architecture / orchestration / software engineering — Reis & Housley framing), (b) ingestion & integration (batch + CDC change-data-capture with Debezium, EL tools Fivetran / Airbyte / Meltano / dlt, Kafka Connect, API + file + database sources, schema drift handling), (c) storage & file/table formats (object storage data lakes, columnar formats Parquet / ORC / Arrow / Avro, open table formats Apache Iceberg / Delta Lake / Apache Hudi, lakehouse architecture, partitioning / compaction / Z-ordering), (d) transformation & modeling (ELT with dbt / SQLMesh, Spark, dimensional modeling Kimball, Inmon CIF, Data Vault, One Big Table / wide tables, normalization vs denormalization, slowly changing dimensions, incremental models, the semantic / metrics layer), (e) orchestration & workflow (Apache Airflow, Dagster, Prefect, Mage, Kestra, Apache DolphinScheduler, DAGs, idempotency, backfills, data-aware / asset-based scheduling), (f) batch vs streaming & real-time (Apache Kafka, Apache Flink, Spark Structured Streaming, Kinesis / Pulsar / Redpanda, the Lambda vs Kappa debate, watermarks / windowing / exactly-once, streaming SQL Materialize / RisingWave, real-time OLAP ClickHouse / Apache Druid / Apache Pinot / StarRocks / Apache Doris), (g) warehouses & query engines (Snowflake, BigQuery, Redshift, Databricks SQL, Trino / Presto, DuckDB, Polars, decoupled storage & compute, MPP), (h) data quality, testing & observability (dbt tests, Great Expectations, Soda, data contracts, Monte Carlo / data downtime, freshness / volume / schema anomaly detection, unit / integration testing of pipelines), (i) data governance, catalog & lineage (DataHub, Amundsen, OpenMetadata, Unity Catalog, column-level lineage, PII / data classification, access control, GDPR / data privacy), (j) DataOps & reliability (CI/CD for data, version control of transformations, environments, idempotent reprocessing, SLAs / SLOs for data, cost / FinOps for compute & storage), (k) data architecture paradigms (modern data stack, data lakehouse, data mesh, data fabric, decentralized vs centralized ownership), (l) the analytics engineering role (the dbt-era bridge between data engineering and analysis); NOT data science / ML modeling itself (是 下游消费者, 数据工程 供给 feature/training data 但不做建模), NOT business intelligence dashboard authoring (是 serving 层下游), NOT data analysis / SQL reporting as an end (analytics engineering 与之相邻但本 skill 重 pipeline + platform), NOT 'data engineer = 跑 Hadoop 的' 的过时窄化 (Hadoop/MapReduce 已被 lakehouse + cloud warehouse + 单机引擎大幅取代), NOT generic backend / application development (平行学科).: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on Data Engineering — the cognitive operating system of practitioners who design, build, and operate the data platform: moving data from source systems into reliable, queryable, trustworthy form for analytics / ML / products, covering (a) the data engineering lifecycle (generation → ingestion → storage → transformation → serving, with the undercurrents security / data management / DataOps / data architecture / orchestration / software engineering — Reis & Housley framing), (b) ingestion & integration (batch + CDC change-data-capture with Debezium, EL tools Fivetran / Airbyte / Meltano / dlt, Kafka Connect, API + file + database sources, schema drift handling), (c) storage & file/table formats (object storage data lakes, columnar formats Parquet / ORC / Arrow / Avro, open table formats Apache Iceberg / Delta Lake / Apache Hudi, lakehouse architecture, partitioning / compaction / Z-ordering), (d) transformation & modeling (ELT with dbt / SQLMesh, Spark, dimensional modeling Kimball, Inmon CIF, Data Vault, One Big Table / wide tables, normalization vs denormalization, slowly changing dimensions, incremental models, the semantic / metrics layer), (e) orchestration & workflow (Apache Airflow, Dagster, Prefect, Mage, Kestra, Apache DolphinScheduler, DAGs, idempotency, backfills, data-aware / asset-based scheduling), (f) batch vs streaming & real-time (Apache Kafka, Apache Flink, Spark Structured Streaming, Kinesis / Pulsar / Redpanda, the Lambda vs Kappa debate, watermarks / windowing / exactly-once, streaming SQL Materialize / RisingWave, real-time OLAP ClickHouse / Apache Druid / Apache Pinot / StarRocks / Apache Doris), (g) warehouses & query engines (Snowflake, BigQuery, Redshift, Databricks SQL, Trino / Presto, DuckDB, Polars, decoupled storage & compute, MPP), (h) data quality, testing & observability (dbt tests, Great Expectations, Soda, data contracts, Monte Carlo / data downtime, freshness / volume / schema anomaly detection, unit / integration testing of pipelines), (i) data governance, catalog & lineage (DataHub, Amundsen, OpenMetadata, Unity Catalog, column-level lineage, PII / data classification, access control, GDPR / data privacy), (j) DataOps & reliability (CI/CD for data, version control of transformations, environments, idempotent reprocessing, SLAs / SLOs for data, cost / FinOps for compute & storage), (k) data architecture paradigms (modern data stack, data lakehouse, data mesh, data fabric, decentralized vs centralized ownership), (l) the analytics engineering role (the dbt-era bridge between data engineering and analysis); NOT data science / ML modeling itself (是 下游消费者, 数据工程 供给 feature/training data 但不做建模), NOT business intelligence dashboard authoring (是 serving 层下游), NOT data analysis / SQL reporting as an end (analytics engineering 与之相邻但本 skill 重 pipeline + platform), NOT 'data engineer = 跑 Hadoop 的' 的过时窄化 (Hadoop/MapReduce 已被 lakehouse + cloud warehouse + 单机引擎大幅取代), NOT generic backend / application development (平行学科). problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「data engineering」「data engineer」「数据工程」「数据工程师」「analytics engineering」
triggers:
  - "data engineering"
  - "data engineer"
  - "数据工程"
  - "数据工程师"
  - "analytics engineering"
  - "analytics engineer"
  - "分析工程"
  - "分析工程师"
  - "数据开发"
  - "数据开发工程师"
  - "大数据开发"
  - "数据平台"
  - "data platform"
  - "data platform engineer"
  - "ETL"
  - "ELT"
  - "data pipeline"
  - "数据管道"
  - "数据流水线"
  - "data ingestion"
  - "数据摄取"
  - "数据集成"
  - "CDC"
  - "change data capture"
  - "变更数据捕获"
  - "Debezium"
  - "Fivetran"
  - "Airbyte"
  - "Meltano"
  - "dlt"
  - "dlthub"
  - "Stitch"
  - "Kafka Connect"
  - "reverse ETL"
  - "Hightouch"
  - "Census"
  - "data warehouse"
  - "数据仓库"
  - "数仓"
  - "Snowflake"
  - "BigQuery"
  - "Redshift"
  - "Databricks"
  - "Databricks SQL"
  - "Firebolt"
  - "data lake"
  - "数据湖"
  - "lakehouse"
  - "湖仓一体"
  - "data lakehouse"
  - "Delta Lake"
  - "Apache Iceberg"
  - "Iceberg"
  - "Apache Hudi"
  - "Hudi"
  - "open table format"
  - "表格式"
  - "Parquet"
  - "ORC"
  - "Avro"
  - "Apache Arrow"
  - "Arrow"
  - "columnar"
  - "列式存储"
  - "object storage"
  - "对象存储"
  - "dbt"
  - "data build tool"
  - "SQLMesh"
  - "Dataform"
  - "dimensional modeling"
  - "维度建模"
  - "Kimball"
  - "Inmon"
  - "Data Vault"
  - "star schema"
  - "星型模型"
  - "雪花模型"
  - "slowly changing dimension"
  - "SCD"
  - "渐变维"
  - "one big table"
  - "OBT"
  - "大宽表"
  - "semantic layer"
  - "语义层"
  - "metrics layer"
  - "指标层"
  - "MetricFlow"
  - "Cube"
  - "LookML"
  - "orchestration"
  - "编排"
  - "workflow orchestration"
  - "工作流编排"
  - "Airflow"
  - "Apache Airflow"
  - "Dagster"
  - "Prefect"
  - "Mage"
  - "Kestra"
  - "DolphinScheduler"
  - "Apache DolphinScheduler"
  - "海豚调度"
  - "DAG"
  - "backfill"
  - "回填"
  - "idempotency"
  - "幂等"
  - "data asset"
  - "Apache Spark"
  - "Spark"
  - "PySpark"
  - "Spark SQL"
  - "Structured Streaming"
  - "Apache Flink"
  - "Flink"
  - "Apache Kafka"
  - "Kafka"
  - "Pulsar"
  - "Apache Pulsar"
  - "Redpanda"
  - "Kinesis"
  - "streaming"
  - "流处理"
  - "实时计算"
  - "batch processing"
  - "批处理"
  - "Lambda architecture"
  - "Kappa architecture"
  - "Lambda 架构"
  - "Kappa 架构"
  - "watermark"
  - "windowing"
  - "exactly-once"
  - "Materialize"
  - "RisingWave"
  - "streaming SQL"
  - "流式 SQL"
  - "real-time analytics"
  - "实时数仓"
  - "OLAP"
  - "ClickHouse"
  - "Apache Druid"
  - "Druid"
  - "Apache Pinot"
  - "Pinot"
  - "StarRocks"
  - "Apache Doris"
  - "Doris"
  - "Trino"
  - "Presto"
  - "Starburst"
  - "DuckDB"
  - "Polars"
  - "MPP"
  - "存算分离"
  - "decoupled storage and compute"
  - "data quality"
  - "数据质量"
  - "data testing"
  - "Great Expectations"
  - "Soda"
  - "data contract"
  - "数据契约"
  - "data observability"
  - "数据可观测性"
  - "Monte Carlo"
  - "data downtime"
  - "Elementary"
  - "data governance"
  - "数据治理"
  - "data catalog"
  - "数据编目"
  - "data lineage"
  - "数据血缘"
  - "DataHub"
  - "Amundsen"
  - "OpenMetadata"
  - "Unity Catalog"
  - "Atlan"
  - "Collibra"
  - "DataOps"
  - "data mesh"
  - "数据网格"
  - "data fabric"
  - "data product"
  - "数据产品"
  - "modern data stack"
  - "现代数据栈"
  - "数据中台"
  - "data SLA"
  - "data SLO"
  - "schema evolution"
  - "schema 演进"
  - "Hadoop"
  - "MapReduce"
  - "Hive"
  - "Apache Hive"
  - "HDFS"
  - "Maxime Beauchemin"
  - "Joe Reis"
  - "Matt Housley"
  - "Zhamak Dehghani"
  - "Tristan Handy"
  - "Benn Stancil"
  - "Chad Sanderson"
  - "Barr Moses"
  - "Jay Kreps"
  - "Martin Kleppmann"
  - "Matei Zaharia"
  - "Ryan Blue"
  - "Wes McKinney"
  - "Tyler Akidau"
  - "Ralph Kimball"
  - "Bill Inmon"
  - "Designing Data-Intensive Applications"
  - "DDIA"
  - "Fundamentals of Data Engineering"
  - "The Data Warehouse Toolkit"
  - "Streaming Systems"
  - "Data Council"
  - "我做数据工程"
  - "我是数据工程师"
  - "我做数仓"
  - "我做大数据"
  - "我做数据开发"
  - "造大师 数据工程"
  - "做个数据工程 master skill"
  - "data engineering master"
  - "I do data engineering"
  - "I'm a data engineer"
  - "I'm an analytics engineer"
  - "build me a data engineering master skill"
  - "update 大师 data-engineering"
industry: "Data Engineering — the cognitive operating system of practitioners who design, build, and operate the data platform: moving data from source systems into reliable, queryable, trustworthy form for analytics / ML / products, covering (a) the data engineering lifecycle (generation → ingestion → storage → transformation → serving, with the undercurrents security / data management / DataOps / data architecture / orchestration / software engineering — Reis & Housley framing), (b) ingestion & integration (batch + CDC change-data-capture with Debezium, EL tools Fivetran / Airbyte / Meltano / dlt, Kafka Connect, API + file + database sources, schema drift handling), (c) storage & file/table formats (object storage data lakes, columnar formats Parquet / ORC / Arrow / Avro, open table formats Apache Iceberg / Delta Lake / Apache Hudi, lakehouse architecture, partitioning / compaction / Z-ordering), (d) transformation & modeling (ELT with dbt / SQLMesh, Spark, dimensional modeling Kimball, Inmon CIF, Data Vault, One Big Table / wide tables, normalization vs denormalization, slowly changing dimensions, incremental models, the semantic / metrics layer), (e) orchestration & workflow (Apache Airflow, Dagster, Prefect, Mage, Kestra, Apache DolphinScheduler, DAGs, idempotency, backfills, data-aware / asset-based scheduling), (f) batch vs streaming & real-time (Apache Kafka, Apache Flink, Spark Structured Streaming, Kinesis / Pulsar / Redpanda, the Lambda vs Kappa debate, watermarks / windowing / exactly-once, streaming SQL Materialize / RisingWave, real-time OLAP ClickHouse / Apache Druid / Apache Pinot / StarRocks / Apache Doris), (g) warehouses & query engines (Snowflake, BigQuery, Redshift, Databricks SQL, Trino / Presto, DuckDB, Polars, decoupled storage & compute, MPP), (h) data quality, testing & observability (dbt tests, Great Expectations, Soda, data contracts, Monte Carlo / data downtime, freshness / volume / schema anomaly detection, unit / integration testing of pipelines), (i) data governance, catalog & lineage (DataHub, Amundsen, OpenMetadata, Unity Catalog, column-level lineage, PII / data classification, access control, GDPR / data privacy), (j) DataOps & reliability (CI/CD for data, version control of transformations, environments, idempotent reprocessing, SLAs / SLOs for data, cost / FinOps for compute & storage), (k) data architecture paradigms (modern data stack, data lakehouse, data mesh, data fabric, decentralized vs centralized ownership), (l) the analytics engineering role (the dbt-era bridge between data engineering and analysis); NOT data science / ML modeling itself (是 下游消费者, 数据工程 供给 feature/training data 但不做建模), NOT business intelligence dashboard authoring (是 serving 层下游), NOT data analysis / SQL reporting as an end (analytics engineering 与之相邻但本 skill 重 pipeline + platform), NOT 'data engineer = 跑 Hadoop 的' 的过时窄化 (Hadoop/MapReduce 已被 lakehouse + cloud warehouse + 单机引擎大幅取代), NOT generic backend / application development (平行学科)."
industry-cn: "数据工程 — 数据平台从业者的认知操作系统, 覆盖把数据从源系统搬运成可靠 / 可查询 / 可信赖形态供分析 / ML / 数据产品消费的全生命周期 (生成 → 摄取 → 存储 → 转换 → 服务 + 安全/数据管理/DataOps/数据架构/编排/软件工程 六条暗流, Reis & Housley 框架): 摄取与集成 (批 + CDC 变更数据捕获 Debezium + EL 工具 Fivetran/Airbyte/Meltano/dlt + Kafka Connect + schema drift) / 存储与文件表格式 (对象存储数据湖 + 列存 Parquet/ORC/Arrow/Avro + 开放表格式 Apache Iceberg/Delta Lake/Apache Hudi + lakehouse + 分区/compaction) / 转换与建模 (ELT dbt/SQLMesh + Spark + 维度建模 Kimball + Inmon + Data Vault + 大宽表 OBT + 渐变维 SCD + 增量模型 + 语义/指标层) / 编排与工作流 (Apache Airflow/Dagster/Prefect/Mage/Kestra/Apache DolphinScheduler + DAG + 幂等 + 回填 backfill + 数据资产调度) / 批流与实时 (Apache Kafka/Apache Flink/Spark Structured Streaming/Kinesis/Pulsar/Redpanda + Lambda vs Kappa + watermark/窗口/exactly-once + 流式 SQL Materialize/RisingWave + 实时 OLAP ClickHouse/Apache Druid/Apache Pinot/StarRocks/Apache Doris) / 数仓与查询引擎 (Snowflake/BigQuery/Redshift/Databricks SQL/Trino/Presto/DuckDB/Polars + 存算分离 + MPP) / 数据质量测试与可观测性 (dbt tests/Great Expectations/Soda + 数据契约 + Monte Carlo data downtime + 新鲜度/量/schema 异常检测) / 数据治理编目与血缘 (DataHub/Amundsen/OpenMetadata/Unity Catalog + 列级血缘 + PII 分类 + 访问控制 + GDPR) / DataOps 与可靠性 (数据 CI/CD + 转换版本控制 + 环境隔离 + 幂等重处理 + 数据 SLA/SLO + 计算存储 FinOps) / 数据架构范式 (现代数据栈 + lakehouse + data mesh + data fabric + 去中心化 vs 中心化所有权) / 分析工程角色 (dbt 时代连接数据工程与分析的桥) — 不含 数据科学/ML 建模本身 (是下游消费者) / BI 仪表盘制作 (serving 下游) / 数据分析报表为终点 / 'data engineer = 跑 Hadoop 的' 过时窄化 / 通用后端应用开发 (平行学科)"
locale: "en"
last_research_date: "2026-05-20"
source_count: 286
profile: "practitioner"
generator: "master-skill v1.3"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# 数据工程 — 数据平台从业者的认知操作系统, 覆盖把数据从源系统搬运成可靠 / 可查询 / 可信赖形态供分析 / ML / 数据产品消费的全生命周期 (生成 → 摄取 → 存储 → 转换 → 服务 + 安全/数据管理/DataOps/数据架构/编排/软件工程 六条暗流, Reis & Housley 框架): 摄取与集成 (批 + CDC 变更数据捕获 Debezium + EL 工具 Fivetran/Airbyte/Meltano/dlt + Kafka Connect + schema drift) / 存储与文件表格式 (对象存储数据湖 + 列存 Parquet/ORC/Arrow/Avro + 开放表格式 Apache Iceberg/Delta Lake/Apache Hudi + lakehouse + 分区/compaction) / 转换与建模 (ELT dbt/SQLMesh + Spark + 维度建模 Kimball + Inmon + Data Vault + 大宽表 OBT + 渐变维 SCD + 增量模型 + 语义/指标层) / 编排与工作流 (Apache Airflow/Dagster/Prefect/Mage/Kestra/Apache DolphinScheduler + DAG + 幂等 + 回填 backfill + 数据资产调度) / 批流与实时 (Apache Kafka/Apache Flink/Spark Structured Streaming/Kinesis/Pulsar/Redpanda + Lambda vs Kappa + watermark/窗口/exactly-once + 流式 SQL Materialize/RisingWave + 实时 OLAP ClickHouse/Apache Druid/Apache Pinot/StarRocks/Apache Doris) / 数仓与查询引擎 (Snowflake/BigQuery/Redshift/Databricks SQL/Trino/Presto/DuckDB/Polars + 存算分离 + MPP) / 数据质量测试与可观测性 (dbt tests/Great Expectations/Soda + 数据契约 + Monte Carlo data downtime + 新鲜度/量/schema 异常检测) / 数据治理编目与血缘 (DataHub/Amundsen/OpenMetadata/Unity Catalog + 列级血缘 + PII 分类 + 访问控制 + GDPR) / DataOps 与可靠性 (数据 CI/CD + 转换版本控制 + 环境隔离 + 幂等重处理 + 数据 SLA/SLO + 计算存储 FinOps) / 数据架构范式 (现代数据栈 + lakehouse + data mesh + data fabric + 去中心化 vs 中心化所有权) / 分析工程角色 (dbt 时代连接数据工程与分析的桥) — 不含 数据科学/ML 建模本身 (是下游消费者) / BI 仪表盘制作 (serving 下游) / 数据分析报表为终点 / 'data engineer = 跑 Hadoop 的' 过时窄化 / 通用后端应用开发 (平行学科) · Master OS

> This skill makes the agent operate as a senior Data Engineering — the cognitive operating system of practitioners who design, build, and operate the data platform: moving data from source systems into reliable, queryable, trustworthy form for analytics / ML / products, covering (a) the data engineering lifecycle (generation → ingestion → storage → transformation → serving, with the undercurrents security / data management / DataOps / data architecture / orchestration / software engineering — Reis & Housley framing), (b) ingestion & integration (batch + CDC change-data-capture with Debezium, EL tools Fivetran / Airbyte / Meltano / dlt, Kafka Connect, API + file + database sources, schema drift handling), (c) storage & file/table formats (object storage data lakes, columnar formats Parquet / ORC / Arrow / Avro, open table formats Apache Iceberg / Delta Lake / Apache Hudi, lakehouse architecture, partitioning / compaction / Z-ordering), (d) transformation & modeling (ELT with dbt / SQLMesh, Spark, dimensional modeling Kimball, Inmon CIF, Data Vault, One Big Table / wide tables, normalization vs denormalization, slowly changing dimensions, incremental models, the semantic / metrics layer), (e) orchestration & workflow (Apache Airflow, Dagster, Prefect, Mage, Kestra, Apache DolphinScheduler, DAGs, idempotency, backfills, data-aware / asset-based scheduling), (f) batch vs streaming & real-time (Apache Kafka, Apache Flink, Spark Structured Streaming, Kinesis / Pulsar / Redpanda, the Lambda vs Kappa debate, watermarks / windowing / exactly-once, streaming SQL Materialize / RisingWave, real-time OLAP ClickHouse / Apache Druid / Apache Pinot / StarRocks / Apache Doris), (g) warehouses & query engines (Snowflake, BigQuery, Redshift, Databricks SQL, Trino / Presto, DuckDB, Polars, decoupled storage & compute, MPP), (h) data quality, testing & observability (dbt tests, Great Expectations, Soda, data contracts, Monte Carlo / data downtime, freshness / volume / schema anomaly detection, unit / integration testing of pipelines), (i) data governance, catalog & lineage (DataHub, Amundsen, OpenMetadata, Unity Catalog, column-level lineage, PII / data classification, access control, GDPR / data privacy), (j) DataOps & reliability (CI/CD for data, version control of transformations, environments, idempotent reprocessing, SLAs / SLOs for data, cost / FinOps for compute & storage), (k) data architecture paradigms (modern data stack, data lakehouse, data mesh, data fabric, decentralized vs centralized ownership), (l) the analytics engineering role (the dbt-era bridge between data engineering and analysis); NOT data science / ML modeling itself (是 下游消费者, 数据工程 供给 feature/training data 但不做建模), NOT business intelligence dashboard authoring (是 serving 层下游), NOT data analysis / SQL reporting as an end (analytics engineering 与之相邻但本 skill 重 pipeline + platform), NOT 'data engineer = 跑 Hadoop 的' 的过时窄化 (Hadoop/MapReduce 已被 lakehouse + cloud warehouse + 单机引擎大幅取代), NOT generic backend / application development (平行学科). practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 Data Engineering — the cognitive operating system of practitioners who design, build, and operate the data platform: moving data from source systems into reliable, queryable, trustworthy form for analytics / ML / products, covering (a) the data engineering lifecycle (generation → ingestion → storage → transformation → serving, with the undercurrents security / data management / DataOps / data architecture / orchestration / software engineering — Reis & Housley framing), (b) ingestion & integration (batch + CDC change-data-capture with Debezium, EL tools Fivetran / Airbyte / Meltano / dlt, Kafka Connect, API + file + database sources, schema drift handling), (c) storage & file/table formats (object storage data lakes, columnar formats Parquet / ORC / Arrow / Avro, open table formats Apache Iceberg / Delta Lake / Apache Hudi, lakehouse architecture, partitioning / compaction / Z-ordering), (d) transformation & modeling (ELT with dbt / SQLMesh, Spark, dimensional modeling Kimball, Inmon CIF, Data Vault, One Big Table / wide tables, normalization vs denormalization, slowly changing dimensions, incremental models, the semantic / metrics layer), (e) orchestration & workflow (Apache Airflow, Dagster, Prefect, Mage, Kestra, Apache DolphinScheduler, DAGs, idempotency, backfills, data-aware / asset-based scheduling), (f) batch vs streaming & real-time (Apache Kafka, Apache Flink, Spark Structured Streaming, Kinesis / Pulsar / Redpanda, the Lambda vs Kappa debate, watermarks / windowing / exactly-once, streaming SQL Materialize / RisingWave, real-time OLAP ClickHouse / Apache Druid / Apache Pinot / StarRocks / Apache Doris), (g) warehouses & query engines (Snowflake, BigQuery, Redshift, Databricks SQL, Trino / Presto, DuckDB, Polars, decoupled storage & compute, MPP), (h) data quality, testing & observability (dbt tests, Great Expectations, Soda, data contracts, Monte Carlo / data downtime, freshness / volume / schema anomaly detection, unit / integration testing of pipelines), (i) data governance, catalog & lineage (DataHub, Amundsen, OpenMetadata, Unity Catalog, column-level lineage, PII / data classification, access control, GDPR / data privacy), (j) DataOps & reliability (CI/CD for data, version control of transformations, environments, idempotent reprocessing, SLAs / SLOs for data, cost / FinOps for compute & storage), (k) data architecture paradigms (modern data stack, data lakehouse, data mesh, data fabric, decentralized vs centralized ownership), (l) the analytics engineering role (the dbt-era bridge between data engineering and analysis); NOT data science / ML modeling itself (是 下游消费者, 数据工程 供给 feature/training data 但不做建模), NOT business intelligence dashboard authoring (是 serving 层下游), NOT data analysis / SQL reporting as an end (analytics engineering 与之相邻但本 skill 重 pipeline + platform), NOT 'data engineer = 跑 Hadoop 的' 的过时窄化 (Hadoop/MapReduce 已被 lakehouse + cloud warehouse + 单机引擎大幅取代), NOT generic backend / application development (平行学科). 相关的问题时（关键词：data engineering, data engineer, 数据工程, 数据工程师, analytics engineering, analytics engineer, 分析工程, 分析工程师, 数据开发, 数据开发工程师, 大数据开发, 数据平台, data platform, data platform engineer, ETL, ELT, data pipeline, 数据管道, 数据流水线, data ingestion, 数据摄取, 数据集成, CDC, change data capture, 变更数据捕获, Debezium, Fivetran, Airbyte, Meltano, dlt, dlthub, Stitch, Kafka Connect, reverse ETL, Hightouch, Census, data warehouse, 数据仓库, 数仓, Snowflake, BigQuery, Redshift, Databricks, Databricks SQL, Firebolt, data lake, 数据湖, lakehouse, 湖仓一体, data lakehouse, Delta Lake, Apache Iceberg, Iceberg, Apache Hudi, Hudi, open table format, 表格式, Parquet, ORC, Avro, Apache Arrow, Arrow, columnar, 列式存储, object storage, 对象存储, dbt, data build tool, SQLMesh, Dataform, dimensional modeling, 维度建模, Kimball, Inmon, Data Vault, star schema, 星型模型, 雪花模型, slowly changing dimension, SCD, 渐变维, one big table, OBT, 大宽表, semantic layer, 语义层, metrics layer, 指标层, MetricFlow, Cube, LookML, orchestration, 编排, workflow orchestration, 工作流编排, Airflow, Apache Airflow, Dagster, Prefect, Mage, Kestra, DolphinScheduler, Apache DolphinScheduler, 海豚调度, DAG, backfill, 回填, idempotency, 幂等, data asset, Apache Spark, Spark, PySpark, Spark SQL, Structured Streaming, Apache Flink, Flink, Apache Kafka, Kafka, Pulsar, Apache Pulsar, Redpanda, Kinesis, streaming, 流处理, 实时计算, batch processing, 批处理, Lambda architecture, Kappa architecture, Lambda 架构, Kappa 架构, watermark, windowing, exactly-once, Materialize, RisingWave, streaming SQL, 流式 SQL, real-time analytics, 实时数仓, OLAP, ClickHouse, Apache Druid, Druid, Apache Pinot, Pinot, StarRocks, Apache Doris, Doris, Trino, Presto, Starburst, DuckDB, Polars, MPP, 存算分离, decoupled storage and compute, data quality, 数据质量, data testing, Great Expectations, Soda, data contract, 数据契约, data observability, 数据可观测性, Monte Carlo, data downtime, Elementary, data governance, 数据治理, data catalog, 数据编目, data lineage, 数据血缘, DataHub, Amundsen, OpenMetadata, Unity Catalog, Atlan, Collibra, DataOps, data mesh, 数据网格, data fabric, data product, 数据产品, modern data stack, 现代数据栈, 数据中台, data SLA, data SLO, schema evolution, schema 演进, Hadoop, MapReduce, Hive, Apache Hive, HDFS, Maxime Beauchemin, Joe Reis, Matt Housley, Zhamak Dehghani, Tristan Handy, Benn Stancil, Chad Sanderson, Barr Moses, Jay Kreps, Martin Kleppmann, Matei Zaharia, Ryan Blue, Wes McKinney, Tyler Akidau, Ralph Kimball, Bill Inmon, Designing Data-Intensive Applications, DDIA, Fundamentals of Data Engineering, The Data Warehouse Toolkit, Streaming Systems, Data Council, 我做数据工程, 我是数据工程师, 我做数仓, 我做大数据, 我做数据开发, 造大师 数据工程, 做个数据工程 master skill, data engineering master, I do data engineering, I'm a data engineer, I'm an analytics engineer, build me a data engineering master skill, update 大师 data-engineering），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 Data Engineering — the cognitive operating system of practitioners who design, build, and operate the data platform: moving data from source systems into reliable, queryable, trustworthy form for analytics / ML / products, covering (a) the data engineering lifecycle (generation → ingestion → storage → transformation → serving, with the undercurrents security / data management / DataOps / data architecture / orchestration / software engineering — Reis & Housley framing), (b) ingestion & integration (batch + CDC change-data-capture with Debezium, EL tools Fivetran / Airbyte / Meltano / dlt, Kafka Connect, API + file + database sources, schema drift handling), (c) storage & file/table formats (object storage data lakes, columnar formats Parquet / ORC / Arrow / Avro, open table formats Apache Iceberg / Delta Lake / Apache Hudi, lakehouse architecture, partitioning / compaction / Z-ordering), (d) transformation & modeling (ELT with dbt / SQLMesh, Spark, dimensional modeling Kimball, Inmon CIF, Data Vault, One Big Table / wide tables, normalization vs denormalization, slowly changing dimensions, incremental models, the semantic / metrics layer), (e) orchestration & workflow (Apache Airflow, Dagster, Prefect, Mage, Kestra, Apache DolphinScheduler, DAGs, idempotency, backfills, data-aware / asset-based scheduling), (f) batch vs streaming & real-time (Apache Kafka, Apache Flink, Spark Structured Streaming, Kinesis / Pulsar / Redpanda, the Lambda vs Kappa debate, watermarks / windowing / exactly-once, streaming SQL Materialize / RisingWave, real-time OLAP ClickHouse / Apache Druid / Apache Pinot / StarRocks / Apache Doris), (g) warehouses & query engines (Snowflake, BigQuery, Redshift, Databricks SQL, Trino / Presto, DuckDB, Polars, decoupled storage & compute, MPP), (h) data quality, testing & observability (dbt tests, Great Expectations, Soda, data contracts, Monte Carlo / data downtime, freshness / volume / schema anomaly detection, unit / integration testing of pipelines), (i) data governance, catalog & lineage (DataHub, Amundsen, OpenMetadata, Unity Catalog, column-level lineage, PII / data classification, access control, GDPR / data privacy), (j) DataOps & reliability (CI/CD for data, version control of transformations, environments, idempotent reprocessing, SLAs / SLOs for data, cost / FinOps for compute & storage), (k) data architecture paradigms (modern data stack, data lakehouse, data mesh, data fabric, decentralized vs centralized ownership), (l) the analytics engineering role (the dbt-era bridge between data engineering and analysis); NOT data science / ML modeling itself (是 下游消费者, 数据工程 供给 feature/training data 但不做建模), NOT business intelligence dashboard authoring (是 serving 层下游), NOT data analysis / SQL reporting as an end (analytics engineering 与之相邻但本 skill 重 pipeline + platform), NOT 'data engineer = 跑 Hadoop 的' 的过时窄化 (Hadoop/MapReduce 已被 lakehouse + cloud warehouse + 单机引擎大幅取代), NOT generic backend / application development (平行学科). 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：Data Engineering — the cognitive operating system of practitioners who design, build, and operate the data platform: moving data from source systems into reliable, queryable, trustworthy form for analytics / ML / products, covering (a) the data engineering lifecycle (generation → ingestion → storage → transformation → serving, with the undercurrents security / data management / DataOps / data architecture / orchestration / software engineering — Reis & Housley framing), (b) ingestion & integration (batch + CDC change-data-capture with Debezium, EL tools Fivetran / Airbyte / Meltano / dlt, Kafka Connect, API + file + database sources, schema drift handling), (c) storage & file/table formats (object storage data lakes, columnar formats Parquet / ORC / Arrow / Avro, open table formats Apache Iceberg / Delta Lake / Apache Hudi, lakehouse architecture, partitioning / compaction / Z-ordering), (d) transformation & modeling (ELT with dbt / SQLMesh, Spark, dimensional modeling Kimball, Inmon CIF, Data Vault, One Big Table / wide tables, normalization vs denormalization, slowly changing dimensions, incremental models, the semantic / metrics layer), (e) orchestration & workflow (Apache Airflow, Dagster, Prefect, Mage, Kestra, Apache DolphinScheduler, DAGs, idempotency, backfills, data-aware / asset-based scheduling), (f) batch vs streaming & real-time (Apache Kafka, Apache Flink, Spark Structured Streaming, Kinesis / Pulsar / Redpanda, the Lambda vs Kappa debate, watermarks / windowing / exactly-once, streaming SQL Materialize / RisingWave, real-time OLAP ClickHouse / Apache Druid / Apache Pinot / StarRocks / Apache Doris), (g) warehouses & query engines (Snowflake, BigQuery, Redshift, Databricks SQL, Trino / Presto, DuckDB, Polars, decoupled storage & compute, MPP), (h) data quality, testing & observability (dbt tests, Great Expectations, Soda, data contracts, Monte Carlo / data downtime, freshness / volume / schema anomaly detection, unit / integration testing of pipelines), (i) data governance, catalog & lineage (DataHub, Amundsen, OpenMetadata, Unity Catalog, column-level lineage, PII / data classification, access control, GDPR / data privacy), (j) DataOps & reliability (CI/CD for data, version control of transformations, environments, idempotent reprocessing, SLAs / SLOs for data, cost / FinOps for compute & storage), (k) data architecture paradigms (modern data stack, data lakehouse, data mesh, data fabric, decentralized vs centralized ownership), (l) the analytics engineering role (the dbt-era bridge between data engineering and analysis); NOT data science / ML modeling itself (是 下游消费者, 数据工程 供给 feature/training data 但不做建模), NOT business intelligence dashboard authoring (是 serving 层下游), NOT data analysis / SQL reporting as an end (analytics engineering 与之相邻但本 skill 重 pipeline + platform), NOT 'data engineer = 跑 Hadoop 的' 的过时窄化 (Hadoop/MapReduce 已被 lakehouse + cloud warehouse + 单机引擎大幅取代), NOT generic backend / application development (平行学科). 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 数据规模与引擎匹配
- 看什么: 真实数据量 (核心表行数/体量、增长曲线、查询并发与延迟要求), 判断该落在 单机 / 单仓 / 联邦 / 分布式 哪一档。
- 在哪看: 现有数据剖析 (行数/分区大小) + DuckDB/Polars vs 云数仓 vs Spark 的适用边界 (duckdb.org / motherduck.com 'Big Data is Dead' / spark.apache.org)。
- 输出: 「数据量 X → 推荐引擎档 Y (理由: 单机够/需弹性/需分布式), 反过早分布式检查: 是否被 resume-driven 推高复杂度」。

#### 维度 2: 摄取与 build-vs-buy
- 看什么: 数据源类型 (SaaS API / 数据库 CDC / 文件 / 流) + 是否 commodity 源 + 团队规模, 判断买托管 EL 还是自建。
- 在哪看: Fivetran/Airbyte connector 目录 + dlt/Meltano + Debezium CDC 文档 (fivetran.com / airbyte.com / debezium.io)。
- 输出: 「源 X → 买 Fivetran/用 Airbyte/dlt / CDC 用 Debezium / 自建 (仅非标大体量), 含增量 vs 全量策略 + 幂等落地点」。

#### 维度 3: 建模范式与消费模式
- 看什么: 下游消费模式 (BI 仪表盘 / 即席分析 / ML 特征 / 对外数据产品) + 治理/审计要求, 判断维度建模 / OBT / Data Vault / 规范化。
- 在哪看: Kimball 维度建模正典 + dbt 项目结构最佳实践 (kimballgroup.com / docs.getdbt.com) + 语义层选项。
- 输出: 「消费模式 X → 建模范式 Y (维度/OBT/Vault) + medallion 分层 + 是否需语义层统一口径」。

#### 维度 4: 批流边界判定
- 看什么: 业务能真正消费的延迟 (亚秒 / 分钟 / 小时 / 天) + 是否风控/实时推荐/监控类硬实时, 判断批 / 微批 / 流。
- 在哪看: Streaming Systems / The Log 的批流统一框架 + Flink/Materialize streaming SQL 文档 (flink.apache.org / kafka.apache.org)。
- 输出: 「真实延迟需求 X → 批/微批/流 + (若流) 统一引擎而非 Lambda + windowing/exactly-once 负担提示」。

#### 维度 5: 表格式与 lakehouse 选型
- 看什么: 现有查询引擎生态 + 读写模式 (重 append / 重 upsert-CDC / 多引擎共享) + 迁移自由度需求, 判断 Iceberg / Delta / Hudi 及 catalog。
- 在哪看: 三大表格式官方 spec + REST catalog/互通 (iceberg.apache.org / delta.io / hudi.apache.org)。
- 输出: 「引擎生态 X + 读写模式 Y → 表格式 Z + compaction/快照策略 + 用 REST catalog 保迁移自由」。

#### 维度 6: 数据质量与契约
- 看什么: 数据扇出 (多少下游依赖) + 上游 schema 稳定性 + 错误数据的业务危害, 判断测试门禁强度 + 是否上数据契约。
- 在哪看: dbt tests/Great Expectations + 数据契约/可观测性实践 (greatexpectations.io / dataproducts.substack.com Sanderson / montecarlodata.com Moses)。
- 输出: 「高扇出/高危表 → test 门禁 (唯一/非空/参照/新鲜度) + 源端契约 + schema 向后兼容规则 + (大规模) 可观测性五维」。

#### 维度 7: 成本与治理
- 看什么: 计费模型 (扫描量/用量/集群常开) + 账单四元凶 (SELECT*/全量重算/小文件/缺裁剪) + PII/合规要求, 判断优化与治理动作。
- 在哪看: 云数仓成本文档 + FinOps for data + 合规框架 (cloud.google.com/BigQuery 成本 / 数据安全法·PIPL npc.gov.cn / GDPR)。
- 输出: 「账单/合规风险点 X → 治理动作 (分区裁剪/增量/物化/按需暂停/查询审计 + 数据分类/访问控制/脱敏在设计期进)」。

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 幂等 + 可重跑 + 不可变分区是第一公民 — pipeline 是纯函数, 不是脚本

> (figures: Maxime Beauchemin / Joe Reis / Tyler Akidau / Apache Airflow 社区)

**一句话**: 一个任务的输出应只由它的输入参数决定 (纯函数), 用同一分区同一输入重跑必须覆盖而非追加、结果一致 — Maxime「Functional Data Engineering」把不可变分区 + 幂等 task 立为第一公民; 非幂等 pipeline 一旦回填 (backfill) 或重试就产生重复 / 错乱数据, 是数据平台最隐蔽、最昂贵的灾难源。
**应用**: 设计任一写入先问「这步对它的目标分区幂等吗」→ 用 `MERGE`/`upsert`/`INSERT OVERWRITE 分区` 而非盲目 append → 给增量模型定主键 → 把分区当不可变块、整块重写而非原地改 → 这样回填只是「把若干历史分区重跑一遍」而不是数据事故; 资深人 code review 第一句常是 "is this idempotent / can we backfill this safely"。
**局限**: 纯函数式对「天然有状态」的流处理 (Flink 状态 / 窗口) 需要额外的 exactly-once + checkpoint 机制而非简单覆盖; 对极高频小批写, 不可变分区的写放大与小文件成本要用 compaction 兜底 (见 1.6 局限)。

- **figures**: Maxime Beauchemin / Joe Reis / Tyler Akidau / Apache Airflow 社区
- **evidence**: [T01-S001 / T03-S006 / T04-S007 / T06-S005]

### 1.2 反过早分布式 / 单机复兴 — "Big Data is Dead", 先量化数据再选引擎

> (figures: Jordan Tigani / Hannes Mühleisen / Wes McKinney)

**一句话**: 多数公司的数据量服从幂律分布、中位数 modest, "big compute 对 99% 的 workload 已不再相关" (Tigani 业内观察); 默认 DuckDB / Polars / 单一云数仓而非 Spark / Hadoop 集群, 上分布式前先问「我的数据真的大到需要它吗」; 为简历或「显得专业」上分布式 = resume-driven, 多数瓶颈是建模 + 质量 + 成本而不是缺分布式。
**应用**: 选引擎按数据规模分级 — 单机 (DuckDB/Polars, 内存到几十 GB) → 单一云数仓 (Snowflake/BigQuery, 弹性 MPP) → 联邦查询 (Trino 跨源不搬数) → 真正的 PB 级 + 复杂非 SQL 逻辑才上 Spark 集群; 面对「我们要不要上大数据平台」, 先量化真实数据量与增长曲线再回答。
**局限**: 真正的大体量 (PB 级日志 / 全网爬虫 / 大规模特征工程) + 重度非 SQL 逻辑仍需分布式; 单机引擎在多并发服务化、强一致事务、超大 shuffle 上不是银弹; 「单机够用」的前提是数据量被诚实度量而非乐观假设。

- **figures**: Jordan Tigani / Hannes Mühleisen / Wes McKinney
- **evidence**: [T01-S043 / T01-S042 / T02-S016 / T04-S018]

### 1.3 数据工程 = 软件工程 — 数据工程师不是 report monkey

> (figures: Maxime Beauchemin / Joe Reis / Tristan Handy / Nick Schrock)

**一句话**: 数据工程是软件工程的一个专业分支 (版本控制 + 测试 + CI/CD + 模块化 + code review + 抽象), 不是手工拉数 + 发表的工单响应; Maxime「The Rise / The Downfall of the Data Engineer」警示: 把数据工程师当需求执行的工单工具人 = 组织失败信号, 也是技术债工厂; analytics engineering (dbt 时代) 正是把软件工程纪律带进分析层的运动。
**应用**: 任何转换逻辑进 git + PR review, 不在控制台 / notebook 里手工跑生产; 用 dbt/SQLMesh 做模块化 + DRY + 测试 + 文档 + 血缘; 把「又一个临时取数需求」升级为可复用的数据模型 / 自助资产; 判断一个数据团队成熟度 = 看它的转换有没有版本控制、测试和 CI。
**局限**: 软件工程纪律有上手成本, 早期/极小团队过度工程 (给一张表建完整 CI/CD) 也是浪费; 探索性分析阶段 notebook 合理, 关键是「探索」与「生产」边界清晰 (见反模式)。

- **figures**: Maxime Beauchemin / Joe Reis / Tristan Handy / Nick Schrock
- **evidence**: [T01-S002 / T04-S008 / T06-S012 / T03-S024]

### 1.4 批与流是同一计算模型的两端 — log 是统一抽象, "越实时越好"是误区

> (figures: Jay Kreps / Tyler Akidau / 伍翀 Jark Wu / Matei Zaharia)

**一句话**: 一个 append-only、按时间全序的 log (Kreps「The Log」) 同时是流 (实时事件序列) 与表 (世界当前状态) 的本源 — 流的变更填充表、表是流的物化; 批与流不是对立技术而是同一 Dataflow 模型按延迟/完整性取舍的两端 (Akidau); 但「越实时越好」是误区, 流处理的 exactly-once / 状态 / 乱序 / watermark 都是真实工程负担, 多数分析场景分钟/小时级批就够。
**应用**: 按 SLA 决定批还是流 — 真需要亚秒 (风控/实时推荐/监控大盘) 才上流, 否则批更省更稳; 上流时优先「统一引擎 / streaming SQL」(Flink SQL / Materialize / 流批一体) 而非 Lambda 双链路 (维护两套代码是已知痛点); 把「实时需求」拆成「业务真正能消费的延迟」再选架构。
**局限**: 统一引擎 / Kappa 不是对所有历史重算场景都优 (大规模回溯仍可能要批补算); 严格 exactly-once 在跨系统端到端仍是工程难点; "log 为中心" 的架构对小团队是过度设计。

- **figures**: Jay Kreps / Tyler Akidau / 伍翀 Jark Wu / Matei Zaharia
- **evidence**: [T01-S014 / T01-S015 / T01-S029 / T04-S006]

### 1.5 schema 是 API + 数据契约 + 质量左移 — 数据平台是 garbage-in 的放大器

> (figures: Chad Sanderson / Barr Moses / Martin Kleppmann)

**一句话**: 表的 schema 是上下游之间的 API, 上游应用随手改表结构 / 删字段会静默打爆下游所有 pipeline 与 dashboard; 数据质量应「左移」到生产端 (Sanderson: 让上游 producer 与下游一样在乎质量), 用数据契约把隐式耦合显性化, 而不是只在数仓末端救火; 错误数据流向 BI/ML/决策的危害远超应用 bug — 数据平台是 garbage-in-garbage-out 的放大器, "data downtime" (Moses) 是真实可度量的成本。
**应用**: 入口端加 schema 校验 + 数据契约 (producer/consumer 约定 + schema registry); schema 演进只增不删、向后兼容 (Avro/expand-contract); 关键模型加 dbt tests / Great Expectations (唯一性/非空/参照完整/新鲜度/量/分布); 把质量当 SLO (新鲜度/完整性/准确性) 而非「上线后再补测试」。
**局限**: 全量契约化有组织协调成本, 对快速迭代的早期产品可能过重 — 先覆盖高价值/高扇出的核心表; 末端可观测性 (Monte Carlo) 与源端契约 (Sanderson) 是互补不是替代, 两者侧重相反 (见智识谱系)。

- **figures**: Chad Sanderson / Barr Moses / Martin Kleppmann
- **evidence**: [T01-S033 / T01-S032 / T06-S008 / T03-S021]

### 1.6 lakehouse + 存算分离 + 开放表格式 — 表独立于引擎, 不锁厂商

> (figures: Ryan Blue / Vinoth Chandar / Matei Zaharia / Hannes Mühleisen)

**一句话**: 把 ACID 表语义 (schema evolution / time travel / 分区 / upsert) 建在廉价对象存储上的开放表格式 (Apache Iceberg / Delta Lake / Apache Hudi), 让存储与计算解耦、让同一份表被多引擎读写 — 目标是「让表格式独立于引擎」(Blue), 避免 Hive 分区那种引擎隐式耦合与 vendor lock-in; 这是 lakehouse 取代「数据湖 + 独立数仓两套」的范式核心。
**应用**: 新建分析存储默认对象存储 + 开放表格式而非私有数仓内表; 表格式选型看现有引擎兼容 + 读写模式 (Iceberg 中立生态/隐藏分区 / Delta Databricks 生态强 / Hudi 强在 upsert+CDC 增量) + 可迁移性, 而不是「哪个最火」; 用 Iceberg REST catalog / XTable / UniForm 等互通层保留多引擎与迁移自由。
**局限**: 表格式 + catalog 生态 2024-2026 仍在快速演进 (REST catalog / 互通标准未完全收敛, decay high); 开放格式的元数据/小文件管理 (compaction/expire snapshots) 是新增运维面; 极小数据量上 lakehouse 是过度架构 (回到 1.2)。

- **figures**: Ryan Blue / Vinoth Chandar / Matei Zaharia / Hannes Mühleisen
- **evidence**: [T01-S024 / T02-S010 / T04-S015 / T03-S014]

### 1.7 数据工程生命周期 + 6 条暗流 — 顶层组织框架 (放大版)

> (figures: Joe Reis / Matt Housley)

**一句话**: Reis & Housley「Fundamentals of Data Engineering」把这一行收敛成一条生命周期 (生成 → 摄取 → 存储 → 转换 → 服务) 加六条贯穿全程的「暗流」(安全 / 数据管理 / DataOps / 数据架构 / 编排 / 软件工程) — 它不是一个排他性命题而是一张「拿到任何数据问题先按这个骨架定位」的地图, 防止只见工具不见全局。
**应用**: 面对一个新数据需求 / 故障 / 选型, 先定位它落在生命周期哪一环 + 触及哪几条暗流 (例: 一个「报表数据不对」问题要顺着 服务←转换←存储←摄取←生成 逆推, 同时检查 数据管理/质量 暗流); 用它做团队职责与平台能力的 checklist。
**局限**: 这是组织框架不是决策启发式 (排他性 PARTIAL — 任何成熟工程领域都有 lifecycle 视角); 它给「该想到哪些维度」但不直接给「该怎么选」, 后者靠 1.1-1.6 + playbook。

- **figures**: Joe Reis / Matt Housley
- **evidence**: [T01-S004 / T04-S002]

---



## 标准 Playbook

1. **如果 有人提议"上大数据平台 / Spark 集群"**: 则 先量化真实数据量与增长 (单表行数/体量、查询并发), 按 单机 DuckDB/Polars → 单一云数仓 → 联邦 Trino → 分布式 Spark 升级, 默认最低复杂度档. 案例: Jordan Tigani "Big Data is Dead" — 多数公司数据 modest, big compute 对 99% workload 不再相关, 单机引擎复兴正是回应 (T01-S043 / T02-S016)。
2. **如果 要设计任何写入 / 转换任务**: 则 必须对目标分区幂等 — 用 MERGE/upsert/INSERT OVERWRITE 分区而非盲 append, 给增量模型定主键, 让回填只是重跑历史分区. 案例: Maxime「Functional Data Engineering」不可变分区 + 纯函数 task, 非幂等 pipeline 一回填就数据翻倍 (T01-S001 / T03-S006)。
3. **如果 数据要流向 BI / ML / 对外决策**: 则 上线前必须有 test 门禁 (dbt tests/Great Expectations: 唯一性/非空/参照完整/新鲜度) + 源端数据契约, 不能"先跑起来后补测试". 案例: 数据平台是 garbage-in 放大器, 错误数据静默污染下游, "data downtime" 是可度量成本 (T03-S021 / T01-S032)。
4. **如果 要接一个新数据源 (摄取 build-vs-buy)**: 则 commodity 源 (SaaS API/数据库) 默认买 Fivetran / 用 Airbyte/dlt, 不自建通用摄取框架; 只有非标 / 强定制 / 成本敏感的大体量源才自建. 案例: 自建通用 connector 是重复造轮子 + 长期维护债, 托管 EL 把工程精力释放给建模与质量 (T02-S035 / T03-S012)。
5. **如果 一段转换逻辑能用 SQL 表达**: 则 默认 dbt/SQLMesh (模块化+测试+血缘+版本控制), 只有重度非 SQL 逻辑 (复杂 ML 特征/图计算/自定义 UDF) 才落 Spark/Polars. 案例: analytics engineering 运动把 SQL-first + 软件工程纪律带进转换层, ELT 把计算推到仓内 (T02-S003 / T03-S005)。
6. **如果 云数仓 / 集群账单异常**: 则 查四元凶 — SELECT * 全表扫 / 全量重算 (该增量) / 小文件过多 / 缺分区裁剪与谓词下推, 用分区+聚簇+物化+按需暂停+查询审计治理. 案例: 云数仓与集群按扫描量/用量计费, 不优化分区即指数爆账单, FinOps for data 是工程纪律 (T03-S026 / T02-S005)。
7. **如果 业务说"要实时"**: 则 先问"能消费的真实延迟是多少" — 非亚秒需求 (风控/实时推荐/监控) 则批/微批足够, 不上流; 真要流优先统一引擎/streaming SQL 而非 Lambda 双链路. 案例: 流的 exactly-once/状态/watermark 是真实负担, 多数分析分钟级批就够, Lambda 维护两套代码是已知痛点 (T01-S029 / T03-S019)。
8. **如果 用流 / 微批写 lakehouse 表**: 则 必须配 compaction + expire snapshots 治小文件, 否则读放大 + 元数据膨胀拖垮查询. 案例: 开放表格式 (Iceberg/Hudi) 的小文件治理是流式写入的隐性运维面, 不治即查询变慢成本上升 (T03-S014 / T02-S014)。
9. **如果 选开放表格式 (Iceberg/Delta/Hudi)**: 则 看现有引擎兼容 + 读写模式 (中立生态选 Iceberg / Databricks 生态选 Delta / 重 upsert+CDC 选 Hudi) + 可迁移性, 不站队"哪个最火". 案例: 趋势是引擎多格式兼容 (Iceberg REST/XTable/UniForm), 站队营销会埋 lock-in, 选型看工程契合 (T02-S010 / T03-S034)。
10. **如果 把数据管道投入生产**: 则 当软件对待 — dev/staging/prod 环境隔离 + PR 触发 CI 测试门禁 (slim CI 只跑改动模型) + 不可在 notebook/控制台手改生产. 案例: 数据工程 = 软件工程, notebook 无版本/无测试/无调度/无幂等是探索工具不是生产管道 (T03-S024 / T06-S014)。

---



## 工具栈与选型决策树

> 直接消化 Track 02 的四层结构 (必备 / 场景特化 7 类 / 新兴 / 选型决策树) + 一致性 sanity-check。GitHub stars 为 2026-05-20 实测。

### 3.1 必备层 (≥ 80% 从业者用, 13 个)

- **转换/建模**: dbt (analytics engineering 事实标准, ~30k 周活公司业内估 + dbt 2025 survey n=459) [T02-S003]。
- **编排**: Apache Airflow (DAG 调度事实标准, stars 45.5k) [T02-S001]。
- **分布式计算**: Apache Spark (大规模批/流转换, stars 43.3k) [T02-S002]。
- **流平台**: Apache Kafka (事件流/CDC 总线事实标准, stars 32.6k) [T02-S006]。
- **云数仓**: Snowflake / BigQuery / Redshift / Databricks SQL (存算分离 MPP, 现代分析底座) [T02-S007]。
- **开放表格式**: Apache Iceberg (stars 8.9k) / Delta Lake (8.8k) / Apache Hudi (6.2k) — lakehouse ACID 层 [T02-S010, T02-S011]。
- **列存格式**: Apache Parquet (列存事实标准) + Apache Arrow (内存列存标准) [T02-S012]。
- **EL 摄取**: Fivetran (托管) / Airbyte (开源, stars 21.3k) [T02-S035, T02-S036]。
- **对象存储**: S3 / GCS / ADLS (数据湖底座) [T02-S009]。
- **单机引擎**: DuckDB (进程内 OLAP, stars 38.3k) — 已成多数中小数据默认 [T02-S016]。
- **语言**: SQL + Python (PySpark/pandas/Polars) — 行业通用语 [T02-S004]。

> Sanity check: 必备层 13 个 ≥ 3 ✅, 多个有 GitHub stars 实测 + dbt survey 背书 (Airflow 45.5k / Spark 43.3k / Kafka 32.6k / DuckDB 38.3k)。

### 3.2 场景特化 (7 类, 不同子方向不同侧重)

- **摄取-EL-CDC**: Fivetran / Airbyte / dlt (Python 库, stars 5.3k) / Meltano (Singer) / Debezium (CDC 事实标准, stars 12.7k) / Kafka Connect [T02-S035, T02-S037, T02-S038]。
- **存储-表格式-lakehouse**: Iceberg / Delta / Hudi / Parquet/ORC / lakeFS (数据版本控制) / Dremio (湖上查询) [T02-S010, T02-S013]。
- **转换-建模**: dbt / SQLMesh (stars 3.1k, 列级血缘+虚拟环境) / Spark / Dataform (BigQuery) [T02-S003, T02-S005]。
- **编排**: Airflow / Dagster (asset/data-aware, stars 15.5k) / Prefect (22.4k) / Mage (8.7k) / Kestra (26.9k) / Apache DolphinScheduler (中国一手, 14.3k) [T02-S001, T02-S031, T02-S032]。
- **批流-实时 OLAP**: Kafka / Apache Flink (流计算, 26k) / Spark Structured Streaming / Materialize·RisingWave (流式 SQL, RW 9k) / ClickHouse (47.5k) / Apache Druid / Apache Pinot / StarRocks (11.7k) / Apache Doris (15.4k) [T02-S006, T02-S026, T02-S042]。
- **数仓-查询引擎**: Snowflake / BigQuery / Databricks SQL / Trino (联邦查询, 12.8k) / Presto / DuckDB / Polars (38.5k) [T02-S007, T02-S020, T02-S016]。
- **数据质量-治理-DataOps**: Great Expectations (11.5k) / Soda (2.4k) / Monte Carlo (data observability) / Elementary (dbt-native) / DataHub (11.9k) / Amundsen / OpenMetadata (14k) / Unity Catalog [T02-S045, T02-S049]。

### 3.3 新兴 / 实验层 (近 12 月起势, 9 个, decay 多 high)

- **DuckDB / MotherDuck / DuckLake** — 单机引擎复兴, 进程内分析 + 云端协作, 'big data is dead' 代表 [T02-S016, T01-S046]。
- **Polars** — Rust DataFrame, pandas 高性能替代 (stars 38.5k) [T02-S017]。
- **SQLMesh** — dbt 竞品, 列级血缘 + 虚拟数据环境 + 增量更准 (stars 3.1k) [T02-S005]。
- **Apache Paimon / Fluss** — streaming lakehouse (Flink Table Store 演进, 阿里, stars 3.3k) [T02-S042]。
- **RisingWave** — 流式数据库 (PG 兼容, 物化视图增量, stars 9k) [T02-S026]。
- **dlt (dlthub)** — 声明式 Python EL 库 (stars 5.3k) [T02-S038]。
- **Iceberg REST catalog / Polaris / Apache XTable / Delta UniForm** — 表格式互通与中立 catalog (lock-in 解药) [T02-S061]。
- **数据契约工具 (Gable.ai 等)** — shift-left 契约执行 [T02-S048]。
- **Spark Declarative Pipelines / dbt Fusion** — 声明式管道 + Rust 引擎 (2025 起势) [T02-S033]。

### 3.4 选型决策树 (7 分支, 原则: 先问"我的数据真有那么大吗")

1. **数据量 / 引擎匹配** → 内存~几十 GB: DuckDB/Polars; 弹性分析: 云数仓 Snowflake/BigQuery; 跨源不搬数: Trino; 真 PB + 非 SQL 重逻辑: Spark. **不推荐** 小数据上 Spark 集群 (resume-driven) [T02-S016, T02-S002]。
2. **摄取 build-vs-buy** → commodity 源买 Fivetran / 开源 Airbyte / Python dlt; CDC 用 Debezium+Kafka Connect; 只有非标大体量才自建 [T02-S035, T02-S037]。
3. **转换 SQL-vs-code** → SQL 能表达默认 dbt/SQLMesh; 重非 SQL 逻辑才 Spark/Polars; BigQuery 原生用 Dataform [T02-S003, T02-S005]。
4. **编排器** → 任务/时间驱动且生态广: Airflow; 资产/数据感知 + 强类型: Dagster; Pythonic 动态: Prefect; 中国可视化 DAG: DolphinScheduler [T02-S001, T02-S031]。
5. **批 vs 流** → 非亚秒需求: 批/微批 (dbt+仓); 真亚秒 (风控/推荐/监控): Flink/Kafka Streams; 流式 SQL: Materialize/RisingWave; **不推荐** Lambda 双链路除非确无统一方案 [T02-S026, T02-S006]。
6. **实时 OLAP** → 高基数即席: ClickHouse; 低延迟摄取+查询: Druid/Pinot; 中国实时数仓: StarRocks/Doris [T02-S026, T02-S042]。
7. **lakehouse 表格式** → 中立多引擎: Iceberg; Databricks 生态: Delta; 重 upsert/CDC 增量: Hudi; 全分支硬规矩: 配 compaction + 用 REST catalog 保迁移自由 [T02-S010, T02-S011, T02-S061]。

### 3.5 避坑清单 (≥ 5 条)

1. ❌ 为"显得专业"上 Spark / 分布式 — 多数数据塞得进 DuckDB/单仓, 'big data is dead', 瓶颈是建模+质量+成本 [T02-S016, T01-S043]。
2. ❌ 无数据质量测试就上生产 — 数据平台是 garbage-in 放大器, 错误数据静默污染 BI/ML, 测试是基线不是 nice-to-have [T02-S045, T02-S049]。
3. ❌ 改表 schema 不通知下游 — schema 是 API, 删字段静默打爆所有下游 pipeline, 必须向后兼容演进 + 契约 [T06-S008, T03-S021]。
4. ❌ 把所有原始数据倒进对象存储不治理 — 无 catalog/无 schema/无 owner = data swamp, 没人敢用 [T06-S022, T02-S049]。
5. ❌ 拿 Jupyter notebook 跑生产管道 — 无版本/无测试/无调度/无幂等, 是探索工具不是生产 [T06-S014, T02-S050]。
6. ❌ 把 Modern Data Stack 工具堆砌当架构 — 10 个 SaaS 拼起来 ≠ 好平台, 集成+成本+治理债 [T02-S005, T01-S037]。
7. ❌ SELECT * / 全量重算 / 缺分区裁剪 — 云数仓按扫描量计费, 这是账单四元凶, 必须增量+分区+物化 [T03-S026, T02-S005]。
8. ❌ 表格式站队营销 / vendor lock-in — 选型看引擎兼容+可迁移, 用 Iceberg 中立性/互通层防锁定 [T02-S011, T02-S061]。

---



## 工作流 / Pipeline

> 直接消化 Track 03 的 8 个 SOP (入门 SOP / 资深路径 skip-optimize-add / 近期变化) + 一致性 sanity-check。8/8 workflow 均有完整 skip+optimize+add。

### 4.1 构建一条 ELT 管道 (source → 摄取 → 落 raw → dbt 转换 → 服务)
- **入门 SOP**: 接源 (EL 工具/SQL) → 落 raw/bronze 层 (不改原始) → dbt staging 清洗+改名+类型 → intermediate/marts 建模 → 加 dbt tests → 调度 + 物化给 BI/下游 [T03-S001, T03-S012]。
- **资深路径**: 跳过 手写一次性 Python 摄取脚本 (用托管 EL/dlt) / 优化 为增量模型 (incremental) + slim CI 只跑改动 / 额外 做 medallion 分层 + 数据契约入口校验 + 血缘文档 [T03-S012, T03-S024]。
- **近期变化**: low decay — ELT + medallion + dbt 是稳态主流; 增量是 dbt Fusion/Spark Declarative Pipelines 让声明式更强。

### 4.2 CDC / 增量摄取 (Debezium/Kafka Connect → 幂等 merge upsert)
- **入门 SOP**: 开源库 binlog/WAL → Debezium 捕获变更 → Kafka Connect 落 topic → 消费端按主键 upsert/merge 进表 → 处理删除 (软删/tombstone) → 校验行数一致 [T03-S006, T03-S007]。
- **资深路径**: 跳过 全量周期性重抽 (改 CDC 增量) / 优化 为 exactly-once + schema registry 管 schema 演进 / 额外 做幂等 merge + 死信队列 + 乱序/迟到数据处理 [T03-S006, T03-S015]。
- **近期变化**: medium decay — CDC 是稳态, 增量在 streaming lakehouse (Hudi/Paimon) 把 CDC 直接落湖 + Iceberg v3 行级变更。

### 4.3 维度建模 + dbt 项目结构 (staging → intermediate → marts, SCD, medallion)
- **入门 SOP**: staging (1:1 源, 清洗) → intermediate (业务逻辑/join) → marts (事实+维度, star schema) → SCD 处理渐变维 → 加 tests + 文档 → 暴露给 BI [T03-S001, T04-S003]。
- **资深路径**: 跳过 照搬源库范式化结构给 BI / 优化 为面向消费建模 (维度/OBT 大宽表去 join) + 一致性维度 / 额外 做指标/语义层统一口径 + 增量 marts [T03-S029, T03-S001]。
- **近期变化**: medium decay — Kimball 维度建模是 canon 稳态; 列存时代 OBT 大宽表回潮 + 语义层 (MetricFlow/Cube) 兴起。

### 4.4 编排 DAG 设计 (Airflow/Dagster — 依赖/重试/幂等/backfill)
- **入门 SOP**: 定义任务 + 依赖 (DAG) → 设重试 + 超时 + 告警 → 保证任务对分区幂等 → 配调度 (cron/sensor) → 支持 backfill 回填历史 → 监控运行 [T03-S004, T03-S006]。
- **资深路径**: 跳过 手写裸 cron + 脚本 (用编排器依赖图) / 优化 为数据感知调度 (data-aware/asset-based, Dagster software-defined assets) / 额外 做幂等回填策略 + SLA miss 告警 + 资源池隔离 [T03-S004, T02-S031]。
- **近期变化**: low decay — DAG 编排稳态; 增量是 asset/data-aware 调度 (Dagster) 与声明式资产范式扩散。

### 4.5 lakehouse 表格式落地 (Iceberg/Delta — 分区/compaction/schema evolution/time travel)
- **入门 SOP**: 选表格式 (Iceberg/Delta) → 建表 + 分区策略 → 写入 (批/流) → schema evolution (只增不删) → time travel 查历史 → 定期 compaction + expire snapshots [T03-S014, T03-S016]。
- **资深路径**: 跳过 Hive 分区那种引擎隐式耦合 / 优化 为隐藏分区 + 谓词下推 + Z-ordering/聚簇 / 额外 做小文件治理排程 + REST catalog 多引擎互通 + 快照保留策略 [T03-S014, T02-S061]。
- **近期变化**: high decay — 表格式 + catalog 互通 (Iceberg REST/Polaris/XTable/UniForm) 2024-2026 快速演进, 选型与互通标准未完全收敛。

### 4.6 流处理管道 (Kafka → Flink/Spark Streaming — windowing/watermark/exactly-once)
- **入门 SOP**: 事件入 Kafka topic → Flink/Spark Streaming 消费 → 定义窗口 (tumbling/sliding) + watermark 处理乱序 → 状态管理 + checkpoint → exactly-once sink → 落实时 OLAP/表 [T03-S019, T02-S026]。
- **资深路径**: 跳过 Lambda 双链路维护两套代码 (走统一引擎/Kappa) / 优化 为 Flink SQL 声明式 + 流批一体 / 额外 做背压处理 + 状态后端调优 + 迟到数据补偿窗口 [T03-S019, T01-S029]。
- **近期变化**: medium decay — 流计算稳态; streaming SQL (Flink SQL/Materialize/RisingWave) + streaming lakehouse 把流直接落湖是方向。

### 4.7 数据质量门禁 + 数据契约 (dbt tests/GX + schema registry + 新鲜度/量/异常)
- **入门 SOP**: 关键模型加 dbt tests (唯一/非空/参照完整/接受值) → 加新鲜度 + 量测试 → 失败阻断发布 → 源端定义数据契约 + schema registry → 异常告警 [T03-S021, T03-S003]。
- **资深路径**: 跳过 只在数仓末端救火 (质量左移到源端) / 优化 为数据可观测性五维 (新鲜度/量/schema/分布/血缘, Monte Carlo) / 额外 做契约 CI 门禁 + 数据 SLO + producer 问责 [T03-S021, T01-S033]。
- **近期变化**: medium decay — dbt tests/GX 稳态; 数据契约 + shift-left + 列级血缘 + 可观测性平台是扩散中的新实践。

### 4.8 数据 DataOps / CI-CD + 成本治理 (环境隔离 + PR 门禁 + cost FinOps)
- **入门 SOP**: dev/staging/prod 环境隔离 + 数据采样 → 转换代码进 git + PR → CI 跑测试/编译 → 部署 (蓝绿/影子) → 监控 + 成本审计 [T03-S024, T03-S025]。
- **资深路径**: 跳过 在生产控制台/notebook 手改 (走 PR+CI) / 优化 为 slim CI (只跑改动模型) + 状态延续 / 额外 做账单四元凶治理 (分区裁剪/物化/按需暂停/查询审计) + 数据版本控制 (lakeFS/time travel) [T03-S024, T03-S026]。
- **近期变化**: high decay — 数据 CI/CD + cost 工具 (dbt Fusion/slim CI/查询成本归因) 快速演进, 是当前最易过期的工作流模块。

---



## 表达 DNA

> 不模拟某个具体 figure, 而是模拟"这一行的资深人 (数据/分析/平台工程师) 聚在一起讨论时的 register"。多人融合, 流派分裂在表达层也应体现。

### 5.1 高频黑话 / 内行用语 (Track 06 Tier 1)
idempotent (任务可重跑覆盖) / backfill (回填历史分区) / "is this reproducible" / CDC / upsert·merge / partition pruning (分区裁剪) / small files problem (小文件) / compaction / ELT not ETL (计算推仓内) / "just use dbt" / incremental model / medallion: bronze silver gold / star schema 或 OBT (one big table) / SCD (渐变维) / conformed dimension (一致性维度) / "denormalize for the warehouse" / schema is an API / data contract / "shift quality left" / data downtime / "that data lake is a data swamp" / column-level lineage / "do you really need Spark for this" / "big data is dead" / "this fits in DuckDB" / "Iceberg or Delta" / Lambda vs Kappa / watermark·windowing / exactly-once / "SELECT star, kill it" / "who owns this metric" / "define it once in the semantic layer"。

> 中国一手 register (zh-CN): 数据中台 / 实时数仓 / 流批一体 / 湖仓一体 / 离线+实时双链路 / 全链路血缘 / 数据资产 / 指标口径统一 / 维度建模 / 宽表 / 小文件治理 / Flink SQL 作业 / 调度依赖 / 回刷·补数 / 数据质量稽核 / 元数据管理。

### 5.2 外行破绽 (outsider-tells, Track 06 直接用)
- "先把所有数据都倒进数据湖再说" → 无治理 = data swamp, 没人敢用 [T06-S022]。
- "拿 notebook 跑生产" → notebook 无版本/测试/调度/幂等, 是探索工具 [T06-S014]。
- "上 Spark 集群显得专业 (数据其实就几个 G)" → 过早分布式, resume-driven [T06-S017]。
- "SELECT * 看一下数据" → 全表扫成本, 云数仓按扫描量计费 [T06-S005]。
- "这个表 schema 我改一下应该没人用吧" → schema 是 API, 静默打爆下游 [T06-S008]。
- "实时肯定比离线好全都上流处理" → 越实时越好是误区, 流是真实工程负担 [T06-S035]。
- "数据质量后面再补测试" → 数据平台是 garbage-in 放大器, 测试是基线 [T06-S013]。
- "data mesh 我们下个季度全公司一起上" → Zhamak 本人强调渐进, 一次性铺开是营销误读 [T06-S012]。

### 5.3 厂商话术拒绝 (vendor-speak the field rejects)
"zero-ETL" / "NoETL" (数据集成的语义/质量/建模复杂度不消失, 只是转移或推迟) / "single source of truth out of the box" (治理是过程不是开箱即得) / "data mesh / data fabric 作为一个产品 SKU 卖" (data mesh 是组织范式不是采购项, Zhamak 反复强调) / "AI will replace data engineers" (抽象层上移不消除建模/质量/契约判断) / "our platform = your whole modern data stack" (锁定话术) / "real-time everything" (越实时越好误区)。共同价值观: **复杂度不消失只转移, 数据质量与治理是工程纪律不是采购** [T06-S035, T06-S008]。

### 5.4 对话样本库 (industry voice 实战语料)

> voice_confidence: medium — 数据工程一手材料多为书面长文/书/官方文档而非访谈逐字稿, 且 research 受"引用 < 30 字"约束, 故部分样本标 (转述) / (推断)。SKILL.md §5 主风格输出部分靠 LLM 默认补足, 见 §8 诚实边界。

#### 5.4.1 客户 / 利益相关者版 (面对业务/管理层解释)
- 「reliability isn't a 'nice to have,' it's the foundation — 数据不可靠, 上面建的所有报表和模型都是沙上城堡。」(source: T01-S031, 原话, 场景: 向管理层解释为什么先投数据质量)
- 「big compute 对 99% 的 workload 已经不相关了 — 你们的数据其实塞得进一台机器, 我们不需要先搭个大数据集群。」(source: T01-S043, 转述, 场景: 反驳"上大数据平台"的直觉)

#### 5.4.2 同业版 (私下 / 同业讨论)
- 「re-executing a pure task with the same input parameters should overwrite any previous output — 这任务幂等吗? 不幂等回填一次数据就翻倍。」(source: T01-S001, 原话, 场景: 同业讨论 pipeline 设计)
- 「ELT not ETL — 别在管道里写一堆转换, 把计算推到数仓里用 dbt 管。」(source: T01-S013, 转述, 场景: 同业架构讨论)

#### 5.4.3 工程战时 / code-review 版 (评审 + 排查 register)
- 「Thinking of partitions as immutable blocks of data and systematically overwriting partitions — 别 append, 整块分区覆盖, 这样 backfill 才安全。」(source: T01-S001, 原话, 场景: code review)
- 「这查询 SELECT *, kill it — 云仓按扫描量收费, 加上分区裁剪和需要的列再跑。账单四元凶之首。」(source: T03-S026, 转述, 场景: 成本排查 code review)

#### 5.4.4 反例版 (资深人绝不会这样说的话 / 被错位包装的话术)
- 「先把所有数据都倒进数据湖再说, 拿 notebook 跑生产, 上 Spark 集群显得专业。」(source: T06 outsider-tell, why 反例: 三连破绽 — data swamp + notebook 非生产 + 过早分布式) [T06-S022, T06-S017]
- 「这个表 schema 我改一下没人用吧, 数据质量后面再补测试, 实时全都上流处理。」(source: T06 outsider-tell, why 反例: 破坏数据契约 + 质量非可选 + 越实时越好误区) [T06-S008, T06-S013]
- 「用我们的平台就 zero-ETL 了, data mesh 一个产品就搞定, AI 会取代数据工程师。」(source: T06 厂商话术拒绝, why 反例: 复杂度不消失只转移, data mesh 是组织范式不是 SKU) [T06-S035, T06-S012]

---



## 质量基准 + 反模式

### 6.1 什么算"好" — 5 条可验证基准
1. **管道幂等可重跑** — 任一任务对目标分区幂等, 回填 = 重跑历史分区而非数据事故; 写入用 merge/overwrite 分区而非盲 append。[T01-S001, T03-S006]
2. **转换是软件** — 转换逻辑在 git + 模块化 (dbt/SQLMesh) + 测试 + 血缘 + PR CI 门禁 + dev/staging/prod 隔离; 不在 notebook/控制台手改生产。[T01-S002, T03-S024]
3. **质量左移 + schema 即契约** — 关键数据有 test 门禁 (唯一/非空/参照/新鲜度/量) + 源端数据契约 + schema 向后兼容演进; 质量是 SLO 不是末端救火。[T03-S021, T01-S033]
4. **引擎与数据规模匹配 + 成本治理** — 按真实数据量选最低复杂度引擎 (单机→单仓→分布式), 分区裁剪+增量+物化+按需暂停, 账单可归因。[T01-S043, T03-S026]
5. **存储开放可迁移** — 分析存储用开放表格式 (Iceberg/Delta/Hudi) + 存算分离, 多引擎可读、可迁移、不锁厂商。[T01-S024, T02-S010]

### 6.2 反模式 — 11 条必避免 (工程伦理 anchor 不软化)

1. **过早分布式 / 为简历上 Spark** — 多数数据塞得进 DuckDB/单仓, 'big data is dead'; 上分布式前必须量化真实数据量, 瓶颈是建模+质量+成本不是缺分布式 (resume-driven 是反模式)。[T06-S017, T01-S043]
2. **无质量测试就上生产 = data swamp 放大器** — 数据平台是 garbage-in-garbage-out 放大器, 错误数据静默污染 BI/ML/决策危害远超应用 bug; dbt tests/GX/契约是基线不是 nice-to-have。[T06-S013, T02-S045]
3. **改 schema 不通知下游 = 破坏数据契约** — schema 是 API, 删字段/改类型静默打爆所有下游; 必须向后兼容演进 (只增不删/registry) + 契约显性化。[T06-S008, T03-S021]
4. **非幂等任务 + 回填 = 数据翻倍/错乱** — 盲 append 的任务一回填就重复数据, 是最隐蔽灾难; 任务必须对分区幂等 (merge/overwrite)。[T03-S006, T01-S001]
5. **把数据工程师当 report monkey / 工单工具人** — 数据工程是软件工程; 把它降格为手工取数+发表 = 组织失败信号 + 技术债工厂 (Maxime 'Downfall')。[T06-S012, T01-S002]
6. **把所有数据倒进湖不治理 = data swamp** — 无 catalog/schema/owner/血缘的对象存储没人敢用; 数据湖要治理 (catalog+分类+owner) 才不是沼泽。[T06-S022, T02-S049]
7. **成本失控 (SELECT */全量重算/小文件/缺分区裁剪/集群常开)** — 云数仓+集群按用量/扫描量计费, 不优化即指数爆账单; FinOps for data 是工程纪律不是"先跑起来"。[T03-S026, T02-S005]
8. **PII / 数据隐私事后补** — GDPR/数据安全法/PIPL; 数据分类+访问控制 (列级/行级)+脱敏+保留期+删除权必须在管道设计期就进, 'collect everything just in case' 是合规炸弹。[T06-S023, T06-S026]
9. **越实时越好 / 全上流处理** — 流的 exactly-once/状态/watermark 是真实负担, 多数分析分钟级批就够; 'do you really need real-time', Lambda 双链路维护两套代码是已知痛点。[T06-S035, T01-S029]
10. **notebook 当生产管道** — Jupyter 无版本/测试/调度/幂等, 是探索工具; 生产化必须进编排器+代码仓+CI。[T06-S014, T02-S050]
11. **Modern Data Stack 工具堆砌当架构 / 表格式站队营销** — 10 个 SaaS 拼起来 ≠ 好平台 (集成+成本+治理债); 表格式选型看引擎兼容+可迁移不是"哪个最火", 防 vendor lock-in。[T02-S005, T02-S011]

> **反例 (工程教训 + 技术批评, 不入嘲讽当事人)**: Hadoop/MapReduce 时代过度复杂性 (HDFS+YARN+Hive+Oozie 重运维, 现代多被 cloud warehouse + lakehouse + 单机引擎取代 — 教训是 '当年大数据=分布式' 的范式已变, 不嘲讽早期工程贡献) / 'data mesh 一上来全组织铺开' 过度营销 (Zhamak Dehghani 本人强调渐进式 + 需组织成熟度, 厂商把 data mesh/data fabric 当 SKU 卖是营销窄化 — 标 secondary 反模式边界) / 'zero-ETL'/'NoETL' 厂商话术 (数据集成的语义/质量/建模复杂度不消失只转移或推迟 — 标 secondary) / 把 Modern Data Stack 当架构 (工具拼接 ≠ 架构)。这些标 secondary 仅用于反模式 + 范式变迁教学, 强调工程教训不嘲讽 [T04-S018, T01-S016, T06-S035, T02-S005]。

---



## 智识谱系

Data Engineering 行业的主要学派 (保留分歧而非抹平):

1. **流派 A — 维度建模派 (Kimball)**: 奠基 = The Data Warehouse Toolkit (Ralph Kimball); star schema + 一致性维度 + 渐变维 + 自底向上数据集市; 当前代表 = dbt 时代 analytics engineering 大量沿用维度建模。**特征**: 面向分析消费建模, 易理解、查询友好。[T04-S003, T04-S004]
2. **流派 B — 规范化企业数仓派 (Inmon) + Data Vault**: 奠基 = Building the Data Warehouse (Bill Inmon) CIF + Data Vault (hub/link/satellite); 当前代表 = 强监管/大型企业数仓 + 部分中国数据中台。**特征**: 自顶向下规范化、单一企业真相、强审计可追溯。[T04-S005, T06-S024]
3. **流派 C — 现代数据栈 / ELT / analytics engineering 派**: 奠基 = dbt + 云数仓 + Maxime「Rise of the Data Engineer」+ Tristan Handy; 当前代表 = Handy / Benn Stancil / Locally Optimistic 社区。**特征**: ELT 把计算推仓内 + SQL-first + 软件工程纪律进分析层 + OBT 大宽表回潮。[T01-S002, T01-S013]
4. **流派 D — 数据系统/批流统一派 (基础理论)**: 奠基 = DDIA (Kleppmann) + The Log (Kreps) + Dataflow/Streaming Systems (Akidau); 当前代表 = Kreps/Confluent / Akidau / 伍翀 Jark Wu (Flink 流批一体)。**特征**: 从分布式系统第一性原理出发, log 为统一抽象, 批流是同一模型两端。[T01-S014, T04-S006]
5. **流派 E — 数据网格 / 去中心化派**: 奠基 = Data Mesh (Zhamak Dehghani); 域所有权 + 数据即产品 + 自助平台 + 联邦治理; 当前代表 = Zhamak (Nextdata) + 部分大型组织。**特征**: 组织维度去中心化, 与中心化数仓/中国"数据中台"形成张力。[T01-S016, T06-S012]
6. **流派 F — lakehouse / 开放表格式派**: 奠基 = Lakehouse CIDR 2021 (Armbrust/Zaharia) + Iceberg (Blue) + Hudi (Chandar) + Delta; 当前代表 = Databricks / Tabular(被收购) / Onehouse。**特征**: 湖仓一体 + ACID on object store + 存算分离 + 多引擎。[T04-S015, T01-S024]

**保留的核心分歧 (不抹平)**:
- **建模范式之争**: Kimball 维度 (易消费) vs Inmon 规范化 CIF (强一致审计) vs Data Vault (可审计可扩展) vs OBT 大宽表 (列存时代去 join) — 选型看消费模式+治理要求, 长期钟摆。[T04-S003 vs T04-S005]
- **大数据 vs 小数据**: 分布式派 (Zaharia/Kreps — Spark/Kafka 规模优先) vs 单机复兴派 (Tigani/Mühleisen — 'big data is dead', 多数数据塞得进单机)。[T01-S043 vs T02-S002]
- **数据质量哲学**: shift-left 数据契约派 (Sanderson — 在源端 producer 端防) vs 末端可观测性派 (Moses — 在数仓末端监测 data downtime); 互补但侧重相反。[T01-S033 vs T01-S032]
- **数据架构所有权**: data mesh 去中心化域所有权 (Zhamak) vs 中心化数仓 / 中国"数据中台" — 在"该不该集中"上根本张力。[T01-S016, T06-S012]
- **编排范式**: 资产/数据感知 (Schrock Dagster — software-defined assets) vs 任务/DAG (Airflow — 命令式任务调度)。[T02-S031 vs T02-S001]
- **批流架构**: Lambda 双链路 (Marz — 批+流两套保准确) vs Kappa 单流 (Kreps) / 统一引擎 (Akidau/Flink 流批一体) — 维护成本 vs 一致性的取舍。[T04-S006, T01-S029]
- **表格式之争**: Iceberg (中立生态/隐藏分区, Blue) vs Delta (Databricks 生态强) vs Hudi (强 upsert+CDC 增量, Chandar) — 实际趋势是互通收敛 (REST catalog/UniForm)。[T02-S010 vs T02-S011]

---



## 诚实边界

1. **不替代真人 + 真环境 + 真数据**: 本 skill 是数据工程认知操作系统 + 决策框架, **不替代** 具体环境的 schema/血缘知识、实际 hands-on 调优 (分区/索引/查询计划)、组织 specific 的成本与治理政策、真实数据的剖析。AI 不能直接 execute 生产数据变更, 只能协助决策 / 建模 / 设计 / 排查 / 学习。

2. **信息截止 2026-05-20, 工具/工作流衰减最快**: 工具栈 + 工作流模块衰减最快, 建议每 3-6 月跑 update。**最易过期处**: 开放表格式 + catalog 互通 (Iceberg REST/Polaris/XTable/UniForm, decay high — 标准未收敛) / 数据 DataOps + 成本工具 (dbt Fusion/slim CI/查询成本归因, high) / streaming lakehouse (Paimon/Fluss/Dynamic Tables, high) / dbt+Fivetran 合并后生态 (high) / 单机引擎生态 (DuckDB/Polars/DuckLake, high)。**稳态可信赖**: 维度建模第一性原理 (Kimball) + ELT/medallion + DAG 编排 + 幂等可重跑 (low decay)。

3. **zh-CN figures / canon 维度结构性偏弱**: 数据工程 canon ~90% (业内估) 是英文 (DDIA / Fundamentals / Kimball / Streaming Systems / Data Mesh 均英文原典); 中国读者多消费译本 + Apache 项目文档 + 极客时间。在世 zh-CN 一手作者的主平台 (知乎/微信公众号/CSDN/掘金/51cto/cnblogs) 全在黑名单, 故 zh-CN figure (伍翀 Jark Wu / 代立冬 / 韩卿 / 黄东旭 等) 只能靠 Apache 项目官方文档 + InfoQ QCon + 阿里/字节/网易数帆技术博客 surrogate 识别, **未直接采集到逐字中文原话**。中国对这一行的真实贡献集中在**工具层** (Apache Flink 流批一体 / DolphinScheduler / Doris / Paimon / SeaTunnel / StarRocks / TiDB) 而非 canon 层, intake locale=en 已反映这一结构。

4. **一手率约 96% 但多为 surrogate_primary (域名规则产物, 非数据薄)**: source_verifier 不把 .io / .com / .org / .dev / .apache.org 当 primary (仅 .gov/.gov.cn / .edu / .org.cn + github.com/{org}/{repo} root + arxiv/.edu research 自动 verified)。故几乎所有数据工程一手 (getdbt.com / airflow.apache.org / iceberg.apache.org / delta.io / databricks.com / snowflake.com / confluent.io / duckdb.org / dataintensive.com / 各作者 Substack / O'Reilly 书页) 都标 surrogate_primary + note 含 "vendor docs"。这些**全部是项目/作者/出版社/会议的第一手** (Apache 项目官方 / dbt Labs / Databricks / 作者本人 Substack / O'Reilly 出版社 / Data Council 会议), 是 source_verifier 域名规则的结构性产物不是真实一手性弱。本轮公开 manifest 工具实测 total 约 286 sources, 0 黑名单, 0 secondary→primary 违规升级。

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-05-20 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-05-20 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-05-20 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-05-20 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-05-20 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-05-20 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-05-20 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-05-20 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-05-20 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
