---
title : "Triển khai hạ tầng bằng mã nguồn"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---
Phần này mô tả chi tiết cách sử dụng AWS CloudFormation để tự động khởi tạo và quản lý toàn bộ hạ tầng cần thiết cho pipeline ETL.

### 1. Giới thiệu template
- File: **template-workshop-anhthu.yaml**

- Mục đích: Định nghĩa toàn bộ tài nguyên AWS dưới dạng code, bao gồm:

- S3 Buckets:

    - Buckets để lưu DAGs & requirements cho MWAA.

    - Buckets để lưu dữ liệu thô (raw data).

- IAM Roles & Policies:

    - Role cho MWAA (đọc DAG, ghi S3, submit Glue).

    - Role cho Glue (đọc S3, ghi Redshift).

- VPC & Networking:

    - VPC, Subnets, Security Groups cho MWAA, Glue và Redshift.

- MWAA Environment: tham chiếu tới S3, IAM Role, network.

- AWS Glue Resources: Connection đến Redshift, (tùy chọn) Crawler, Job definition.

- Amazon Redshift Cluster: cấu hình node type, node count, database, parameter group.

- Secrets Manager: lưu trữ OpenWeather API key và credentials Redshift.

- Outputs: Endpoint của Redshift, tên buckets, ARN của Roles.

Mẫu template này áp dụng chuẩn YAML cho CloudFormation, giúp versioning, review và reuse dễ dàng.

### 2. Những chỗ cần chú ý khi **tái sử dụng code**
Trước khi deploy, bạn cần kiểm tra và thay thế các giá trị sau trong phần **Parameters** hoặc trực tiếp trong template:

- Các tên của các thành phần dịch vụ và các địa chỉ IP, API keys, ARN url, đường dẫn tới các dịch vụ sử dụng, các loại  phù hợp.

{{% notice warning %}}
Chọn đúng lớp node (node class) và số lượng node, vùng có giá phù hợp khối lượng dữ liệu.
{{% /notice %}}


### 3. Các bước triển khai (Deployment)

#### Bước 1: Tạo CloudFormation Stack
1. Đăng nhập AWS Console → chọn **CloudFormation**.  
2. Chọn **Create stack** → **With new resources (standard)**.  
3. Chọn **Upload a template file**, tải lên `template-workshop-anhthu.yaml`.  
4. Nhấn **Next**.
5. Nhấn **Next** qua phần **Options** (tuỳ chọn thêm Tags).  
6. Chọn “I acknowledge that AWS CloudFormation might create IAM resources”.  
7. Nhấn **Create stack** và theo dõi tab **Events** đến khi trạng thái là **CREATE_COMPLETE**.

#### Bước 2: Kiểm tra tài nguyên đã tạo
- **S3**  
- **IAM**  
  - Kiểm tra hai IAM Role (MWAA, Glue) với đúng policy.  
- **VPC & Security Groups**  
  - Trong VPC console, xác nhận Subnets và Security Groups cho phép:
    - MWAA truy xuất S3  
    - Glue truy xuất S3 & Redshift  
    - Redshift cho phép kết nối port 5439  
- **MWAA Environment**  
  - Console MWAA hiển thị environment mới, status **Available**. 
- **AWS Glue**  
  - Xác nhận Connection `redshift-demo-connection`.  
- **Redshift**  
  - Console Redshift hiển thị cluster *available*.  

{{% notice note %}}
Tạo bao nhiêu check bấy nhiêu để lúc làm **không bị thiếu môi trường hay kết nối** (nếu có phải xóa đi tạo stack lại) và có thể note lại để lúc xóa đảm bảo **không xóa thiếu** dịch vụ **tránh tăng các khoản phí** không đáng nói.
{{% /notice %}}

#### Bước 3: Kết nối và kiểm thử Redshift
