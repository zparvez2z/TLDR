### Introduction to Data Engineering

**Tools or the Data Engineer**
* Database(eg: MySql, Postgres)
* Processing(eg: Spark, Hive)
* Scheduling(eg: Airflow, cron)

**Parallel Computation Framework**
*Old framework*
* Apache Hadoop
    * HDFS
    * Map reduce
* Hive(Sits on top of hadoop)
    * HiveSQL

*new framework*
* Apache Spark
    * In memory processing
    * RDD
**Resilient distributed dataset**
    * Don't have named column
    * Transformation (eg: .map() or .filter() )
    * Action( eg: .count() or .first() )

**PySpqrk**
* Python interface to spark
* Dataframe abstraction
* Very similar to pandas

**Workflow Scheduling FrameWork**
 * Apache AirFlow
 * Term: DAG( Directed acyclic graph)

 **Extract**

 Extract from:
* Unstructured data(eg: plain text(pragraph), flat files(tsv,csv))
* Semi-Structured(eg: json)
* Structured( databases)

**Databases**
Application Database | Analytical Databases
---------------------|---------------------
OLTP                 | OLAP
Row oriented         | Column oriented

*Excercises*
* Fetch from API
* Read from DB(Postgres)

**Transform**

