from pyspark import SparkConf, SparkContext
import collections

# sparkconf and sc object setup
conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

# RDD created
lines = sc.textFile("ml-100k/u.data")
# Map - Lambda function
ratings = lines.map(lambda x: x.split()[2])
# turple returned for countByValue action of RDD: ex. 3 star shows 27145 times - (3,27145)
result = ratings.countByValue()

# create an ordered dictionary by turple item (first element), and print it out
sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
