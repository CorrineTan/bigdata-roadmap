## Notes for Taming Big Data with Apache Spark and Python - Hands On!

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