## Pyspark

#### DataFrame Basics
```
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Basics").getOrCreate()
df = spark.read.json("people.json")
df.show()
df.printSchema()
df.columns     ==> list of data column names
df.describe().show()
```

```
from pyspark.sql.types import (StuctField, StringType, IntegerType, StructType)

data schema = [StructField('age', IntegerType(), True),
			   StructField('name', StringType(), True)]
final_struc = StuctType(fields=data_schema)
df = spark.read.json("people.json", schema = final_struc)
```