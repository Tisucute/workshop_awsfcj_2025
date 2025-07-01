---
title : "Tập dữ liệu được sử dụng"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 3. </b> "
---
### Giới thiệu về tập dữ liệu lấy từ OpenWeather API

Tập dữ liệu thu thập từ OpenWeather API là một chuỗi thời gian (time-series) các bản ghi thời tiết, mỗi bản ghi tương ứng với một thời điểm quan sát tại một vị trí địa lý cụ thể. Bộ dữ liệu này rất phù hợp cho các bài toán phân tích biến động khí hậu, dự báo thời tiết, trực quan hóa dashboard hoặc xây dựng mô hình máy học.

**Các trường dữ liệu chính gồm:**

- **Thông tin chung:**
  - `dt`: Thời điểm quan sát (UNIX timestamp)
  - `timezone`: Độ lệch múi giờ so với UTC
  - `id`, `name`: Mã và tên thành phố

- **Vị trí địa lý:**
  - `coord.lat`, `coord.lon`: Vĩ độ, kinh độ

- **Thông số thời tiết chính (main):**
  - `temp`: Nhiệt độ trung bình
  - `feels_like`: Cảm giác nhiệt độ
  - `temp_min`, `temp_max`: Nhiệt độ cực tiểu/cực đại
  - `pressure`: Áp suất khí quyển
  - `humidity`: Độ ẩm

- **Thời tiết chi tiết (weather - mảng):**
  - `main`: Mô tả ngắn (ví dụ: "Clear", "Rain")
  - `description`: Mô tả chi tiết hơn
  - `icon`: Mã icon hiển thị

- **Gió:**
  - `wind.speed`: Tốc độ gió (m/s)
  - `wind.deg`: Hướng gió (độ)

- **Mây:**
  - `clouds.all`: Phần trăm che phủ mây

- **Tầm nhìn:**
  - `visibility`: Tầm nhìn (mét)

- **Lượng mưa/tuyết (nếu có):**
  - `rain.1h`, `rain.3h`: Lượng mưa trong 1h/3h
  - `snow.1h`, `snow.3h`: Lượng tuyết trong 1h/3h

- **Thời điểm mặt trời mọc/lặn:**
  - `sys.sunrise`, `sys.sunset`: Thời điểm mặt trời mọc/lặn (UNIX timestamp)

**Lưu ý:**  
Dữ liệu thường được thu thập định kỳ (ví dụ mỗi 15–60 phút), lưu dưới dạng JSON gốc hoặc chuyển thành bảng CSV với các