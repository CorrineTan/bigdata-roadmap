### Spark very very basics
1. Two mode:
Local:
- LocalMode: -master local[2]
Cluster:
- Standalone --master spark://node1.com://7077

2. RDD is a data structure. And each hdfs block has 1 RDD partition, and matching to a task.

3. RDD vs MapReduce:

1). intermediate resule put into a distributed memory, instead of a HDFS block. 

![spark](https://github.com/CorrineTan/bigdata-roadmap/blob/main/Images/spark1.png)