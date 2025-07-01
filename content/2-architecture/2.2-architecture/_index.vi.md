---
title : "Xây dựng Sơ đồ Kiến trúc"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---
### Sơ đồ Kiến trúc

- **Pipeline trên AWS Cloud tự động thu thập dữ liệu từ OpenWeather API bằng Python và lưu vào S3, sau đó AWS Glue làm sạch và chuyển đổi dữ liệu trước khi nạp vào Redshift theo star-schema; Amazon Athena và QuickSight phục vụ phân tích ad-hoc và trực quan hóa, còn Apache Airflow điều phối toàn bộ quy trình với retry, logging và khả năng mở rộng linh hoạt.** 

Sơ đồ dưới đây minh họa tổng thể kiến trúc hệ thống trên AWS:
![So Do](/images/2.architecture/Kien_truc.png)