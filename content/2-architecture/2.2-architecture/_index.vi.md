---
title : "Xây dựng Sơ đồ Kiến trúc"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---
### Sơ đồ Kiến trúc

- **Kiến trúc này mô tả một quy trình thu thập, xử lý, lưu trữ, phân tích và trực quan hóa dữ liệu thời tiết thông qua các dịch vụ AWS và công cụ mã nguồn mở. Ban đầu, người dùng gửi yêu cầu thông tin thời tiết. Một Python script được đóng gói và lưu trữ vào môi trường Amazon S3, để Apache Airflow (MWAA) tự động gọi thực thi theo lịch định sẵn. Python script này sử dụng thư viện PySpark (Spark được tích hợp sẵn trong script Python) để gọi API của OpenWeather, lấy dữ liệu thời tiết theo thời gian thực, xử lý sơ bộ và lưu vào bucket Amazon S3 dưới dạng dữ liệu thô. Tiếp theo, AWS Glue Job tiến hành các bước ETL nâng cao, làm sạch, chuẩn hóa dữ liệu và nạp vào Amazon Redshift, sẵn sàng cho việc phân tích chuyên sâu. Sau đó, Amazon QuickSight kết nối với Redshift để tạo ra dashboard tương tác, trực quan hóa dữ liệu giúp người dùng dễ dàng phân tích và ra quyết định.**

- **Toàn bộ hạ tầng và các dịch vụ này được quản lý và triển khai tự động bằng AWS CloudFormation, đồng thời được bảo mật chặt chẽ bởi AWS IAM, VPC và Secrets Manager, giúp kiểm soát truy cập và lưu trữ an toàn các thông tin nhạy cảm trong hệ thống.** 

Sơ đồ dưới đây minh họa tổng thể kiến trúc hệ thống trên AWS:
![So Do](/images/2.architecture/Kien_truc.png)