# 🎓 Smart Education Analytics and Student Performance Prediction System using Apache Spark

## 📌 Project Overview

This project implements a **Smart Education Analytics Platform** using **Apache Spark** and **PySpark** to process large-scale educational datasets. The platform performs distributed data processing, exploratory data analysis (EDA), ETL pipeline development, and machine learning to predict student performance and placement probability.

The project also demonstrates **DevOps practices** by containerizing the application with Docker, deploying it using Kubernetes, and automating the build and testing process using GitHub Actions.

---

# 📖 Problem Statement

Educational institutions generate large volumes of student data, including academic records, attendance, online learning activities, examination scores, and placement records.

Traditional systems struggle to efficiently process this growing volume of data.

The objective of this project is to develop a scalable Educational Analytics Platform capable of:

- Processing educational datasets efficiently
- Performing distributed analytics
- Generating academic reports
- Predicting student placement probability
- Automating deployment using modern DevOps tools

---

# 🎯 Objectives

- Initialize Apache Spark and load educational datasets.
- Perform distributed processing using Spark RDDs.
- Implement key-value operations and persistence.
- Perform DataFrame transformations and aggregations.
- Execute Spark SQL queries for educational analytics.
- Develop ETL pipelines.
- Train a Machine Learning model for placement prediction.
- Containerize the application using Docker.
- Deploy the application using Kubernetes.
- Automate build and testing using GitHub Actions.

---

# 🏗️ System Architecture

```
                    Educational Datasets
                             │
                             ▼
                  Apache Spark Session
                             │
        ┌────────────────────┴────────────────────┐
        ▼                                         ▼
    RDD Processing                         DataFrames
        │                                         │
        └────────────────────┬────────────────────┘
                             ▼
                       Spark SQL & EDA
                             │
                             ▼
                      ETL Data Pipeline
                             │
                             ▼
               Machine Learning (MLlib)
                             │
                             ▼
                     Docker Container
                             │
                             ▼
                  Kubernetes Deployment
                             │
                             ▼
                 GitHub Actions CI/CD Pipeline
```

---

# 📂 Project Structure

```
Smart_Education_Analytics/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── data/
│   ├── xAPI-Edu-Data.csv
│   ├── student-mat.csv
│   ├── student-por.csv
│   └── Placement_Data_Full_Class.csv
│
├── documentation/
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── notebooks/
│   └── Case_Study(AI).ipynb
│
├── output/
│
├── screenshots/
│
├── src/
│   └── main.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

# 💻 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Big Data Framework | Apache Spark |
| Spark API | PySpark |
| SQL Engine | Spark SQL |
| Machine Learning | PySpark MLlib |
| Version Control | Git |
| Repository | GitHub |
| Containerization | Docker |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| IDE | Visual Studio Code |

---

# 📊 Datasets Used

### 1. xAPI Educational Dataset

Used for:

- Student attendance analysis
- Student engagement analysis
- Learning activity analysis

---

### 2. Student Mathematics Dataset

Used for:

- Mathematics performance analysis
- Academic report generation

---

### 3. Student Portuguese Dataset

Used for:

- Subject-wise performance analysis

---

### 4. Campus Placement Dataset

Used for:

- Placement prediction
- Placement trend analysis

---

# ⚙️ Project Implementation

## Q1. Spark Initialization

- SparkSession Creation
- Dataset Loading
- Schema Validation

---

## Q2. RDD Operations

Implemented:

- map()
- filter()
- collect()
- count()
- take()

---

## Q3. Key-Value Operations

Implemented:

- reduceByKey()
- groupByKey()
- sortByKey()
- cache()
- persist()

---

## Q4. DataFrame Operations

Implemented:

- Filtering
- GroupBy
- Aggregation
- Join Operations

---

## Q5. Exploratory Data Analysis

Performed:

- Attendance Pattern Analysis
- Subject-wise Performance
- Top Performing Students
- Placement Trends
- Semester-wise Academic Reports

Using Spark SQL.

---

## Q6. ETL Pipeline

Pipeline:

Extract

↓

Transform

↓

Load

Processed data stored in Parquet format.

---

## Q7. Machine Learning

Algorithm:

**Logistic Regression**

Objective:

Predict student placement probability.

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

---

# 🐳 Docker Implementation

## Build Docker Image

```bash
docker build -t smart-education-analytics .
```

---

## Run Docker Container

```bash
docker run --rm smart-education-analytics
```

Output:

```
Spark Started Successfully

Spark Version: 4.1.2

xAPI Dataset Records: 480
```

---

# ☸️ Kubernetes Deployment

## Deploy Application

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

---

## Verify Deployment

```bash
kubectl get deployments

kubectl get pods

kubectl get services

kubectl logs <pod-name>
```

---

# 🚀 GitHub Actions CI/CD Pipeline

The GitHub Actions workflow automates:

- Repository Checkout
- Python Environment Setup
- Dependency Installation
- Python Validation
- Docker Image Build
- Docker Container Testing

Workflow File:

```
.github/workflows/ci-cd.yml
```

---

# 📈 Results

The project successfully:

- Loaded educational datasets into Apache Spark.
- Performed distributed data processing.
- Generated attendance and academic analytics.
- Executed Spark SQL queries.
- Built ETL pipelines.
- Predicted placement probability.
- Containerized the Spark application using Docker.
- Deployed the application on Kubernetes.
- Automated build and testing using GitHub Actions.

---

# 📸 Execution Screenshots

Include screenshots of:

- GitHub Repository
- Spark Initialization
- RDD Operations
- Spark SQL Outputs
- Docker Build
- Docker Run
- Kubernetes Deployment
- Kubernetes Pods
- Kubernetes Logs
- GitHub Actions Success

---

# 🔮 Future Scope

- Apache Kafka Integration
- Spark Streaming
- Cloud Deployment (AWS/Azure/GCP)
- Student Recommendation System
- Interactive Dashboard using Streamlit
- Real-Time Educational Analytics
- Deep Learning Models

---

# 📚 References

- Apache Spark Documentation
- PySpark Documentation
- Docker Documentation
- Kubernetes Documentation
- GitHub Actions Documentation
- UCI Machine Learning Repository
- Kaggle Datasets

---

# 👨‍💻 Developer

**Naresh Desale**

C-DAC Big Data Analytics Case Study

---

# ⭐ GitHub Repository

**Repository Link**

https://github.com/NareshDesale/Smart_Education_Analytics
