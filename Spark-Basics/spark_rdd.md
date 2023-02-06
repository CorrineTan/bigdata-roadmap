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


