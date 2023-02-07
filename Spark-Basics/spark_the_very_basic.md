### Spark very very basics

1. Two mode:
Local:
- LocalMode: -master local[2]
This is to just start a JVM process.

Cluster:
- Standalone --master spark://node1.com://7077
Driver: Job (scheduler running) + Exectutors (running task and caching the data)


2. RDD is a data structure. And each hdfs block has 1 RDD partition, and matching to a task.

3. RDD vs MapReduce:

1). Spark: intermediate result put into a distributed memory RDD, instead of a disk HDFS file system (lots of IO, serializaiton/deserialization cost)

![spark1](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark1.png)

2). Spark Scheduler use DAG: Transformation+action. And Task running using thread, instead of process.

4. Spark's data stored in HDFS. AND Spark code running on YARN.

5. Install spark: spark_env.sh, JAVA_HOME, SCALA_HOME, HADOOP_CONF_DIR

6. Running spark-shell: 4040 prot. sc: SparkContext.  spark: SparkSession

7. Running a spark application:

1) Read data: val inputRDD = sc.textFile()

2) Processing: inputRDD.flatMap.map.reduceByKey

![spark2](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark2.png)

8. Spark Standalone: similar to Hadoop YARN.

Masters + Workers

Master: Resource Manager in Hadoop. The resource of all cluster

Workers: Node Manager in Hadoop. The resource of every node, run the executor.

9. HA: 1). Multiple masters.  2). Zookeper to coordiante: vote + monitor

10. Cluster mode:

Driver Program: application manager  ===> AppMaster in Hadoop 

Executors: Thread pool: running task and caching the data.  ===> MapTask and ReduceTask in Hadoop

Both Driver and Executors are JVM process. 

Every task running on executor (thread pool) is thread. 

Driver: need to determine memory, CPU core

Exectutor: need to determine numbers, meomory(execution, storage), CPU core.

11. Spark entrypoint: SparkContext. 

val sparkConf: sparkConf => master, appName

val sc: sparkContext

12. Spark Core: 

- RDDs: resilient distributed datasets

Shared variables:

- Accumulators

- Broadcast variables

