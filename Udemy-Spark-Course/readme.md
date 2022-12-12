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

<img src="https://github.com/CorrineTan/spark-roadmap/blob/main/Images/spark_high_level.png">
