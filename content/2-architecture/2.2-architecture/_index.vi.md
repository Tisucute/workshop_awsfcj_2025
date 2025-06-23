---
title : "Xây dựng Sơ đồ Kiến trúc"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---
### Sơ đồ Kiến trúc

Để xây dựng một hệ thống Data Pipeline hiện đại, tự động hóa và dễ mở rộng cho tập dữ liệu Olist trên AWS, việc thiết kế kiến trúc tổng thể là bước quan trọng nhằm đảm bảo dữ liệu được thu thập, xử lý, lưu trữ và phân tích một cách hiệu quả, bảo mật và tối ưu chi phí.

Kiến trúc này sử dụng hoàn toàn các dịch vụ AWS như Amazon S3, AWS Glue, AWS Lambda, AWS Step Functions, Amazon Redshift, Amazon QuickSight cùng các dịch vụ hỗ trợ như IAM, CloudWatch, CloudTrail, SNS, KMS, DataBrew và Athena. Mỗi dịch vụ đảm nhận một vai trò riêng biệt trong pipeline, từ lưu trữ, xử lý, tự động hóa, bảo mật đến trực quan hóa dữ liệu. Dữ liệu Olist được ingest vào S3, xử lý và chuyển đổi qua Glue, tự động hóa bằng Lambda và Step Functions, lưu trữ phân tích trên Redshift và trực quan hóa qua QuickSight. Các dịch vụ giám sát, bảo mật và thông báo giúp hệ thống vận hành ổn định, an toàn.

Sơ đồ dưới đây minh họa tổng thể kiến trúc hệ thống trên AWS:
![So Do](/images/2.architecture/So_Do.png)