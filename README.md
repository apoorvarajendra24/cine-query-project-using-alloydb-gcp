# 🎬 Cine-Query: Movie Search using Google AlloyDB & Cloud Run

## 📌 Overview
Cine-Query is a cloud-native movie search and information system built on Google Cloud Platform (GCP). It enables users to efficiently query and explore movie data using a high-performance database and scalable serverless infrastructure.

The project combines:
- AlloyDB for PostgreSQL for fast and reliable data processing  
- Cloud Run for containerized, serverless deployment  
- Google Cloud Console & CLI for seamless cloud management  

---

## 🚀 Features
- 🎥 Movie Search – Query and retrieve movie records quickly  
- ⚡ High Performance – Powered by AlloyDB’s columnar engine  
- ☁️ Serverless Scalability – Automatically scales using Cloud Run  
- 🔗 Cloud-Native Integration – Fully built within the GCP ecosystem  

---

## 🛠️ Tech Stack

| Component        | Technology |
|-----------------|-----------|
| Cloud Platform  | Google Cloud Platform (GCP) |
| Database        | AlloyDB for PostgreSQL |
| Backend         | Containerized Application |
| Deployment      | Cloud Run |
| Tools           | Google Cloud Console, GCloud CLI, Docker |

---

## 🏗️ Architecture

```
Client Request
     ↓
Cloud Run (Backend/API)
     ↓
AlloyDB (PostgreSQL Database)
     ↓
Query Execution & Response
```

### Architecture Details
- Cloud Run hosts the backend service and handles incoming requests  
- AlloyDB stores and processes movie-related data  
- VPC Connector / Private IP ensures secure communication  

---

## 📋 Prerequisites
- A Google Cloud Project with billing enabled  
- Google Cloud SDK (gcloud CLI) installed  
- Docker installed  

---

## 🚀 Setup & Deployment

### 1️⃣ AlloyDB Setup
- Create an AlloyDB Cluster and Primary Instance via GCP Console  
- Create a database (e.g., `cine_db`)  
- Create tables for movie data  
- Import dataset into AlloyDB  

---

### 2️⃣ Local Setup

Clone the repository:

```bash
git clone https://github.com/apoorvarajendra24/cine-query-project-using-alloydb-gcp.git
cd cine-query-project-using-alloydb-gcp
```

Set environment variables:

```env
DB_USER=your_username
DB_PASS=your_password
DB_NAME=cine_db
INSTANCE_HOST=your_alloydb_private_ip
```

---

### 3️⃣ Deploy to Cloud Run

Build the container image:

```bash
gcloud builds submit --tag gcr.io/[PROJECT_ID]/cine-query
```

Deploy the service:

```bash
gcloud run deploy cine-query \
  --image gcr.io/[PROJECT_ID]/cine-query \
  --platform managed \
  --vpc-connector [CONNECTOR_NAME] \
  --allow-unauthenticated
```

---

## 🔐 Security Considerations
- Use Private IP for AlloyDB connections  
- Store credentials securely using environment variables  
- Apply IAM roles and permissions for controlled access  

---

## 📈 Future Enhancements
- Natural language movie search (AI integration)  
- Personalized recommendation system  
- Analytics dashboard  
- Integration with Generative AI (Gemini)  

---

## 🔗 Repository
https://github.com/apoorvarajendra24/cine-query-project-using-alloydb-gcp  

---

## ⭐ Final Note
This project demonstrates how to build a scalable, cloud-native application using modern GCP services like AlloyDB and Cloud Run.
