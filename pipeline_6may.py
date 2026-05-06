from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

def create_spark():
    return SparkSession.builder \
        .master("local[*]") \
        .appName("Pipeline") \
        .getOrCreate()

def bronze(spark):
    df = spark.read.csv("patients.csv", header=True, inferSchema=True)
    df.write.mode("overwrite").parquet("output/bronze")
    return "output/bronze"

def silver(spark, path):
    df = spark.read.parquet(path)

    df_incremental = df.filter(col("visit_date") > "2024-01-01")
    df_clean = df_incremental.fillna({"billing_amount": 0})
    df_clean = df_clean.dropDuplicates(["patient_id"])

    df_clean.write.mode("overwrite").parquet("output/silver")
    return "output/silver"

def gold(spark, path):
    df = spark.read.parquet(path)

    df_gold = df.groupBy("diagnosis") \
        .agg(sum("billing_amount").alias("total_billing"))

    df_gold.write.mode("overwrite").parquet("output/gold")
    return "output/gold"