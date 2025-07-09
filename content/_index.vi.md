---
title : "Xây dựng kiến trúc xử lý tự động và trực quan hóa dữ liệu thời gian thực trên AWS"
date: 2025-06-18 
weight : 1 
chapter : false
---
# Xây dựng kiến trúc xử lý tự động và trực quan hóa dữ liệu thời gian thực trên AWS

**Họ tên:** Nguyễn Ngọc Anh Thư  
**MSSV:** 22133059  
**Email:** ngocanhthugialai@gmail.com  
**Trường:** Đại học Sư phạm Kỹ thuật TP.HCM (HCMUTE)

### Tổng quan

Đề tài **"Xây dựng kiến trúc xử lý tự động và trực quan hóa dữ liệu thời gian thực trên AWS"** là sự tâm huyết và nỗ lực nhằm xây dựng một hệ thống toàn diện, tự động hóa việc thu thập, xử lý và hiển thị trực quan các luồng dữ liệu thời gian thực dựa trên nền tảng Amazon Web Services (AWS). Với mục tiêu đáp ứng nhu cầu phân tích và ra quyết định nhanh chóng, hiệu quả dựa trên dữ liệu mới nhất, hệ thống được thiết kế bao gồm các thành phần chính: thu thập dữ liệu thời tiết từ API của OpenWeather bằng Python và lưu trữ vào AWS S3; orchestration thông qua Amazon Managed Workflows for Apache Airflow (MWAA); xử lý và chuyển đổi dữ liệu bằng AWS Glue; lưu trữ dữ liệu vào kho dữ liệu AWS Redshift; và cuối cùng trực quan hóa kết quả bằng AWS QuickSight trên dashboard trực quan.

Việc triển khai hạ tầng được thực hiện thông qua mã nguồn (Infrastructure as Code - IaC) sử dụng AWS CloudFormation, đảm bảo tính nhất quán, tự động hóa và dễ dàng quản lý, mở rộng khi có nhu cầu thay đổi hoặc bổ sung tài nguyên. Các chính sách bảo mật và quản lý truy cập cũng được thiết lập thông qua AWS IAM và môi trường bảo mật mạng riêng ảo (VPC) nhằm đảm bảo an toàn cho hệ thống.

Em rất hy vọng báo cáo này không chỉ phản ánh chân thực quá trình thực hiện của em, mà còn là một tài liệu thân thiện, dễ hiểu, đồng hành cùng các bạn sinh viên mới tiếp cận AWS hoặc các mô hình phát triển hiện đại. Mong rằng, qua đây em có thể truyền tải được sự nhiệt huyết, niềm đam mê với công nghệ và hỗ trợ các bạn tự tin hơn trên hành trình khám phá và ứng dụng AWS.

### Thời gian thực hiện

- **Lấy dữ liệu:** 1 ngày 
{{% notice warning %}}
Dữ liệu chỉ đủ để phân tích, nếu nhiều hơn có thể phát sinh thêm nhiều chi phí
{{% /notice %}}
- **Thực hiện các thao tác:** 2 - 3 tiếng (tùy vào độ quen thuộc với các công cụ)

### Nội dung

1. [Giới thiệu](1-introduce/)
2. [Các công cụ sử dụng và Sơ đồ kiến trúc](2-architecture/)
   - [Các công cụ sử dụng](2-architecture/2.1-tools/)
   - [Sơ đồ kiến trúc](2-architecture/2.2-architecture/)
3. [Các bước thực hiện quá trình ETL tự động](3-etl-process/)
   - [Về các file môi trường](3-etl-process/3.1-env-files/)
   - [Triển khai hạ tầng bằng mã nguồn](3-etl-process/3.2-infra-as-code/)
   - [Thiết lập biến, tạo kết nối và upload môi trường](3-etl-process/3.3-setup-variables-connection/)
   - [Quá trình thực hiện ETL](3-etl-process/3.4-etl-execution/)
4. [Phân tích và trực quan hóa](4-analysis-visualization/)
   - [Phân tích với AWS Redshift](4-analysis-visualization/4.1-redshift/)
   - [Trực quan hóa với AWS Quicksight](4-analysis-visualization/4.2-quicksight/)
5. [Dọn dẹp tài nguyên](5-cleanup/)
6. [Kết luận](6-in-conclusion/)