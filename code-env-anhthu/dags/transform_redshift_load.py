
# =============================
# DAG: transform_redshift_dag
# Orchestrate ETL pipeline: chờ dữ liệu từ API, sau đó chạy Glue Job để ETL vào Redshift
# =============================
from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from datetime import datetime, timedelta


# Thông số mặc định cho các task trong DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 3),  # Đảm bảo giống với DAG lấy dữ liệu
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# Định nghĩa DAG Airflow: chạy mỗi giờ, không catchup
dag = DAG(
    'transform_redshift_dag',
    default_args=default_args,
    schedule_interval='@hourly',  # Chạy mỗi giờ, đồng bộ với DAG lấy dữ liệu
    catchup=False
)


# Task 1: Chờ DAG openweather_api_dag (lấy dữ liệu từ API) hoàn thành thành công trước khi ETL
wait_openweather_api = ExternalTaskSensor(
    task_id='wait_openweather_api',
    external_dag_id='openweather_api_dag',  # Tên DAG lấy dữ liệu từ OpenWeather API
    external_task_id=None,                  # Chờ toàn bộ DAG thành công
    timeout=2000,                          # Timeout (giây)
    dag=dag,
    mode='reschedule',
    allowed_states=["success"]
)


# Task 2: Trigger Glue Job để ETL dữ liệu từ S3 vào Redshift
transform_task = GlueJobOperator(
    task_id='transform_task',
    job_name='glue_transform_task',  # Tên Glue Job đã tạo sẵn
    script_location='s3://aws-glue-assets-324413232937-us-east-1/scripts/transform.py',  # Đường dẫn script ETL
    aws_conn_id='AWS_CONN',         # Kết nối AWS trong Airflow
    region_name="us-east-1",
    iam_role_name='data-workshop-anhthu-RedshiftIamRole-wTwBvtcZavdl',  # IAM Role cho Glue
    create_job_kwargs={
        "GlueVersion": "4.0",
        "NumberOfWorkers": 2,
        "WorkerType": "G.1X",
        "Connections": {"Connections": ["redshift-demo-connection"]}  # Kết nối Glue với Redshift
    },
    # Nếu muốn truyền tham số động cho Glue Job, mở comment bên dưới:
    # job_arguments={
    #     "--SOURCE_S3_PATH": "s3://airflowoutputtos3bucket-324413232937-us-east-1/raw/weather_api_data.csv"
    # },
    dag=dag,
)


# Định nghĩa thứ tự: phải chờ lấy dữ liệu xong mới ETL
wait_openweather_api >> transform_task
