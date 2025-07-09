---
title : "Các file môi trường"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 3.1 </b> "
---
Trong hệ thống ETL tự động trên AWS, các file môi trường là tập hợp mã nguồn Python và cấu hình được sử dụng bởi Apache Airflow (MWAA) để điều phối toàn bộ quy trình thu thập – xử lý – lưu trữ dữ liệu. Các file này được lưu trữ trong Amazon S3, và được phân chia rõ ràng theo vai trò: môi trường của Airflow và môi trường thực thi của Glue.

### Về môi trường của Airflow
#### 1. openweather_api.py – DAG thu thập dữ liệu
Đây là file đầu tiên cần được triển khai trong môi trường Airflow. File này định nghĩa một DAG tên là openweather_api_dag, có nhiệm vụ:

Gọi OpenWeather API để lấy dữ liệu thời tiết thời gian thực tại TP. Hồ Chí Minh.

Xử lý dữ liệu JSON trả về từ API thành định dạng bảng (dạng DataFrame của pandas).

Chuyển dữ liệu sang chuỗi CSV.

Upload file CSV này lên Amazon S3 (bucket vùng raw) để phục vụ bước ETL tiếp theo.

Điểm nổi bật:

Sử dụng requests để gọi API, pandas để xử lý dữ liệu.

API key được bảo mật bằng cách lấy từ Airflow Variable (Variable.get('key')).

Giao tiếp giữa các task trong DAG thông qua XCom.

Upload file bằng S3CreateObjectOperatoropenweather_api.

DAG này được thiết lập để chạy mỗi giờ, đảm bảo dữ liệu luôn được cập nhật liên tục.

#### 2. transform_redshift_load.py – DAG điều phối quá trình ETL
DAG này tên là transform_redshift_dag, dùng để:

Chờ DAG openweather_api_dag chạy thành công, thông qua ExternalTaskSensor.

Sau đó gọi AWS Glue Job để thực hiện bước ETL: chuyển đổi dữ liệu và nạp vào Redshift.

DAG sử dụng GlueJobOperator để gọi script ETL transform.py nằm ở ngoài môi trường Airflow (trong thư mục S3 dành riêng cho Glue)transform_redshift_load.

#### 3. requirements.txt 
Nếu cần cài thêm thư viện cho Airflow (như numpy, pandas, requests), file này sẽ liệt kê các package cần cài. Được upload lên S3 tại thư mục cấu hình requirements/ để MWAA đọc khi khởi tạo môi trường.

#### 4. transform.py – Script ETL chạy trong AWS Glue
File này không nằm trong môi trường Airflow, mà được AWS Glue sử dụng để xử lý dữ liệu bằng PySpark:

Đọc file CSV từ S3 (được tạo bởi DAG đầu tiên).

Chuyển đổi kiểu dữ liệu, chuẩn hóa timestamp (dt, dt_iso, ingest_time).

Ghi dữ liệu vào Redshift, đồng thời tạo bảng nếu chưa tồn tại (CREATE TABLE IF NOT EXISTS ...)transform.

File này được gọi trong DAG transform_redshift_dag thông qua script_location.