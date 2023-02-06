### Spark RDD Basics

- RDDs: Resilient Distributed Datasets

- a distributed memory abstration

- in-memory computations on large cluster

- fault-tolerant

- immutable, partitioned collection of elements that can be operated on in parallel

Abstract:

![spark3](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark3.png)

### RDD property:

1. A list of partitions

![spark5](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark5.png)

2. A function for computing each split

![spark6](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark6.png)

3. A list of dependencies on other RDDs

![spark7](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark7.png)

![spark4](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark4.png)

4. (optional) A partitioner for key-value RDDs (e.g. RDD is hash-parititioned/range-parititioned) (if it's non key-value RDDs, paritioner is None)

![spark8](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark8.png)

5. (optional) A list of preferred locations to compute each split on (block locations for HDFS file)

![spark9](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark9.png)


Where does dataset comes from: 2 & 3

Where is dataset, how to partition: 1, 4 & 5.

### WordCount example

![spark11](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark11.png)

![spark10](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark10.png)

### Create RDD

1. Parallelized Collections
From a local scala collection to from an RDD.
For developing/testing

parallelize:
![spark12](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark12.png)

MakeRDD:
![spark13](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark13.png)

2. External Data
From HDFS, HBase, ElasticSearch, Kafka

textFile:
![spark14](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark14.png)

To handling small files: wholeTextFiles():
![spark15](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark15.png)


### Determine RDD Partition number

```
1. rdd.getNumPartitions

2. rdd.partitions.length
```

1.  Best to set 2, 3 times of CPU Core number to. For example:

If read from HDFS, 100 blocks. Better set executor's CPU Core to 100/2 to 100/3 = 30 to 50.

2. Read from HDFS, RDD partition number should be block number

3. Read from HBase, RDD partition number should be region number

### RDD TWO types: Transformation, Action

1. Transformation: return a new RDD

Lazy.
Creates a new dataset from an existing one. 
ex: map, filter

![spark16](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark16.png)

2. Action: return nonRDD(null or others)

Eager.
return a value to driver program after running a computation on database.
ex: count, first, collect, take, reduce, saveAsTextFile

![spark17](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark17.png)


### RDD Transformation Function

#### mapPartitions, foreachPartition

Map and foreach, is pointing to each item. And it's too much. We need to do it towards each partition instead.

![spark18](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark18.png)

#### repartition

Reason to use: 
```

1. dataset is less, but paritition is a lot. Need to reduce # of partitions

2. read from external HBase. By default, 1 region is 1 paritition. If 1 region is exceed 5GB, need to increase partitions.
```

1. repartition: increase partition. But be cautious! Shuffle!

2. coalesce: decrease partition. No shuffle.

3. partitionBy: adjust # opartition

When to increase RDD:  too many data

When to decrease RDD: 

1. after filter, each partition has less data. need to decrease partition

2. store the RDD storage to external systems. need to decrease.


#### aggregation

- reduce and fold. fold is more power, can initialize intermediate temp variable.

![spark19](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark19.png)

- aggregation: seqOp and combOp

![spark20](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark20.png)

![spark21](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark21.png)

- PairRDDFunctions Aggregations:

groupByKey   ===> easy to get data skew!!! OOM

reduceByKey and foldByKey

aggregateByKey

Difference between groupByKey and reduceByKey:

reduceByKey:
![spark22](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark22.png)

#### joins
![spark26](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark26.png)


groupByKey:
![spark23](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark23.png)

### RDD persist

![spark25](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark25.png)

### RDD CheckPointing

Save the dataset to HDFS. 

![spark24](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark24.png)

No lineage anymore. 

Persist and Cache will still have dependencies and lineage. Thus unreliable for executor down. 
