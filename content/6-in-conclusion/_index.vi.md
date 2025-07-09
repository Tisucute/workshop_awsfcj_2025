---
title : "Kết luận"
date :  "`r Sys.Date()`" 
weight : 6
chapter : false
pre : " <b> 6. </b> "
---

### **Lab: Xây dựng kiến trúc xử lý tự động và trực quan hóa dữ liệu thời gian thực trên AWS**

Chúng ta đã hoàn thành một hành trình “end-to-end” từ:

1. Viết **Python script** thu thập dữ liệu thời tiết từ OpenWeather API.  
2. Điều phối workflow với **Apache Airflow (MWAA)**, tận dụng XCom để truyền dữ liệu giữa các task.  
3. Triển khai toàn bộ hạ tầng bằng **AWS CloudFormation**: S3, IAM, VPC, MWAA, Glue, Redshift, Secrets Manager.  
4. Xử lý và chuyển đổi dữ liệu bằng **AWS Glue** (PySpark), nạp vào **Amazon Redshift** với tối ưu DIST/SORT keys.  
5. Phân tích dữ liệu lịch sử và realtime bằng **SQL** trên Redshift.  
6. Trực quan hóa và chia sẻ insight tức thì qua **Amazon QuickSight**.

#### Những gì bạn đã học được:
- **Thiết kế kiến trúc** ETL tự động, tối ưu cho dữ liệu thời gian thực.  
- **Áp dụng IaC** với CloudFormation để duy trì reproducibility và version control.  
- **Tích hợp dịch vụ AWS** linh hoạt: từ storage (S3), compute (Glue), data warehouse (Redshift) đến BI (QuickSight).  
- **Tối ưu performance & chi phí**: chọn node phù hợp, sử dụng materialized views, auto-pause, Reserved Instances.  
- **Xử lý lỗi và giám sát**: sensor, retry, alert trong Airflow; CloudWatch và Cost Explorer.

#### Hướng phát triển tương lai:
- **Mở rộng nguồn dữ liệu**: tích hợp IoT, logs, streams (Kinesis, Kafka).  
- **Machine Learning**: dùng SageMaker để dự báo thời tiết, anomaly detection.  
- **CI/CD cho hạ tầng**: tự động test & deploy DAGs, template CloudFormation.  
- **Lakehouse & Data Mesh**: kết hợp Athena, Glue Elastic Views, Redshift Serverless để giảm độ trễ và chi phí.  

**Cảm ơn mọi người** đã làm theo workshop “Xây dựng kiến trúc xử lý tự động và trực quan hóa dữ liệu thời gian thực trên AWS” của mình. Chúc các bạn thành công và tiếp tục khám phá những giải pháp dữ liệu mạnh mẽ trên AWS!  

<div style="text-align: center; margin-top: 30px;">
  <img
    src="/images/1.introduction/anhthu_aws.png"
    alt="AWS Cloud Novice"
    style="
      width: 400px;                   
      max-width: 100%;                
      border-radius: 12px;
      box-shadow: 0 6px 16px rgba(0,0,0,0.15);
      margin-bottom: 20px;
    "
  />
  <div style="
      display: inline-block;          
      background: rgb(241, 184, 184);
      padding: 15px 20px;
      border-left: 5px solid rgb(233, 137, 137);
      text-align: center;             
      border-radius: 4px;
    ">
    <strong style="font-size: 20px; color: rgb(222, 17, 17);">
      Em xin gửi lời cảm ơn chân thành nhất đến mọi người đã luôn đồng hành và hỗ trợ em  
      suốt 3 tháng “lên mây” đầy thử thách này! 🚀💻
    </strong>
  </div>
</div>


<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>
