from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age, numFriends)

lines = sc.textFile("fakefriends.csv")
rdd = lines.map(parseLine)

# input: (id, name, age, number of friends)   output: (age, numFriends)
# rdd.mapValues(lambda x: (x, 1)) => (33, (385,1))     (33, (2,1))
# .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) => (33,(387,2))
totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

# totalsByAge.mapValues => (33, 193.5)
averagesByAge = totalsByAge.mapValues(lambda x: x[0] / x[1])

results = averagesByAge.collect()
for result in results:
    print(result)
