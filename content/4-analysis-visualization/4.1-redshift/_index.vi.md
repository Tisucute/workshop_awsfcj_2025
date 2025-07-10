---
title : "Phân tích với Amazon Redshift"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---
- Amazon Redshift là kho dữ liệu (data warehouse) OLAP, tối ưu cho truy vấn phân tích trên dữ liệu lớn.  

- Sử dụng mô hình phân phối (distribution key) và sắp xếp (sort key) để tối ưu I/O và hiệu năng.  

- Hỗ trợ SQL tiêu chuẩn, Materialized Views, và các công cụ ETL/BI tích hợp sẵn.

---

### Ví dụ truy vấn với bảng `public.weather_data`

**Nhiệt độ trung bình hàng ngày**  
   ```sql
   SELECT
     DATE(dt) AS date,
     ROUND(AVG(temp), 2) AS avg_temp
   FROM public.weather_data
   GROUP BY date
   ORDER BY date;
```

**Tóm lại**, với Amazon Redshift bạn có thể chạy các truy vấn phân tích dữ liệu thời gian thực, tận dụng tính năng phân phối, sắp xếp và vật liệu hóa để tối ưu chi phí và hiệu năng.

<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>