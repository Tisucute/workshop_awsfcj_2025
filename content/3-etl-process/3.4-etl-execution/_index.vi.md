---
title : "Quá trình thực hiện ETL"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 3.4 </b> "
---
Toàn bộ pipeline ETL đã được cấu hình để **chạy tự động** hàng giờ. Dưới đây là các bước chính khi bạn “go-live”:

#### Bước 1: Bật (unpause) các DAG trong Airflow  
1. Mở **Airflow UI** → **DAGs**.  
2. Tìm hai DAG `openweather_api_dag` và `transform_redshift_dag`.  
3. Chuyển toggle từ **Off** → **On** để kích hoạt tự động chạy theo `schedule_interval` (mỗi giờ).  
4. Xác nhận cột **Schedule** hiển thị “@hourly” và status “healthy”.

> **Lưu ý**: Bạn cũng có thể bật DAGs qua CLI:
> ```bash
> airflow dags unpause openweather_api_dag
> airflow dags unpause transform_redshift_dag
> ```

#### Bước 2: Theo dõi, đợi và kiểm tra (nếu lỗi)  
1. **Theo dõi lần chạy đầu**  
   - Vào tab **Graph** hoặc **Tree** view của `openweather_api_dag`.  
   - Quan sát Task `extract_api_data` → `upload_to_S3`.  
   - Chờ trạng thái từng task chuyển thành **success** (màu xanh lá).

2. **Kiểm tra dữ liệu thô trên S3**  
   - Vào S3 Console → bucket `raw-data`.  
   - Xác nhận file `raw/weather_api_data.csv` đã được viết mới (timestamp gần nhất).

3. **Chờ DAG ETL tiếp theo**  
   - Tương tự với `transform_redshift_dag`, quan sát task `wait_openweather_api` → `transform_task`.  
   - Khi thành công, Glue Job sẽ chạy và nạp dữ liệu vào Redshift.

4. **Kiểm tra dữ liệu trong Redshift**  
   - Vào **Query Editor** → chạy:
     ```sql
     SELECT COUNT(*) FROM public.weather_data;
     ```
   - Xác nhận kết quả (≥ 0) và dữ liệu mới nhất có `ingest_time` phù hợp.

5. **Xử lý lỗi (nếu có)**  
   - Nếu task bất kỳ fail, click vào task → **Logs** để xem chi tiết.  
   - Thông thường lỗi có thể do:
     - API key không hợp lệ (Task `extract_api_data`).  
     - Bucket S3 sai đường dẫn hoặc quyền truy cập.  
     - Glue Job script lỗi khi parse hoặc connect Redshift.  
     - IAM Role thiếu policy.  
   - Sửa code hoặc cấu hình, commit & sync lại DAGs/scripts, then **clear** task → **rerun**.

#### Riêng mình gặp phải lỗi

{{% notice note %}}
Có thể thêm **Giám sát dài hạn** nếu lấy dữ liệu lâu. Ex: Dùng **CloudWatch** & **Cost Explorer** để theo dõi logs và chi phí.
{{% /notice %}}

**Tóm lại**, chỉ cần bật DAGs, sau đó Airflow tự động chạy, theo dõi kết quả và can thiệp khi có lỗi để đảm bảo pipeline vận hành ổn định và dữ liệu luôn được cập nhật.  


<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>