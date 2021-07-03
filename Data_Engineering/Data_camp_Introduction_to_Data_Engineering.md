### Introduction to Data Engineering

**Tools or the Data Engineer**
* Database(eg: MySql, Postgres)
* Processing(eg: Spark, Hive)
* Scheduling(eg: Airflow, cron)

**Parallel Computation Framework**

* *Old framework*
    * Apache Hadoop
        * HDFS
        * Map reduce
    * Hive(Sits on top of hadoop)
        * HiveSQL

* *new framework*
    * Apache Spark
        * In memory processing
        * RDD

**Resilient distributed dataset**
* Don't have named column
* Transformation (eg: .map() or .filter() )
* Action( eg: .count() or .first() )

**PySpark**
* Python interface to spark
* Dataframe abstraction
* Very similar to pandas

**Workflow Scheduling FrameWork**
 * Apache AirFlow
 * Term: DAG( Directed acyclic graph)

 **Extract**

 Extract from:
* Unstructured data(eg: plain text(paragraph), flat files(tsv,csv))
* Semi-Structured(eg: json)
* Structured( databases)

**Databases**
Application Database | Analytical Databases
---------------------|---------------------
OLTP                 | OLAP
Row oriented         | Column oriented

*Exercises*
* Fetch from API
* Read from DB(Postgres)

**Transform**

*Exercises*
* Splitting the rental rate
* Prepare for transformation
* Joining with rating

**Load**

Column VS row oriented DB

Column(Analytics) | Row(Application)
------------------| ----------------
Store per column  | Stored per second
Parallelization     | Added per transaction

*term: MPP DB (Massively Parallel Processing)*

Example:
* Amazon Redshift
* Azure SQL Data Warehouse
* Google bigQuery

*Redshift example:*
* write files to s3 -> Send copy query to Redshift
* csv -> paraquet
* Load to postgres (code example)

*Exercise*
* OLAP or OLTP
* write to file
* Load into postgres

*Encapsulate everything into functions*

**Putting is all together**

* *The ELT function*
    * extract_table_to_df()
    * split_columns_transform()
    * load_df_into_db()

**Airflow**

*exercise*
* defining a DAG
* setting up Airflow
* interpreting the DAG

**Case Study - Data camp course recommendation**

* *Recommendation Technique*
    * Matrix factorization
    * Common sense transformation

* *Recommendation Strategy*
    * Use technology that user has rated most
    * Don't recommend what's already rated
    * Recommend the highest rated courses from the remaining.

* *Exercise*
    * filter corrupt data
    * using the recommendation transformation

