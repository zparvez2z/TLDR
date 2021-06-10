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

 
