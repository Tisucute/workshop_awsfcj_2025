---
title : "Các công cụ được sử dụng"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.1 </b> "
---
### Các công cụ được sử dụng

Trong quá trình xây dựng Data Pipeline cho tập dữ liệu Olist trên AWS, các công cụ và dịch vụ sau được sử dụng:

- **Amazon S3**: Dịch vụ lưu trữ đối tượng, dùng để lưu trữ dữ liệu gốc (raw data) và dữ liệu đã xử lý (processed data).
- **AWS Glue**: Dịch vụ ETL serverless, hỗ trợ crawl schema, chuyển đổi và xử lý dữ liệu tự động.
- **AWS Lambda**: Chạy các đoạn mã nhỏ để tự động hóa các tác vụ như kích hoạt Glue jobs khi có dữ liệu mới.
- **AWS Step Functions**: Điều phối (orchestrate) các bước trong pipeline, đảm bảo các tác vụ diễn ra theo đúng trình tự.
- **Amazon Redshift**: Kho dữ liệu phân tích (data warehouse), lưu trữ dữ liệu đã xử lý để phục vụ truy vấn và phân tích.
- **Amazon QuickSight**: Công cụ trực quan hóa dữ liệu, xây dựng dashboard và báo cáo phân tích.
- **AWS IAM**: Quản lý quyền truy cập và bảo mật cho các dịch vụ và dữ liệu trên AWS.
- **Amazon CloudWatch**: Giám sát, thu thập log và cảnh báo cho các dịch vụ AWS, giúp theo dõi pipeline và xử lý sự cố.
- **AWS CloudTrail**: Theo dõi, ghi lại các hoạt động API trên tài khoản AWS để đảm bảo tính minh bạch và bảo mật.
- **AWS SNS (Simple Notification Service)**: Gửi thông báo tự động khi pipeline hoàn thành hoặc gặp lỗi.
- **AWS KMS (Key Management Service)**: Quản lý và mã hóa dữ liệu, đảm bảo an toàn thông tin trong quá trình lưu trữ và truyền tải.
- **AWS DataBrew**: Hỗ trợ làm sạch, chuẩn hóa dữ liệu mà không cần viết code, giúp tăng tốc quá trình chuẩn bị dữ liệu.
- **AWS Athena**: Truy vấn dữ liệu trực tiếp trên S3 bằng SQL, hỗ trợ kiểm tra nhanh dữ liệu trước khi nạp vào Redshift.

Các công cụ này kết hợp với nhau tạo thành một hệ thống xử lý dữ liệu hiện đại, tự động hóa, bảo mật và dễ dàng mở rộng cho các nhu cầu phân tích dữ liệu

