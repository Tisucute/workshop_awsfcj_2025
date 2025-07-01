---
title : "Giới thiệu"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---
<!-- Ảnh và Thông tin cá nhân -->
<div style="display: flex; gap: 60px; margin-top: 30px; align-items: flex-start;">
  <div style="text-align: center;">
    <img src="/images/1.introduction/Anh_Thu.jpg" alt="Introduction"
         style="width: 260px; border-radius: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.15); margin-bottom: 12px;" />
    <div  style="font-size: 15px; line-height: 1.6;">
    <strong>Nguyễn Ngọc Anh Thư – 22133059</strong><br/>
      Trường Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh
  </div>

  </div>

  <div style="flex: 1;">
  <!-- Tiêu đề nổi bật -->
  <div style="background: #f5f7fa; padding: 15px 20px; border-left: 5px solid #2f80ed; margin-bottom: 20px;">
    <strong style="font-size: 20px; color: #2f80ed;">
      Thiết kế và Triển khai Data Pipeline dữ liệu thời tiết trên AWS Cloud
    </strong>
  </div>
  <div style="text-align: justify; line-height: 1.8; font-size: 18px;">
    Trong kỷ nguyên dữ liệu, việc thu thập, xử lý và phân tích dữ liệu thời gian thực đóng vai trò then chốt trong việc ra quyết định. Đề tài 
    <strong>“Thiết kế và Triển khai Data Pipeline dữ liệu thời tiết trên nền tảng AWS Cloud”</strong> được thực hiện nhằm xây dựng một quy trình tự động, linh hoạt để:
    <ul style="margin-top: 10px;">
      <li>Thu thập dữ liệu thời tiết thực từ OpenWeather API bằng Python.</li>
      <li>Lưu trữ dữ liệu thô vào <strong>Amazon S3</strong> theo kiến trúc Data Lake.</li>
      <li>Xử lý và chuyển đổi dữ liệu tự động với <strong>AWS Glue</strong>.</li>
      <li>Nạp dữ liệu đã biến đổi vào <strong>Amazon Redshift</strong> để phục vụ phân tích OLAP.</li>
      <li>Truy vấn ad-hoc trên S3 với <strong>AWS Athena</strong> và trực quan hóa kết quả trên <strong>AWS QuickSight</strong>.</li>
      <li>Quản lý workflow bằng <strong>Apache Airflow</strong>, chạy các DAG thu thập – xử lý – nạp dữ liệu, với file cấu hình phụ thuộc (<code>requirements.txt</code>).</li>
    </ul>
    <strong>Mục tiêu của đề tài:</strong>
    <ul style="margin-top: 10px;">
      <li>Hiểu và vận dụng kiến trúc Data Lake & Data Warehouse trên AWS.</li>
      <li>Thực hành xây dựng ETL/ELT pipeline tự động, có khả năng mở rộng.</li>
      <li>Áp dụng công cụ phân tích và trực quan hóa dữ liệu thời gian thực.</li>
    </ul>
  </div>
</div>



  </div>
  
</div>

<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>