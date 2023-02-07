### Hive Introduction

SQL-like interface to query data in HDFS. Translate most query to mapreduce job.

HQL: query data stored in Hadoop. 

Hive maps high level SQL operations to low level MapReduce Java API/Tez ApI.

### Hive Use Cases

 - Data Warehouse applicaitons 

 - Integration easy with Spark and HBase

 - Allows users to run SQL

 - Support querying data from different formats (JSON)
 
 ### Basic Hive Script

 ```
create table foo(x int);
show databases;
use default
show tables;
INSERT INTO TABLE foo VALUES ('1');
select * from default.foo;
 ```

 ### Beeline and HUE

 A JDBC client based on the SQL Line CLI.
 HUE - Hadoop User Experience

 ### Hive Metastore

 #### Metastore Purpose
 Purpose: contains a description of the table, and underlying data on which it is built, but doesn't contain actual user data.

 Need to create external metastore - if master node is down, data stored in temporary EBS volumes or Instance Store get disappeared.

 External Metastore:

 1). AWS Glue Data Catalog as Hive Metastore

 2). External RDBMS (MySQL, Orcale), or RDS. Using an external MySQL database or Amazon Aurora

 #### Metastore mode

 1. Remote metastore mode

 - Runs in its own JVM process.

 - Other processes communicate with it using Thrift network API (javax.jdo.option.ConnectionURL property)

 - By default, metastore db is a mysql engine running on master ndoe - listing on 3306

 - org.mariadb.jdbc.Driver connector for the JDBC connection

 2. Embedded Metastore mode

 - Metastore use a Derby database

 - Database and Metastore are embedded in HiveServer JVM Process

 3. Local Metastore

 - Metastore run in same process as main HiveServer process

 - Metastore database runs in a seprated process

 #### Connect to Metastore

 1. Connect to metastore and explore tables:

 /etc/hive/conf.dist/hive-site.xml

 javax.jdo.option.ConnectionPassword
 javax.jdo.option.ConnectionUserName

 mysql -h ip-172-31-24-49.us-west-2.compute.internal -u hive -p
 show databases;
 use hive;
 show tables;
 select * from TBLS;
 select * from VERSION;

 2. Identify the Daemon on which metastore is running and stop/start it


 ### Hive Schema Tool

 - offline tool: Hive Metastore schema manipulation

 - initialze the Metastore schema for current Hive version, and handle upgrading schema

 - EMR use Hive Schema tool for schema verification. Initialize schema if it's not present on URL speicified on hive-site.xml

 - Hive schema initialization logs can be found in Provision node logs on master node

 ### HiveServer2

 - Service that enables clients to executor queries against Hive

 - Large concurrent connections cause OOM

 - Thrift: 10000 to connection with Beeline and Hue

 ### How does HiveServer2 works

 The thrift-based hive service is the core of HS2. responsible for servicing Hive queries.

Overall:

 1. JDBC Client(beeline): creates a HiveConnection by initiating a transport connection (e.g. TCP connection) followed by an OpenSession API call to get a SessionHandle

 2. HiveStatement is executed, and an ExecuteStatement API call is made from the Thrift client.

 In the API call, SessionHandle info is passed to the server with query info

 3. HS2 server: receives the request, ask driver(CommandProcessor) for query parsing and compilation.

 4. Driver(CommandProcessor): kicks off background job to talk to Hadoop, and immediately returns a response to client. 

 Response contains: an OperationHandle created from the server side.

 5. Client: uses the OperationHandle to talk to HS2 to poll the status of query execution.

 ### HiveQL

 1. DDL: creating/altering/dropping databases, tables, views, functions, indexes

 2. DML: put data into Hive tables, extract data to filesystem, manipulate data

 ### Hive on MapReduce Engine

 Hive runs Hive query as a traditional MR job. change by setting:
 hive.execution.engine = mr

Flow:

1. Driver execute query from UI

2. Compiler getPlan from Driver

3. Metastore getMetadata from Compiler

4. Metastore sendMetadata to Compiler

5. Compiler sendPlan to Driver

6. Execution Engine executePlan from Driver

6.1 Job Tracker executeJob from Execution Engine 

Meanwhile, MetaStore and Execution engine is sending MetadataOps for DDLs with each other

6.2 Job Tracker send a JobDone to Executor Engine

6.3 Task Tracker (Map)/(Reduce) do the DFS operation from Job Tracker

7. UI send fetchResults from Driver

8. ExecutionEngine sendResults to Driver

9. ExecutionEngine fetchResults from DataNode 

### Hive on Tez 

TEZ: Default execution engine starting from EMR 5.0.0

Tez engineer is better than MR engine:

No longer having multiple stages with each stage result saved on HDFS. It use a single job. And Tez can split map and reduce jobs into smaller tasks

How does Tez speed up:

(tbd)

### Tez Components

#### Tez AppMaster
(tbd)

#### Tez Task (in YARN container)
(tbd)

#### Client-side process
(tbd)

#### Tez - Container Re-use
(tbd)

#### Tez - Sessions
(tbd)

#### Tez - Customization Core Engine
(tbd)

#### Tez UI and Local Mode
(tbd)

#### Databases and tables in Hive

























