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
    <div style="font-size: 15px; line-height: 1.6;">
      <strong>Nguyễn Ngọc Anh Thư – 22133059</strong><br/>
      Trường Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh
    </div>
  </div>

  <div style="flex: 1;">
    <!-- Tiêu đề nổi bật -->
    <div style="background: #f5f7fa; padding: 15px 20px; border-left: 5px solid #2f80ed; margin-bottom: 20px;">
      <strong style="font-size: 20px; color: #2f80ed;">
        Xây dựng kiến trúc xử lý tự động và trực quan hóa dữ liệu thời gian thực trên AWS
      </strong>
    </div>
    <div style="text-align: justify; line-height: 1.8; font-size: 18px;">
      Báo cáo này trình bày quá trình xây dựng một hệ thống xử lý và trực quan hóa dữ liệu thời gian thực trên AWS, bao gồm các nội dung chính sau:
      <ul>
        <li><b>Giới thiệu:</b> Sơ lược về các nội dung liên quan tới đề tài.</li>
        <li><b>Các công cụ sử dụng & Sơ đồ kiến trúc:</b> Trình bày các dịch vụ AWS, công cụ hỗ trợ và sơ đồ tổng thể của hệ thống.</li>
        <li><b>Các bước thực hiện quá trình ETL tự động:</b> Hướng dẫn chi tiết từng bước từ chuẩn bị môi trường, triển khai hạ tầng, thiết lập kết nối đến thực thi ETL.</li>
        <li><b>Phân tích & trực quan hóa:</b> Mô tả cách phân tích dữ liệu với AWS Redshift và xây dựng dashboard trực quan với AWS QuickSight.</li>
        <li><b>Dọn dẹp tài nguyên:</b> Hướng dẫn xóa các tài nguyên AWS sau khi hoàn thành để tối ưu chi phí.</li>
      </ul>
    </div>
    <br>
    <div style="font-size: 17px;"><strong>Thời gian thực hiện</strong></div>
    <ul style="font-size: 16px;">
      <li><strong>Lấy dữ liệu:</strong> 1 ngày</li>
      <li><strong>Thực hiện các thao tác:</strong> 2 - 3 tiếng (tùy vào độ quen thuộc với các công cụ)</li>
    </ul>
    <div style="margin-bottom: 10px;">
      <div style="background:rgb(249, 176, 175); color:rgb(177, 35, 35); border-left: 5px solid;color: rgb(192, 12, 12); padding: 10px 16px; border-radius: 6px;">
        <strong>Chú ý:</strong> Dữ liệu chỉ đủ để phân tích, nếu nhiều hơn có thể phát sinh thêm nhiều chi phí.
      </div>
    </div>
    <div style="font-size: 17px;"><strong>Điều kiện tiên quyết</strong></div>
    <ul style="font-size: 16px;">
      <li>Có tài khoản AWS và quyền truy cập các dịch vụ cần thiết (S3, IAM, Glue, Redshift, MWAA, QuickSight,...).</li>
      <li>Đã cài đặt Python và các thư viện liên quan (requests, boto3,...).</li>
      <li>Máy tính kết nối internet ổn định.</li>
      <li>Kiến thức cơ bản về AWS và dòng lệnh.</li>
    </ul>
    <div style="font-size: 17px;"><strong>Khoản phí ước tính</strong>:Trong khoảng từ <strong>20$</strong> tới <strong>30$</strong></div>
  
</div>

<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>