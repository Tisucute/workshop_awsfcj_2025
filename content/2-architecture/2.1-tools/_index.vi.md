---
title : "Các công cụ được sử dụng"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.1 </b> "
---
### Các công cụ được sử dụng

#### 1. Data Ingestion

- **OpenWeather API**: Nguồn dữ liệu thời tiết thời gian thực (temperature, humidity, v.v.) qua RESTful endpoint.
- **Python Script**: 
  - Gọi API, parse JSON, làm sạch sơ bộ (ví dụ: chuyển timezone, chuẩn hoá tên trường…)
  - Xuất file (CSV/Parquet/JSON) và ghi lên Amazon S3.

#### 2. Staging & Storage

- **Amazon S3 Bucket**:
  - Raw zone: chứa file thô do Python script tạo.
  - /dags: nơi lưu definition của Airflow DAGs.
  - requirements.txt: liệt kê dependencies (requests, boto3, pandas…) để Airflow tự động cài trước khi chạy task.

#### 3. Transformation

- **AWS Glue**:
  - Glue Crawler (tuỳ chọn): tự động phát hiện schema từ file raw trên S3 và tạo table metadata trong Data Catalog.
  - Glue ETL Job: chạy Scala/Python Spark để:
    - Đọc dữ liệu từ S3 (raw)
    - Làm sạch/biến đổi (ví dụ: filter records, join thêm lookup table, enrichment…)
    - Xuất dữ liệu đã transform sang S3 clean zone hoặc trực tiếp load vào Redshift.

#### 4. Data Warehouse

- **Amazon Redshift Cluster**:
  - Lưu trữ bảng đã qua xử lý (dim, fact) theo mô hình star/snowflake schema.
  - Hỗ trợ query phân tích khối lượng lớn với hiệu năng cao.

#### 5. Orchestration

- **Apache Airflow**:
  - Scheduler & Web UI: lên lịch (cron, interval), trigger manual, monitoring, retry, alert khi có lỗi.
  - DAGs (viết bằng Python): định nghĩa luồng công việc.
    - PythonOperator: chạy script ingestion.
    - GlueJobOperator: khởi job AWS Glue.
    - RedshiftOperator hoặc PostgresOperator: chạy SQL trên Redshift nếu cần.
  - Triển khai code lên Airflow bằng cách mount folder /dags từ S3 và requirements.txt để quản lý dependencies.

#### 6. Analyze

- **AWS Athena**: Cho phép query trực tiếp file dữ liệu trên S3 (clean zone) bằng SQL mà không cần load vào database.
- **Amazon QuickSight**: Kết nối đến Redshift (hoặc Athena) để dựng dashboard, chart, alert; cung cấp giao diện drag-and-drop cho business
– Gọi API, parse JSON, làm sạch sơ bộ (ví dụ: chuyển timezone, chuẩn hoá tên trường…)
– Xuất file (CSV/Parquet/JSON) và ghi lên Amazon S3.


