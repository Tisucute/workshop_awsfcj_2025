---
title : "Dọn dẹp tài nguyên"
date :  "`r Sys.Date()`" 
weight : 5
chapter : false
pre : " <b> 5. </b> "
---
### Mục đích xóa
- **Dọn dẹp tài nguyên** không còn cần thiết, tránh nhầm lẫn và rối rắm trong quản lý.  
- **Ngăn ngừa chi phí phát sinh**: loại bỏ các dịch vụ đang chạy hoặc lưu trữ dữ liệu không dùng.  
- **Bảo mật**: giảm thiểu rủi ro lộ thông tin và bề mặt tấn công.
- **Tiết kiệm chi phí**: AWS tính phí theo thời gian sử dụng và dung lượng. Xóa kịp thời giúp giảm đáng kể hoá đơn.  
- **Quản lý gọn gàng**: Giúp môi trường AWS sạch sẽ, minh bạch, dễ theo dõi và bảo trì.
#### 5.1 Dừng và xóa DAGs trong Airflow
- Truy cập Airflow UI → trang **DAGs**  
- Chuyển hai DAG `openweather_api_dag` và `transform_redshift_dag` về trạng thái **Off**  
- Vào S3 Console → bucket chứa DAGs → xóa các file DAG tương ứng  

#### 5.2 Xóa CloudFormation Stack
- Truy cập AWS Console → dịch vụ **CloudFormation**  
- Chọn stack đã tạo (ví dụ `anhthu-etl-stack`)  
- Chọn **Delete stack** và xác nhận  
- Đợi trạng thái chuyển thành **DELETE_COMPLETE**  

#### 5.3 Xóa hai S3 Buckets
- Truy cập S3 Console → chọn bucket DAGs và bucket dữ liệu thô  
- Mở từng bucket, chọn **Empty bucket** để xóa toàn bộ nội dung  
- Sau khi trống, chọn **Delete bucket** và xác nhận  

#### 5.4 Kiểm tra lại
- Xác nhận không còn stack nào trong CloudFormation  
- Kiểm tra S3 Console đảm bảo hai bucket đã bị xóa  
- Vào Airflow UI đảm bảo không còn DAG hiển thị  
- Vào Redshift Console đảm bảo cluster do CF tạo (nếu có) đã bị xóa hoặc không còn  
- Check kĩ lại các security group để đảm bảo xóa không thiếu bất cứ dịch vụ nào.

<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>