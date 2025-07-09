---
title : "Thiết lập biến, tạo kết nối và upload môi trường"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 3.3 </b> "
---
### 3.3 Thiết lập biến, tạo kết nối và upload môi trường

#### Bước 1: Tạo Variables trong Airflow  
1. Mở **Airflow UI** → **Admin → Variables** → **Create**.  
2. Tạo biến:  
   - **Key**: `key`  
     **Value**: `<YOUR_OPENWEATHER_API_KEY>`  
 
#### Bước 2: Tạo Connections trong Airflow  
1. Mở **Airflow UI** → **Admin → Connections** → **Create**.  
2. Tạo **AWS_CONN** (kết nối tới AWS):  
   - **Conn Id**: `AWS_CONN`  
   - **Conn Type**: `Amazon Web Services`  
   - **Login**: `<AWS_ACCESS_KEY_ID>`  
   - **Password**: `<AWS_SECRET_ACCESS_KEY>`  

**Chú ý cách lấy access key** 

> **Lưu ý**: Trong DAG `transform_redshift_load.py`, tham số  
> ```python
> aws_conn_id='AWS_CONN'
> create_job_kwargs={'Connections':{'Connections':['redshift-demo-connection']}}
> ```  

#### Bước 3: Tạo 2 S3 Buckets để chứa dữ liệu raw khi thu thập được và các nội dung trong Glue thực hiện 

#### Bước 4: Kết nối db để thực hiện đẩy dữ liệu vào trong Redshift
