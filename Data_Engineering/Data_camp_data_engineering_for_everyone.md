### Data Engineering for everyone

**Data Engineers Deliver:**
* The correct data
* In the right form
* To the right people
* As efficiently as possible

**The Five V's of Big Data:**
* Volume (the quantity of data points )
* Variety (type and nature of data)
* Velocity (how fast the data is generated and processed)
* Veracity (how trustworthy the sources are)
* Value (how actionable the data is)

**Data Engineer VS Data Scientist:**
Data Engineer | Data Scientist
------------ | -------------
Ingest and Store Data | Exploit Data
Setup databases | Access databases
Build data pipelines | Use pipelines outputs
Strong software skills | Strong analytical skills

**Data Pipelines:**
<p> A data pipeline is the series of steps required to make data from one system useful in another. The steps might include ingesting, transforming, processing, publishing or moving data. </p>

![data_pipelines](images/data_pipelines.png)

Things that must be considered:
**Automate:**
* Extracting
* Transforming
* Combining
* Validating
* Loading

**Reduce**
* Human intervention
* Errors
* The time it takes to flow

**ELT**
* Extract
* Transform
* Load

**some points about pipelines:**
* Move data from one system to another
* May or may not follow ETL
* Data may not be transformed
* May be directly loaded

**Data Structure**
* Structured ( Relational DB)
* Semi-Structured(json, xml, yaml)
* Unstructured (usually Data Lakes)

**Data Lakes VS Data WareHouse**
Data Lakes | Data WareHouse
------------ | -------------
Store all raw data | Specific data for specific use
Unstructured | Structured
Cost effective | More costly to update
Difficult to analyze | Optimized for data analysis
Requires up-to-date data catalog | - 
Mainly analyzed by Data Scientists | also by Data Analyst and Business Analyst
Big Data, real time analytics | Ad-hoc, read-only queries

**Data Catalog for Data Lakes**
* Source of data
* where data is being/has been used
* Owner of the data
* Frequency of data update
* data governance
* Ensure reproducibility
* No catalog -> data swamp

**Data Processing**
<p> Converting data into useful information </p>

**Value of Data Processing:**
* Remove unwanted data
* To save memory
* Convert data to another type
* Organize data
* To fit into schema / Structure
* Increase productivity

**Scheduling data:**
* Manual Scheduling
* time Scheduling
* Sensor Scheduling

**Batch and Stream data**
* Batches
    * Group records at intervals
    * often cheaper

* Stream
    * Send individual record

**Parallel Processing:**
<p>Parallel processing can be described as a class of techniques which enables the system to achieve simultaneous data-processing tasks to increase the computational speed of a computer system.</p>

* Benefit
    * Processing power (distributing task)
    * Memory (partitioning data)
* Risk
    * Communication overhead
    * Task need to be large
    * need several processing unit

[My certificate of accomplishment](certificates/Data_camp-Engineering_for_Everyone.pdf)