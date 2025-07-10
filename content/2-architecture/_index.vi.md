---
title : "Công cụ sử dụng và Kiến trúc"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2. </b> "
---
Hệ thống ETL thời tiết được xây dựng trên nền tảng AWS, kết hợp với các công cụ mã nguồn mở như Python và Apache Airflow. Dữ liệu thời tiết được lấy từ OpenWeather API, xử lý bởi script Python và điều phối bằng Airflow (MWAA). Dữ liệu thô được lưu tạm vào Amazon S3, sau đó được AWS Glue xử lý và chuẩn hóa trước khi nạp vào kho dữ liệu Amazon Redshift. Cuối cùng, Amazon QuickSight được dùng để trực quan hóa dữ liệu phục vụ phân tích. Toàn bộ hạ tầng được triển khai tự động qua CloudFormation và bảo mật bởi IAM, VPC, và Secrets Manager. Sơ đồ kiến trúc thể hiện rõ luồng dữ liệu và vai trò của từng thành phần trong hệ thống.

{{% notice note %}}
Được thực hiện trong vùng **United States(N.Virginia) - us-east-1**
{{% /notice %}}

![Region](/images/2.architecture/region.png)

#### Nội dung chính:

2.1 [Các công cụ sử dụng](2-architecture/2.1-tools/)

2.2 [Sơ đồ kiến trúc](2-architecture/2.2-architecture/)

<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>
