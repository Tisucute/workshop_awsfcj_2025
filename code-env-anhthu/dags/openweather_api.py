
# =============================
# DAG: openweather_api_dag
# Lấy dữ liệu thời tiết từ OpenWeather API, lưu vào S3
# =============================
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import pandas as pd
import requests
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator


# Thông số mặc định cho các task trong DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 3),  # Đảm bảo giống với các DAG ETL phía sau
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}


# Định nghĩa DAG Airflow: chạy mỗi giờ, không catchup
with DAG(
    'openweather_api_dag',
    default_args=default_args,
    schedule_interval='@hourly',  # Chạy mỗi giờ
    catchup=False
) as dag:


    # Định nghĩa endpoint và tham số API
    # Có thể dùng /forecast (dự báo 5 ngày) hoặc /weather (thời tiết hiện tại)
    api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    api_params = {
        'q': 'Thanh pho Ho Chi Minh, VN',  # Địa điểm lấy dữ liệu
        'appid': Variable.get('key'),      # API key lấy từ Airflow Variable (bảo mật)
        'units': 'metric'                  # Đơn vị nhiệt độ
    }


    # Hàm lấy dữ liệu từ OpenWeather API, chuyển thành DataFrame, đẩy lên XCom
    def extract_openweather_data(**kwargs):
        """
        Gọi OpenWeather API, chuẩn hóa JSON, tách các trường weather, build DataFrame, đẩy CSV lên XCom.
        """
        # Gọi API lấy dữ liệu thời tiết
        resp = requests.get(api_endpoint, params=api_params)
        resp.raise_for_status()
        data = resp.json()

        # Nếu là forecast thì có 'list', còn weather thì là 1 record
        entries = data.get('list', [data])
        records = []
        ingest_time = datetime.utcnow().isoformat()  # Thời gian lấy dữ liệu
        for rec in entries:
            # Lấy các trường cơ bản
            base = {
                'dt': rec.get('dt'),
                'dt_iso': datetime.utcfromtimestamp(rec.get('dt')).isoformat() if rec.get('dt') else None,
                'temp': rec.get('main', {}).get('temp'),
                'feels_like': rec.get('main', {}).get('feels_like'),
                'pressure': rec.get('main', {}).get('pressure'),
                'humidity': rec.get('main', {}).get('humidity'),
                'wind_speed': rec.get('wind', {}).get('speed'),
                'city': rec.get('name', data.get('city', {}).get('name', '')),
                'country': rec.get('sys', {}).get('country', data.get('city', {}).get('country', '')),
                'ingest_time': ingest_time
            }
            # Lấy thông tin weather đầu tiên
            w = rec.get('weather', [{}])[0]
            base.update({
                'weather_id':           w.get('id'),
                'weather_main':         w.get('main'),
                'weather_description':  w.get('description'),
                'weather_icon':         w.get('icon')
            })
            records.append(base)

        # Tạo DataFrame và chuyển thành CSV string
        df = pd.DataFrame(records)
        csv_str = df.to_csv(index=False)


        # Đẩy dữ liệu CSV lên XCom để task sau lấy dùng
        ti = kwargs['ti']
        ti.xcom_push(key='final_data', value=csv_str)


    # Task 1: Lấy dữ liệu từ API, đẩy lên XCom
    extract_api_data = PythonOperator(
        task_id='extract_api_data',
        python_callable=extract_openweather_data,
        provide_context=True
    )


    # Task 2: Upload dữ liệu lên S3 (bucket raw)
    upload_to_s3 = S3CreateObjectOperator(
        task_id='upload_to_S3',
        aws_conn_id='AWS_CONN',
        s3_bucket='airflowoutputtos3bucket-324413232937-us-east-1',
        s3_key='raw/weather_api_data.csv',
        data="{{ ti.xcom_pull(key='final_data') }}",
        replace=True
    )


    # Định nghĩa thứ tự: lấy dữ liệu xong mới upload lên S3
    extract_api_data >> upload_to_s3
