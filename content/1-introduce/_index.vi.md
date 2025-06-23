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
      <strong style="font-size: 20px; color: #2f80ed;">Thiết kế và Triển khai Data Pipeline trên nền tảng AWS Cloud</strong>
    <div style="text-align: justify; line-height: 1.8; font-size: 18px;">
Trong thời đại dữ liệu hiện nay, việc xử lý, lưu trữ và khai thác dữ liệu một cách hiệu quả đóng vai trò then chốt trong hoạt động vận hành và ra quyết định của doanh nghiệp. Đề tài <strong>“Thiết kế và Triển khai Data Pipeline trên nền tảng AWS Cloud ”</strong> được thực hiện nhằm xây dựng một quy trình hiện đại và linh hoạt để thu thập, xử lý, lưu trữ và phân tích dữ liệu từ nhiều nguồn khác nhau.

Dự án tận dụng sức mạnh của nền tảng <strong>Amazon Web Services (AWS)</strong> – dịch vụ điện toán đám mây hàng đầu thế giới – kết hợp với <strong>Snowflake</strong>, một hệ quản trị dữ liệu dạng Data Warehouse hiện đại, hỗ trợ mở rộng theo chiều ngang, tách biệt tài nguyên compute và storage.

Cụ thể, hệ thống Data Pipeline được triển khai sẽ bao gồm:
<ul style="margin-top: 10px;">
  <li>Thu thập dữ liệu thô từ nguồn đầu vào như file <code>.csv</code>, API hoặc luồng streaming.</li>
  <li>Lưu trữ tạm thời trên <strong>Amazon S3</strong> theo kiến trúc Data Lake.</li>
  <li>Tích hợp xử lý tự động thông qua <strong>AWS Lambda</strong>, <strong>Glue</strong> hoặc <strong>Airflow</strong>.</li>
  <li>Nạp dữ liệu vào <strong>Snowflake</strong> theo mô hình star schema (bảng <code>dim</code> và <code>fact</code>).</li>
  <li>Kết nối với Power BI/Superset để trực quan hóa và phân tích.</li>
</ul>

Thông qua đề tài này, người thực hiện hướng đến mục tiêu:
<ul style="margin-top: 10px;">
  <li>Nắm bắt kiến trúc hiện đại trong triển khai hệ thống xử lý dữ liệu phân tán.</li>
  <li>Vận dụng kỹ năng cloud computing trên nền tảng AWS.</li>
  <li>Áp dụng mô hình dữ liệu và kỹ thuật ELT/ETL trong môi trường thực tế.</li>
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