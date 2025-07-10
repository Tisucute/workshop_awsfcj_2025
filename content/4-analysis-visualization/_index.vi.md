---
title : "Phân tích và trực quan hóa"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 4. </b> "
---
#### 1. Giới thiệu về dữ liệu thu được  
Sau khi pipeline ETL chạy xong, bạn sẽ có bảng `public.weather_data` trong Redshift chứa các cột chính sau:

| Cột                 | Kiểu dữ liệu | Mô tả                                                 |
|---------------------|--------------|-------------------------------------------------------|
| `dt`                | timestamp    | Thời điểm ghi nhận (chuyển từ epoch)                  |
| `dt_iso`            | timestamp    | Thời điểm ghi nhận ở định dạng ISO                    |
| `temp`              | double       | Nhiệt độ trung bình (°C)                              |
| `feels_like`        | double       | Nhiệt độ cảm nhận (°C)                                |
| `pressure`          | integer      | Áp suất (hPa)                                         |
| `humidity`          | integer      | Độ ẩm (%)                                             |
| `wind_speed`        | double       | Tốc độ gió (m/s)                                      |
| `weather_main`      | varchar      | Tình trạng thời tiết chính (Clear, Clouds, Rain,…)    |
| `weather_description`| varchar     | Mô tả chi tiết hơn (few clouds, light rain,…)         |
| `city`              | varchar      | Tên thành phố                                         |
| `country`           | varchar      | Quốc gia                                              |
| `ingest_time`       | timestamp    | Thời điểm dữ liệu được ETL vào kho (UTC)              |

Dữ liệu được thu thập mỗi giờ, lưu trữ lịch sử liên tục, giúp phân tích xu hướng và biến động thời tiết theo thời gian.


#### 4.2 Phân tích trên Amazon Redshift  
- **Tính toán chỉ số trung bình & biến động**  
  - Ví dụ: trung bình nhiệt độ hàng ngày, biến động áp suất theo giờ.  
- **Phân loại & lọc theo điều kiện**  
  - Ví dụ: đếm số lần xảy ra “Rain” trong tuần, mức độ ẩm vượt ngưỡng.  
- **Xác định xu hướng & seasonality**  
  - Ví dụ: tăng/giảm nhiệt độ theo mùa, chu kỳ mưa.  
- **Kết hợp với dữ liệu kinh doanh**  
  - Ví dụ: so sánh lưu lượng khách tham quan ngoài trời với điều kiện thời tiết.

Redshift với khả năng xử lý OLAP cho phép bạn chạy các truy vấn tổng hợp, phân tích thời gian lớn một cách nhanh chóng và hiệu quả.


#### 4.3 Trực quan hóa với Amazon QuickSight  
- **Dashboard tương tác**  
  - Dễ dàng kéo thả để tạo biểu đồ line chart (nhiệt độ, độ ẩm), bar chart (số ngày mưa), gauge chart (áp suất trung bình).  
- **Filter & drill-down**  
  - Cho phép chọn khoảng thời gian, thành phố, điều kiện thời tiết để phân tích chi tiết.  
- **Alerts & insights tự động**  
  - Sử dụng tính năng “Anomaly Detection” và “Notifications” để cảnh báo khi nhiệt độ/độ ẩm bất thường.  
- **Chia sẻ & nhúng**  
  - Xuất report, chia sẻ link với đồng nghiệp hoặc nhúng dashboard vào ứng dụng nội bộ.

Kết hợp Redshift và QuickSight, bạn có thể triển khai một giải pháp “end-to-end” từ thu thập dữ liệu, phân tích chuyên sâu đến trực quan hóa linh hoạt, hỗ trợ ra quyết định nhanh chóng dựa trên dữ liệu thời tiết.  

### Nội dung chính:
4.1 [Phân tích với AWS Redshift](4-analysis-visualization/4.1-redshift/)

4.2 [Trực quan hóa với AWS Quicksight](4-analysis-visualization/4.2-quicksight/)

<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>