## Notes Udemy course - Apache Spark

#### Install Pyspark
- To check where does it install:
```
echo 'sc.getConf.get("spark.home")' | spark-shell
```

- By default, Homebrew install all packages into the following directory in all versions of Mac OS. You can easily find home of maven, fish, wget, apache-spark etc at below location
```
/usr/local/Cellar/
```
For me, it's:
```
scala> sc.getConf.get("spark.home")
res0: String = /usr/local/Cellar/apache-spark/3.3.1/libexec
```

#### Spark Knowledge
"A fast and general engine for large-scale data processing."

Spark can slice and dice the data up; distribute processing amongst a huge cluster of computers; divide and conquer:
<img src="https://github.com/CorrineTan/spark-roadmap/blob/main/Images/spark_high_level.png" height="288" width="500">

Hadoop MapReduce is 100 times slower than Spark in some cases, and 10 times faster on disk. (Becaused it use Directed Acyclic Graph engine)

#### RDD - Resilient Distributed Dataset
- Spark Context: created by Driver Program; responsible for making RDD's resilient and distributed; create RDD's; Spark shell creates a "sc" object for you.

- SC to RDD

sc.textfile(file:///path) or sc.textfile(s3n:///path) or sc.textfile(hdfs:///path)

- Create RDD from Hive: 
```
hiveCtx = HiveContext(sc) 
rows = hiveCTX.sql("SELECT ...")
```
- RDD can alse be created from: 

JDB/ODBC(interface of SQL database), Cassandra(no SQL database), HBase, ElasticSearch, JSON/CSV/object/sequence files

- Transformation for RDD's:

Map: input-function-output, 1:1 relationship

FlatMap: 1:n relationship

Filter: filter out values

Others: Distinct, Sample. Union, Intersection, Subtract, Cartesian

- RDD Actions:

Collect: dump out all the values that are in there right now and just print it all out whatever you want to do with them

Count: count values in it

countByValue: breakdown by unique value

Take/Top: lets you sample a few values from RDD results

Reduce: combine all different values for a given key value and boik things down into a summation/aggregation of your RDD

- Lazy Evaluation:

Nothing actually happens in your drive program, until and action is called.

#### Example code 1: fundemental RDD usage - 
https://github.com/CorrineTan/spark-roadmap/blob/main/Udemy-Spark-Course/count_ratings.py

Data source:  MovieLens 100K Dataset  - https://grouplens.org/datasets/movielens/100k/

#### Key/Value RDD's
- Just map pairs of data into RDD. e.x.
```
totalsByAge = rdd.map(lambda x: (x,1))
```

- Special things Spark do for special stuff with Key/Value data:

reduceByKey(): combine values with the same key using some function. e.x.
```
rdd.reduceByKey(lambda x, y: x+y)         --- adds them up
```

Sort RDD by key values: sortByKey()

keys(), values(): create an RDD for just keys or values
