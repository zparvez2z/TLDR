### Introduction to Data Engineering

**Tools or the Data Egineer**
* Database(eg: MySql, Postgres)
* Proessing(eg: Spark, Hive)
* Scheduling(eg: Airflow, cron)

**Parallel Computation Framework**
Old framework
* Apache Hadoop
    * HDFS
    * Map reduce
* Hive(Sits on top of hadoop)
    * HiveSQL

new framework
* Apache Spark
    * In memory processing
    * RDD
**Resilient distributed dataset**
    * Don't have named column
    * Tranformation (eg: .map() or .filter() )
    * Action( eg: .count() or .first() )