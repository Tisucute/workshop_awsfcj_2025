# =============================
# AWS Glue ETL Script
# Đọc dữ liệu thời tiết từ S3, chuyển đổi, nạp vào Redshift
# =============================

import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

# 1) Khởi tạo Glue Job, đọc tham số JOB_NAME (bắt buộc cho Glue)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 2) Đọc file CSV dữ liệu thời tiết từ S3 (do Airflow upload lên)
input_s3_path = "s3://airflowoutputtos3bucket-324413232937-us-east-1/raw/weather_api_data.csv"
dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="csv",
    format_options={"withHeader": True, "inferSchema": True},
    connection_options={"paths": [input_s3_path]},
    transformation_ctx="dyf_raw"
)

# 3) Chuyển đổi kiểu dữ liệu: epoch -> timestamp cho dt, chuẩn hoá các trường thời gian
from pyspark.sql.functions import col, to_timestamp, from_unixtime

df = dyf.toDF() \
    .withColumn("dt", to_timestamp(from_unixtime(col("dt")))) \
    .withColumn("dt_iso", to_timestamp(col("dt_iso"))) \
    .withColumn("ingest_time", to_timestamp(col("ingest_time")))

dyf = DynamicFrame.fromDF(df, glueContext, "dyf_casted")

# 4) Ghi dữ liệu vào Redshift, tạo bảng nếu chưa có (bổ sung các cột dashboard cần)
preactions = """
  CREATE TABLE IF NOT EXISTS public.weather_data (
    dt                    timestamp,
    dt_iso                timestamp,
    temp                  double precision,
    feels_like            double precision,
    pressure              integer,
    humidity              integer,
    wind_speed            double precision,
    weather_id            integer,
    weather_main          varchar(100),
    weather_description   varchar(255),
    weather_icon          varchar(50),
    city                  varchar(100),
    country               varchar(10),
    ingest_time           timestamp
  );
"""
glueContext.write_dynamic_frame.from_options(
    frame=dyf,
    connection_type="redshift",
    connection_options={
        "dbtable":      "public.weather_data",
        "preactions":   preactions,  # Tạo bảng nếu chưa có
        "aws_iam_role": "arn:aws:iam::324413232937:role/data-workshop-anhthu-RedshiftIamRole-wTwBvtcZavdl",
        "redshiftTmpDir":"s3://aws-glue-assets-324413232937-us-east-1/temporary/",
        "useConnectionProperties": "true",
        "connectionName":"redshift-demo-connection"
    },
    transformation_ctx="redshift_write"
)

# 5) Kết thúc Glue Job
job.commit()
