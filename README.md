# 🚀 PySpark ETL Pipeline with Prefect (Bronze → Silver → Gold)

## 📌 Overview

This project implements an end-to-end **data engineering pipeline** using PySpark and Prefect.

The pipeline follows a **medallion architecture**:

* **Bronze Layer** → Raw data ingestion
* **Silver Layer** → Data cleaning & transformation
* **Gold Layer** → Aggregated insights

The workflow is orchestrated using Prefect and integrated with CI/CD using GitHub Actions.

---

## 🛠 Tech Stack

* **PySpark** – Data processing
* **Prefect** – Workflow orchestration
* **Parquet** – Storage format
* **GitHub Actions** – CI/CD pipeline
* **Python 3.11**

---

## 📂 Project Structure

```
project/
│
├── data/
│   └── patients.csv
│
├── output/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── pipeline_6may.py     # ETL logic (Bronze, Silver, Gold)
├── dag.py               # Prefect workflow (orchestration)
├── test_pipeline.py     # Unit tests
├── README.md
└── .github/workflows/
    └── pipeline.yml     # CI/CD pipeline
```

---

## 🔄 Pipeline Architecture

```
Raw CSV → Bronze → Silver → Gold
```

### 🟤 Bronze Layer

* Reads raw CSV data
* Stores data as-is in Parquet format

### ⚪ Silver Layer

* Filters recent data
* Handles missing values
* Removes duplicates

### 🟡 Gold Layer

* Aggregates billing data by diagnosis
* Produces final analytical dataset

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install pyspark prefect pytest
```

### 2. Run the pipeline

```
python dag.py
```

### 3. View Prefect UI (optional)

```
prefect server start
```

Then open:
http://127.0.0.1:4200

---

## 🔁 CI/CD Pipeline

This project uses **GitHub Actions** to automate testing.

### Trigger:

* Runs on every `git push`

### Steps:

* Install dependencies
* Run unit tests

Check results in the **Actions** tab of the repository.

---

## 📊 Sample Output

### Gold Layer Output:

```
diagnosis   | total_billing
------------|---------------
Diabetes    | 500
Cardiac     | 800
```

---

## 🧠 Key Learnings

* Building ETL pipelines with PySpark
* Designing medallion architecture (Bronze/Silver/Gold)
* Workflow orchestration using Prefect
* Handling serialization issues in distributed systems
* Implementing CI/CD for data pipelines

---

## 🚀 Future Improvements

* Add Delta Lake (ACID transactions, MERGE)
* Integrate cloud storage (AWS S3 / GCP)
* Add advanced unit tests for transformations
* Deploy using Airflow for production workflows

---

## 👨‍💻 Author

**Soham Khanna**
