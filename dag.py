from prefect import flow, task
from pipeline_6may import create_spark, bronze, silver, gold

@task(persist_result=False)
def run_bronze(spark):
    return bronze(spark)

@task(persist_result=False)
def run_silver(spark, path):
    return silver(spark, path)

@task(persist_result=False)
def run_gold(spark, path):
    return gold(spark, path)

@flow
def pipeline_flow():
    spark = create_spark()

    bronze_path = run_bronze(spark)
    silver_path = run_silver(spark, bronze_path)
    run_gold(spark, silver_path)

if __name__ == "__main__":
    pipeline_flow()