---
title : "Các công cụ được sử dụng"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.1 </b> "
---
#### 1. OpenWeather API

**OpenWeather API** là dịch vụ cung cấp dữ liệu thời tiết thời gian thực thông qua các RESTful endpoint. Người dùng có thể truy xuất các thông tin như nhiệt độ, độ ẩm, áp suất, v.v. bằng cách gửi yêu cầu HTTP và nhận về dữ liệu ở định dạng JSON hoặc XML.

#### 2. Python Script
**Python** là ngôn ngữ lập trình phổ biến, mạnh mẽ trong xử lý dữ liệu. Trong hệ thống này, Python script được sử dụng để:

- Gọi API (ví dụ: OpenWeather API) để lấy dữ liệu.

- Phân tích cú pháp (parse) dữ liệu JSON trả về.

- Làm sạch, chuẩn hóa dữ liệu (chuyển đổi múi giờ, đổi tên trường, v.v.).

- Xuất dữ liệu ra các định dạng như CSV, Parquet, hoặc JSON.

- Đẩy dữ liệu lên Amazon S3 để lưu trữ.

#### 3. Amazon S3
**Amazon S3** là dịch vụ lưu trữ đối tượng (object storage) của AWS, cho phép lưu trữ và truy xuất dữ liệu với độ bền và khả năng mở rộng cao. Trong kiến trúc này, S3 được dùng để:

- Lưu trữ dữ liệu thô (raw data) do Python script tạo ra.

- Lưu trữ các file định nghĩa DAGs cho Airflow.

- Lưu trữ các file requirements.txt để quản lý dependencies cho Airflow.

#### 4. AWS Glue
**AWS Glue** là dịch vụ ETL (Extract, Transform, Load) serverless của AWS, hỗ trợ tự động hóa việc phát hiện schema, làm sạch, biến đổi và nạp dữ liệu. Các thành phần chính:

- **Glue Crawler**: Tự động quét dữ liệu trên S3, phát hiện schema và tạo metadata table trong Data Catalog.

- **Glue ETL Job**: Chạy mã Scala hoặc Python (Spark) để xử lý, biến đổi dữ liệu và xuất kết quả sang S3 hoặc Redshift.

#### 5. Amazon Redshift
**Amazon Redshift** là dịch vụ data warehouse trên nền tảng đám mây, tối ưu cho các truy vấn phân tích dữ liệu lớn (OLAP). Redshift hỗ trợ lưu trữ dữ liệu theo mô hình star/snowflake schema, cho phép thực hiện các truy vấn phức tạp với hiệu năng cao, phù hợp cho các bài toán BI, phân tích dữ liệu.

#### 6. Apache Airflow (MWAA)
**Apache Airflow** là nền tảng mã nguồn mở dùng để lập lịch, điều phối và giám sát các workflow (luồng công việc) phức tạp. Trên AWS, Airflow được cung cấp dưới dạng dịch vụ Managed Workflows for Apache Airflow (MWAA). Airflow sử dụng các DAGs (Directed Acyclic Graphs) để định nghĩa các bước xử lý dữ liệu, hỗ trợ tự động hóa, retry, alert, và tích hợp với nhiều dịch vụ AWS.

#### 7. Amazon QuickSight
**Amazon QuickSight** là dịch vụ BI (Business Intelligence) trên AWS, hỗ trợ kết nối đến nhiều nguồn dữ liệu như Redshift, S3,... QuickSight cho phép xây dựng dashboard, biểu đồ, báo cáo tương tác với giao diện kéo-thả, hỗ trợ phân tích và trực quan hóa dữ liệu cho người dùng doanh nghiệp.

#### 8. AWS CloudFormation, IAM, VPC, Secrets Manager
- **CloudFormation**: Dịch vụ quản lý hạ tầng dưới dạng mã (Infrastructure as Code), giúp tự động hóa việc triển khai và quản lý tài nguyên AWS.

- **IAM (Identity and Access Management)**: Quản lý quyền truy cập, xác thực và phân quyền cho người dùng/dịch vụ.

- **VPC (Virtual Private Cloud)**: Tạo mạng ảo riêng biệt trên AWS, kiểm soát truy cập và bảo mật cho các tài nguyên.

- **Secrets Manager**: Lưu trữ, quản lý và truy xuất thông tin nhạy cảm (API key, mật khẩu, v.v.) một cách an toàn.


<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>