# Smart Education Analytics and Student Performance Prediction System using Apache Spark

## Project Overview

This project implements a **Smart Education Analytics and Student Performance Prediction System** using **Apache Spark and PySpark**.

The objective is to analyze student academic records, attendance, online learning activities, examination scores, and placement records to generate useful educational insights and predict placement outcomes.

The project demonstrates Big Data processing using Spark, Exploratory Data Analysis (EDA), Spark SQL, ETL Pipeline development, and Machine Learning with PySpark MLlib.

---

# Problem Statement

A university collects student academic records, attendance data, online learning activities, examination scores, and placement records.

The university wants to build an Educational Analytics Platform to:

- Improve academic performance
- Monitor attendance
- Analyze online learning activities
- Generate semester-wise reports
- Predict placement probability

Apache Spark is used for distributed data processing and PySpark MLlib is used for machine learning.

---

# Objectives

- Initialize Apache Spark and load educational datasets.
- Perform RDD transformations and actions.
- Implement Key-Value operations and persistence.
- Perform DataFrame operations including joins and aggregations.
- Analyze educational data using Spark SQL.
- Develop ETL pipelines for academic and placement datasets.
- Build a Machine Learning model to predict placement probability.
- Containerize the application using Docker.
- Deploy using Kubernetes.
- Implement CI/CD using GitHub Actions.

---

# Technologies Used

- Apache Spark
- PySpark
- Spark SQL
- PySpark MLlib
- Python
- Pandas
- Git
- GitHub
- Docker
- Kubernetes
- GitHub Actions
- VS Code

---

# Datasets Used

## 1. xAPI Educational Dataset

Purpose:

- Student Attendance
- Online Learning Activities
- Student Engagement
- Academic Performance

Dataset Link:

https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data

---

## 2. Student Mathematics Dataset

Purpose:

- Academic Performance
- Examination Scores

Dataset Link:

https://archive.ics.uci.edu/ml/datasets/student+performance

---

## 3. Student Portuguese Dataset

Purpose:

- Subject-wise Performance

Dataset Link:

https://archive.ics.uci.edu/ml/datasets/student+performance

---

## 4. Campus Placement Dataset

Purpose:

- Placement Analysis
- Placement Prediction

Dataset Link:

https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement

---

# Project Structure

```
Smart_Education_Analytics/
│
├── data/
│   ├── xAPI-Edu-Data.csv
│   ├── student-mat.csv
│   ├── student-por.csv
│   └── Placement_Data_Full_Class.csv
│
├── notebooks/
│   └── Case_Study(AI).ipynb
│
├── src/
│
├── output/
│
├── screenshots/
│
├── documentation/
│
├── kubernetes/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Project Workflow

```
Educational Datasets
        │
        ▼
Spark Initialization
        │
        ▼
RDD Operations
        │
        ▼
Key-Value Operations
        │
        ▼
DataFrame Operations
        │
        ▼
Spark SQL + EDA
        │
        ▼
ETL Pipeline
        │
        ▼
Machine Learning Model
        │
        ▼
Placement Prediction
        │
        ▼
Docker
        │
        ▼
Kubernetes
        │
        ▼
CI/CD Deployment
```

---

# Features Implemented

## Q1. Spark Initialization and Data Loading

- SparkSession Initialization
- Data Loading
- Schema Validation

---

## Q2. RDD Implementation

- map()
- filter()
- count()
- take()
- countByValue()

---

## Q3. Key-Value Operations

- reduceByKey()
- groupByKey()
- sortByKey()
- cache()
- unpersist()

---

## Q4. DataFrame Operations

- DataFrame Join
- Aggregation
- Filtering
- GroupBy
- Average Calculation

---

## Q5. Exploratory Data Analysis

Performed:

- Attendance Analysis
- Subject-wise Performance
- Top Performing Students
- Placement Trends
- Semester-wise Academic Reports

Spark SQL Queries:

- SELECT
- GROUP BY
- ORDER BY
- AVG
- COUNT
- LIMIT

---

## Q6. ETL Pipeline

### Academic Data

Extract

↓

Transform

↓

Load

### Placement Data

Extract

↓

Transform

↓

Load

Output stored in Parquet format.

---

## Q7. Machine Learning

Algorithm:

Logistic Regression

Framework:

PySpark MLlib

Prediction:

- Placement Status

Evaluation:

- Area Under ROC Curve (AUC)

---

# Installation

## Clone Repository

```bash
git clone https://github.com/NareshDesale/Smart_Education_Analytics.git
```

Move into project directory

```bash
cd Smart_Education_Analytics
```

Install required libraries

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run Jupyter Notebook

```bash
jupyter notebook
```

Open

```
Case_Study(AI).ipynb
```

Run all cells sequentially.

---

# Outputs

The project generates:

- Attendance Analysis
- Student Performance Reports
- Placement Analysis
- ETL Output
- Machine Learning Predictions
- Model Evaluation Report

---

# Screenshots

Include screenshots of:

- Spark Initialization
- RDD Operations
- DataFrame Operations
- Spark SQL Outputs
- ETL Pipeline
- Machine Learning Output
- Docker Build
- Kubernetes Deployment
- GitHub Actions

---

# Future Scope

- Real-time Student Analytics
- Spark Streaming
- Kafka Integration
- Interactive Dashboard using Streamlit
- Cloud Deployment (AWS / Azure / GCP)

---

# Author

**Naresh Desale**

C-DAC Student

---

# Conclusion

This project demonstrates how Apache Spark can be used to process large-scale educational datasets efficiently.

The system integrates distributed data processing, SQL analytics, ETL pipelines, and machine learning to help educational institutions improve student performance analysis and placement prediction.
