---
title : "Trực quan hóa với Amazon QuickSight"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---

- Amazon QuickSight là dịch vụ BI đám mây, cho phép tạo dashboard tương tác từ nhiều nguồn dữ liệu.  

- Sử dụng SPICE (Super-fast, Parallel, In-memory Calculation Engine) để đẩy nhanh tốc độ truy vấn và rendering.  

- Cung cấp các loại biểu đồ đa dạng (line, bar, pie, heatmap, KPI plates…), filter và drill-down.

---

### Kết nối Redshift → QuickSight

1. **Tạo Data source**  
   - Đăng nhập QuickSight → chọn **Manage data → New data set**.  
   - Chọn **Redshift**, nhập:
     - **Data source name**  
     - **Cluster**: chọn cluster Redshift (hoặc nhập endpoint/manual).  
     - **Database**: tên database.  
     - **Authentication**: sử dụng IAM role hoặc user/password (có lưu trong Secrets Manager).  
   - Test connection → Save.

2. **Tạo Data set**  
   - Chọn schema → table `public.weather_data`.  
   - Chọn **Import to SPICE for quicker analytics** hoặc **Direct query** tuỳ nhu cầu.  
   - (Tùy chọn) Thêm filter, custom SQL nếu cần.

---

### Tạo Analysis và trực quan

1. **Khởi tạo Analysis**  
   - Trong QuickSight → **Analyses → New analysis** → chọn data set vừa tạo.

2. **Tạo Visuals**  

{{% notice warning%}}
Quản lý dung lượng **SPICE** và **filter**, giảm dataset nếu cần
{{% /notice %}}

3. **Xuất Dashboard**  
   - Chọn **Share → Publish dashboard**.  
   - Đặt tên, phân quyền xem (user, group).  
   - Gửi link hoặc embed vào ứng dụng nội bộ.

---

Với QuickSight, chỉ mất vài thao tác để biến bảng `weather_data` trong Redshift thành các biểu đồ tương tác, hỗ trợ phân tích trực quan và ra quyết định nhanh chóng.  


<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>