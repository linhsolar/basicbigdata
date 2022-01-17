#!/usr/bin/env python3
## using spark-submit with local or yarn
#spark-submit --master local[*] spark_taxi_amount_calculation.py --input_file file:///opt/data/rawdata/nytaxi-2019download.csv --output_dir file:///opt/data/rawdata/taxiresult01
import csv
import sys
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import argparse
parser = argparse.ArgumentParser()
##local file system starts with file:///
## and hadoop filesystem starts with hdfs://
parser.add_argument('--input_file', help='input data file')
parser.add_argument('--output_dir',help='output dir')

args = parser.parse_args()

##define a context
#change the name suitable for your test
spark = SparkSession.builder.appName("nytaxicount").getOrCreate()
#NOTE: using hdfs:///..... for HDFS file or file:///
# To test the program you can prepare a small data file
inputFile =args.input_file
## hadoop inputFile="hdfs://"
df =spark.read.csv(inputFile,header=True,inferSchema=True)
df.show()
print("Number of trips", df.count())
#number of passenger count per vendor and total amount of money
passenser_exprs = {"passenger_count":"sum","total_amount":"sum"}
df2 = df.agg(passenser_exprs)
# Where do you want to write the output
df2.repartition(1).write.csv(args.output_dir,header=True)
