---
title : "Thiết lập biến, tạo kết nối và upload môi trường"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 3.3 </b> "
---
### 3.3 Thiết lập biến, tạo kết nối và upload môi trường

#### Bước 1: Tạo Variables trong Airflow  
1. Mở **Airflow UI** → **Admin** → **Variables** → **Create**.  
![Tạo biến](/images/3.etl-process/3.3.setup-variables-connection/tao_bien_airflow.png)
2. Tạo biến:  
   - **Key**: `key`  
     **Value**: `<YOUR_OPENWEATHER_API_KEY>`  
 
**Cách lấy API key**
  - Vào trang chủ của **OpenWeather API**:
![Trang chủ API](/images/3.etl-process/3.3.setup-variables-connection/trang_chu_api.png)
  - Chọn **(Tên của bạn)**, vào **My API Keys**, api key sẽ được mặc định hoặc bạn có thể generate mới:
![Lấy API](/images/3.etl-process/3.3.setup-variables-connection/lay_api_key.png)

{{% notice note %}}
Chắc chắn là API key của bạn đang ở chế độ hoạt động.
{{% /notice %}}

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


<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>