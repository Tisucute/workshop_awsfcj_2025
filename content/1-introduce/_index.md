---
title : "Introduce"
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
      HCMC University of Technology and Education (HCMUTE)
    </div>
  </div>

  <div style="flex: 1;">
    <!-- Tiêu đề nổi bật -->
    <div style="background: #f5f7fa; padding: 15px 20px; border-left: 5px solid #2f80ed; margin-bottom: 20px;">
      <strong style="font-size: 20px; color: #2f80ed;">
        Building an Automated Real-Time Data Processing and Visualization Architecture on AWS
      </strong>
    </div>
    <div style="text-align: justify; line-height: 1.8; font-size: 18px;">
      This report presents the process of building a real-time data processing and visualization system on AWS, including the following main contents:
      <ul>
        <li><b>Introduction:</b> Brief overview of contents related to the topic.</li>
        <li><b>Tools & Architectural Diagram:</b> Description of AWS services, supporting tools, and the overall system architecture diagram.</li>
        <li><b>Steps to Implement the Automatic ETL Process:</b> Detailed guidance step-by-step, from preparing the environment, deploying infrastructure, creating connections, to performing ETL.</li>
        <li><b>Analysis & Visualization:</b> Explanation of data analysis with AWS Redshift and dashboard creation with AWS QuickSight.</li>
        <li><b>Cleaning Up Resources:</b> Instructions for deleting AWS resources after completion to optimize costs.</li>
      </ul>
    </div>
    <br>
    <div style="font-size: 17px;"><strong>Execution Time:</strong></div>
    <ul style="font-size: 16px;">
      <li><strong>Data collection:</strong> 1 day</li>
      <li><strong>Performing operations:</strong> 2 - 3 hours (depending on familiarity with the tools)</li>
    </ul>
    <div style="margin-bottom: 10px;">
      <div style="background:rgb(249, 176, 175); color:rgb(177, 35, 35); border-left: 5px solid;color: rgb(192, 12, 12); padding: 10px 16px; border-radius: 6px;">
        <strong>Warning:</strong> The provided data is only sufficient for analysis; additional data may incur extra costs.
      </div>
    </div>
    <div style="font-size: 17px;"><strong>Prerequisites:</strong></div>
    <ul style="font-size: 16px;">
      <li>An AWS account with access rights to necessary services (S3, IAM, Glue, Redshift, MWAA, QuickSight, etc.).</li>
      <li>Python installed along with related libraries (requests, boto3, etc.).</li>
      <li>Stable internet connection.</li>
      <li>Basic knowledge of AWS and command line operations.</li>
    </ul>
    <div style="font-size: 17px;"><strong>Estimated Cost:</strong>Approximately from <strong>20$</strong> to <strong>30$</strong></div>
  
</div>

<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>