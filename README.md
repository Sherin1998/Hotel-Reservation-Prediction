# 🏨 Hotel Booking Prediction – MLOps Certification Project

## Overview
In this project, the goal is to develop a predictive model to determine whether a hotel booking will be canceled—a critical task for hotels, as cancellations can significantly impact revenue and operational planning. The dataset includes numerous features related to bookings, such as lead time, deposit type, and special requests, which increases the complexity of the modeling process. Key challenges involve comprehensive data preprocessing, including feature selection and engineering, handling missing values, and managing data noise. Furthermore, multiple models will be trained, their performance evaluated using appropriate metrics, and insights will be drawn by analyzing the most influential features that drive hotel booking cancellations.

The system predicts hotel booking outcomes, enabling **data-driven decisions for operational efficiency**.

<img width="1361" height="620" alt="Screenshot 2025-10-08 114342" src="https://github.com/user-attachments/assets/9a190838-95aa-4ccc-b3dc-025c6c48651f" />


---

## Features
- **ETL Pipelines**: Automates data ingestion, cleaning, and preprocessing.
- **Data Engineering & Feature Selection**: Optimizes model inputs for improved accuracy.
- **Model Building**: Classification models built using Python and scikit-learn.
- **Experiment Tracking**: Managed with MLflow for reproducibility and monitoring.
- **Deployment & CI/CD**: Dockerized application and automated deployment using CircleCI.
- **Cloud Storage Integration**: Scalable storage via Google Cloud Platform (GCP).


---

## Dataset
- The project uses [Hotel Booking Dataset](https://www.kaggle.com/code/farzadnekouei/hotel-booking-cancellation-prediction) from Kaggle.
- Data includes booking details, customer demographics, and stay information.

<img width="1077" height="573" alt="image" src="https://github.com/user-attachments/assets/00c52593-64c0-43d3-9afe-0a467b14750d" />


---

## Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/hotel-booking-mlops.git
cd hotel-booking-mlops


## ☁️ Google Cloud Platform (GCP) Setup

Follow these steps to configure GCP for the Hotel Booking Prediction MLOps project.

---

### **Step 1: Create a GCP Account**
1. Go to [https://cloud.google.com](https://cloud.google.com) and sign in or create an account.
2. Set up billing (free tier credits can be used initially).

---

### **Step 2: Create a New Project**
1. Navigate to **Google Cloud Console → Select a Project → New Project**.
2. Give it a **name** (e.g., `hotel-booking-mlops`) and note the **Project ID**.

---

### **Step 3: Enable Required APIs**
1. Go to **APIs & Services → Library**.
2. Enable the following APIs:  
   - Cloud Storage API  
   - AI Platform / Vertex AI API (if using managed ML)  
   - Compute Engine API  

---

### **Step 4: Create a Service Account**
1. Navigate to **IAM & Admin → Service Accounts → Create Service Account**.
2. Assign a name (e.g., `mlops-service-account`) and select roles:  
   - **Storage Admin** (access to Cloud Storage)  
   - **ML Engine Admin** (if using AI Platform/Vertex AI)  
3. Complete the creation.

---

### **Step 5: Generate a Key File**
1. In the service account list, click **Actions → Manage Keys → Add Key → Create new key**.
2. Choose **JSON** format and download the key file.  
   ⚠️ Keep it secure as it will be used to authenticate your scripts.

---

### **Step 6: Set Environment Variable**
Set the JSON key path so your code can authenticate with GCP:

- **Windows (Command Prompt):**
```bash
set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your-key.json"

