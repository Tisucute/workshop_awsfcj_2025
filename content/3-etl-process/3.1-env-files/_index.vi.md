---
title : "Các file môi trường"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 3.1 </b> "
---
Trong hệ thống ETL tự động trên AWS, các file môi trường là tập hợp mã nguồn Python và cấu hình được sử dụng bởi Apache Airflow (MWAA) để điều phối toàn bộ quy trình thu thập – xử lý – lưu trữ dữ liệu. Các file này được lưu trữ trong Amazon S3, và được phân chia rõ ràng theo vai trò: môi trường của Airflow và môi trường thực thi của AWS Glue.

### **Về môi trường của Airflow**
#### 1. openweather_api.py – DAG thu thập dữ liệu thời tiết
Đây là file đầu tiên cần được triển khai trong môi trường Airflow. File này định nghĩa một DAG tên là openweather_api_dag, có nhiệm vụ:

- Gọi OpenWeather API để lấy dữ liệu thời tiết thời gian thực tại TP. Hồ Chí Minh.

- Xử lý dữ liệu JSON trả về từ API thành định dạng bảng (dạng DataFrame của pandas).

- Chuyển dữ liệu sang chuỗi CSV.

- Upload file CSV này lên Amazon S3 (bucket vùng raw) để phục vụ bước ETL tiếp theo.

**Luồng xử lý gồm 2 task chính:**

1. extract_api_data: gọi API → chuẩn hóa JSON → build DataFrame → chuyển thành CSV string.

2. upload_to_S3: lấy dữ liệu CSV từ XCom → upload lên bucket/raw/weather_api_data.csv.

DAG này chạy **mỗi giờ**, đảm bảo dữ liệu **luôn cập nhật**.

#### 2. transform_redshift_load.py – DAG điều phối quá trình ETL
DAG này tên là transform_redshift_dag, dùng để:

- Chờ DAG openweather_api_dag chạy thành công, thông qua ExternalTaskSensor.

- Sau đó gọi AWS Glue Job để thực hiện bước ETL: chuyển đổi dữ liệu và nạp vào Redshift.

- DAG sử dụng GlueJobOperator để gọi script ETL transform.py nằm ở ngoài môi trường Airflow (trong thư mục S3 dành riêng cho Glue)transform_redshift_load.

**Cấu trúc gồm 2 task:**

1. wait_openweather_api: đợi DAG trước hoàn tất.

2. transform_task: gọi GlueJobOperator, trỏ đến script ETL trong S3 (transform.py).

#### 3. requirements.txt 
Nếu cần cài thêm thư viện cho Airflow (như numpy, pandas, requests), file này sẽ liệt kê các package cần cài. Được upload lên S3 tại thư mục cấu hình requirements/ để MWAA đọc khi khởi tạo môi trường và chạy đúng các task.
<div class="chroma">
  <pre><code class="language-python">numpy==1.24.3
pandas==1.3.5
requests==2.31.0</code></pre>
</div>

### **Về môi trường thực thi của AWS Glue:** transform.py – Script ETL chạy trong AWS Glue
- File này **không** nằm trong môi trường Airflow, mà được AWS Glue sử dụng để xử lý dữ liệu bằng PySpark.

- Script xử lý dữ liệu bằng PySpark (Spark trong Python).

- Thực hiện các thao tác như: làm sạch dữ liệu, đổi tên trường, chuyển đổi kiểu dữ liệu, kiểm tra null, v.v.

- Kết quả được nạp trực tiếp vào Amazon Redshift thông qua kết nối JDBC.

**Điểm quan trọng:** script này chạy với Spark bên trong Glue nhưng được viết bằng Python (PySpark), dễ tích hợp và chỉnh sửa.

### **Tóm lại**
Các file môi trường đóng vai trò là **bộ não** điều phối toàn bộ pipeline. Chúng gồm:

- Các DAG định nghĩa luồng công việc (gọi API, ETL, load).

- Các script xử lý dữ liệu bằng PySpark.

- Các file cấu hình phụ trợ như requirements.txt.

Việc chuẩn bị chính xác các file này giúp MWAA hoạt động **mượt mà**, đảm bảo **tính tự động**, **chính xác** và **có thể mở rộng** cho hệ thống ETL thời tiết.