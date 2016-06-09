import os
from pyspark import SparkContext, SparkConf


def main():
    # Spark Configurations
    conf = SparkConf()
    conf.set("spark.master", "local[*]")
    conf = conf.setAppName('WordCount')
    sc = SparkContext(conf=conf)

    # Load README
    readme_rdd = sc.textFile(os.path.join(os.path.dirname(__file__), "../README.md"))

    # WordCount
    print (readme_rdd.flatMap(lambda line: line.split())
           .map(lambda word: (word.lower(), 1))
           .reduceByKey(lambda a, b: a + b)
           .map(lambda x: (x[1], x[0]))
           .sortByKey(ascending=False)
           .map(lambda x: (x[1], x[0]))).take(5)


if __name__ == "__main__":
    main()
