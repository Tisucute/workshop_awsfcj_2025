---
title : "Triển khai hạ tầng bằng mã nguồn"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---
Phần này mô tả chi tiết cách sử dụng AWS CloudFormation để tự động khởi tạo và quản lý toàn bộ hạ tầng cần thiết cho pipeline ETL.

### 1. Giới thiệu template
File: **template-workshop-anhthu.yaml**

Mục đích: Định nghĩa toàn bộ tài nguyên AWS dưới dạng code, bao gồm:

**1.1 MWAA Environment (Airflow)**

  - S3 bucket để lưu DAGs, code (AirflowEnvironmentBucket).

  - MWAA Environment (MwaaEnvironment).

  - IAM Role cho MWAA (MwaaExecutionRole).

  - Các subnet, VPC, security group, NAT gateway, route table, v.v.

**1.2 Redshift Cluster**

  - Redshift Cluster (RedshiftCluster).

  - Redshift Subnet Group, Parameter Group.

  - IAM Role cho Redshift (RedshiftIamRole).

  - Secrets Manager để lưu thông tin đăng nhập Redshift (RedshiftCreds).

  - S3 bucket tạm cho Redshift (RedshiftTempDataBucket).

**1.3 Glue Connection**

  - Kết nối Glue tới Redshift (GlueRedshiftConnection).

  - Không tạo Glue Job.

**1.4 Các thành phần mạng và bảo mật**

- VPC, subnet, security group, route table, NAT gateway, VPC endpoint cho S3


Mẫu template này áp dụng chuẩn YAML cho CloudFormation, giúp versioning, review và reuse dễ dàng.

### 2. Những chỗ cần chú ý khi **tái sử dụng code**
Trước khi deploy, bạn cần kiểm tra và thay thế các giá trị sau trong phần **Parameters** hoặc trực tiếp trong template:

- Các tên của các thành phần dịch vụ và các địa chỉ IP, API keys, ARN url, đường dẫn tới các dịch vụ sử dụng, các loại  phù hợp.

{{% notice warning %}}
Chọn đúng lớp node (node class) và số lượng node, vùng có giá phù hợp khối lượng dữ liệu.
{{% /notice %}}

**Ví dụ như:**
![Region](/images/3.etl-process/3.2.infra-as-code/chu_y_tai_su_dung.png)
### 3. Các bước triển khai (Deployment)

#### Bước 1: Tạo CloudFormation Stack
1. Đăng nhập AWS Console → chọn **CloudFormation**.  
    - Chọn **Create stack** 
![Tạo Stack](/images/3.etl-process/3.2.infra-as-code/tao_stack.png)
    - Chọn **Choose an existing template**.
    - Chọn **Upload a template file**, tải lên `template-workshop-anhthu.yaml`.  
![Step1](/images/3.etl-process/3.2.infra-as-code/step_1_stack.png)
2. Nhấn **Next**.
    - Điền tên của stack **data-workshop-anhthu**.
![Step2](/images/3.etl-process/3.2.infra-as-code/step_2_stack.png)
3. Nhấn **Next**.
    - Chọn **I acknowledge that AWS CloudFormation might create IAM resources**.  
![Step3](/images/3.etl-process/3.2.infra-as-code/step_3_stack.png)
4. Nhấn **Next**.
    - Kiểm tra lại kĩ các nội dung và chọn **Submit**.
![Step4](/images/3.etl-process/3.2.infra-as-code/submit.png)
5. Nhấn **Next** qua phần **Options** (tuỳ chọn thêm Tags).  
6. 
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


<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>