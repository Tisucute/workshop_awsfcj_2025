---
title : "Building an Automated Real-Time Data Processing and Visualization Architecture on AWS"
date: 2025-06-18 
weight : 1 
chapter : false
---

# Building an Automated Real-Time Data Processing and Visualization Architecture on AWS

**Author:** Nguyễn Ngọc Anh Thư  
**Student ID:** 22133059  
**Email:** ngocanhthugialai@gmail.com  
**University:** Ho Chi Minh City University of Technology and Education (HCMUTE)

### Overview

The project "Building an Automated Processing and Real-time Data Visualization Architecture on AWS" represents my dedication and effort to develop a comprehensive system that automates the collection, processing, and visualization of real-time data streams using Amazon Web Services (AWS). With the aim of meeting the increasing demand for timely analysis and decision-making based on the latest data, the system is designed to include key components: weather data collection from OpenWeather API using Python and storage in AWS S3; orchestration managed by Amazon Managed Workflows for Apache Airflow (MWAA); data processing and transformation using AWS Glue; data storage in AWS Redshift warehouse; and finally, visualization of results through AWS QuickSight on an intuitive dashboard.

Infrastructure deployment is implemented through Infrastructure as Code (IaC) using AWS CloudFormation, ensuring consistency, automation, ease of management, and scalability for future resource changes or additions. Security policies and access management are also configured through AWS IAM and a secure Virtual Private Cloud (VPC) environment to ensure system safety.

I genuinely hope this report not only accurately reflects my efforts but also serves as a friendly, easy-to-understand resource for students new to AWS or modern development methodologies. Through this work, I aim to convey my enthusiasm and passion for technology and support students in gaining confidence as they embark on their AWS exploration and application journey.

### Implementation Timeline

- **Data collection:** 1 day 
- **Execution of steps:** 2–3 hours (depending on familiarity with the tools)
{{% notice warning %}}
The data is only sufficient for analysis; collecting more may incur additional costs.
{{% /notice %}}
- **Thực hiện các thao tác:** 2 - 3 tiếng (tùy vào độ quen thuộc với các công cụ)

### Contents

1. [Introduction](1-introduce/)
2. [Tools and Architecture Diagram](2-architecture/)
   - [Tools Used](2-architecture/2.1-tools/)
   - [Architecture Diagram](2-architecture/2.2-architecture/)
3. [Steps for Automated ETL Process](3-etl-process/)
   - [About Environment Files](3-etl-process/3.1-env-files/)
   - [Infrastructure as Code Deployment](3-etl-process/3.2-infra-as-code/)
   - [Setting Variables, Creating Connections, and Uploading Environment](3-etl-process/3.3-setup-variables-connection/)
   - [ETL Execution Process](3-etl-process/3.4-etl-execution/)
4. [Analysis and Visualization](4-analysis-visualization/)
   - [Analysis with AWS Redshift](4-analysis-visualization/4.1-redshift/)
   - [Visualization with AWS Quicksight](4-analysis-visualization/4.2-quicksight/)
5. [Cleanup](5-cleanup/)