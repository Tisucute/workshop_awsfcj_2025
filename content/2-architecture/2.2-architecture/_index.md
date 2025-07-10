---
title : "Architecture Diagram"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---
### Architecture Diagram

- **This architecture describes a process for collecting, processing, storing, analyzing, and visualizing weather data using AWS services and open-source tools. Initially, users request weather information. A Python script packaged and stored within an Amazon S3 environment is automatically invoked by Apache Airflow (MWAA) according to a predefined schedule. This Python script leverages PySpark (Spark integrated directly into the Python script) to call the OpenWeather API, retrieve real-time weather data, perform preliminary processing, and store the raw data into an Amazon S3 bucket. Subsequently, AWS Glue Jobs perform advanced ETL tasks, cleaning and normalizing the data before loading it into Amazon Redshift for deeper analysis. Amazon QuickSight then connects to Redshift to build interactive dashboards, enabling users to visualize and easily analyze data to make informed decisions.**

- **The entire infrastructure and services are automatically managed and deployed through AWS CloudFormation, secured by AWS IAM, VPC, and Secrets Manager, ensuring controlled access and secure storage of sensitive information within the system.** 

The diagram below illustrates the overall system architecture on AWS:
![So Do](/images/2.architecture/Kien_truc.png)

<!-- logo bên dưới -->
<div style="position: bottom; height: 100px;">
  <div style="position: absolute; bottom: 10px; right: 10px; display: flex; gap: 20px; align-items: end;">
  <img src="/images/1.introduction/logo_aws.jpg" alt="AWS Logo" style="height: 100px;">
  </div>
</div>