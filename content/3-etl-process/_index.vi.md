---
title : "Các bước thực hiện quá trình ETL tự động"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 3. </b> "
---
Trong kiến trúc thu thập và xử lý dữ liệu thời tiết sử dụng AWS, phần quan trọng nhất nằm ở quy trình ETL (Extract – Transform – Load) tự động. Đây là nơi toàn bộ dữ liệu được lấy về từ OpenWeather API, xử lý, lưu trữ và chuyển hóa thành thông tin có thể phân tích được.

### Luồng xử lý tổng thể gồm 4 bước chính:

#### 1. Chuẩn bị môi trường

- Viết script Python để gọi API và xử lý dữ liệu ban đầu.

- Đóng gói các file này vào S3 để Airflow (MWAA) có thể chạy tự động.

#### 2. Triển khai hạ tầng tự động

Sử dụng AWS CloudFormation để triển khai toàn bộ tài nguyên cần thiết như S3, MWAA, IAM, Glue, Redshift...

#### 3. Cấu hình Airflow

- Thiết lập biến (Variables) và kết nối (Connections) trong Airflow.

- Upload DAG và các tệp cần thiết lên đúng vị trí trong S3.

#### 4. Thực thi ETL

- Apache Airflow tự động kích hoạt pipeline theo lịch trình.

- Gọi API → lưu vào S3 → xử lý bằng Glue → lưu vào Redshift → trực quan hóa bằng QuickSight.

### Tại sao cần ETL tự động?

- **Tiết kiệm thời gian**: Không cần thủ công tải dữ liệu hằng ngày.

- **Chuẩn hóa dữ liệu**: Đảm bảo dữ liệu có định dạng sạch, đồng nhất, có thể phân tích.

- **Tích hợp dễ dàng**: Với các công cụ phân tích như Amazon Redshift & QuickSight.

- **Có thể mở rộng**: Dễ dàng áp dụng cho nhiều loại dữ liệu khác nhau, không chỉ thời tiết.

#### Nội dung chính:
3.1  [Về các file môi trường](3-etl-process/3.1-env-files/)

3.2  [Triển khai hạ tầng bằng mã nguồn](3-etl-process/3.2-infra-as-code/)

3.3  [Thiết lập biến, tạo kết nối và upload môi trường](3-etl-process/3.3-setup-variables-connection/)

3.4 [Quá trình thực hiện ETL](3-etl-process/3.4-etl-execution/)
