# 🏨 Hotel Booking Prediction – MLOps Certification Project

## Overview
This project aims to develop a predictive model to determine whether a hotel booking will be canceled—a critical task for hotels, as cancellations can significantly impact revenue and operational planning.  

The dataset includes features such as lead time, deposit type, special requests, and more. Key challenges include data preprocessing, feature engineering, handling missing values, and managing noisy data. Multiple models are trained, evaluated with appropriate metrics, and analyzed for feature importance to provide actionable insights.

The system predicts hotel booking outcomes, enabling **data-driven decisions for operational efficiency**.

![Project Screenshot](https://github.com/user-attachments/assets/9a190838-95aa-4ccc-b3dc-025c6c48651f)

---

## Features
- **ETL Pipelines**: Automates data ingestion, cleaning, and preprocessing.
- **Data Engineering & Feature Selection**: Optimizes model inputs for improved accuracy.
- **Model Building**: Classification models using Python and scikit-learn.
- **Experiment Tracking**: Managed with MLflow for reproducibility.
- **Deployment & CI/CD**: Dockerized application and automated deployment using CircleCI.
- **Cloud Storage Integration**: Scalable storage via Google Cloud Platform (GCP).

![Features Screenshot](https://github.com/user-attachments/assets/9fba5891-9161-4945-bf92-27c254d0dab4)

---

## Dataset
- Source: [Hotel Booking Dataset - Kaggle](https://www.kaggle.com/code/farzadnekouei/hotel-booking-cancellation-prediction)
- Includes booking details, customer demographics, and stay information.

![Dataset Screenshot](https://github.com/user-attachments/assets/00c52593-64c0-43d3-9afe-0a467b14750d)

---

## Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/hotel-booking-mlops.git
cd hotel-booking-mlops




2️⃣ Create & Activate Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

☁️ Google Cloud Platform (GCP) Setup
Step 1: Create a GCP Account

Go to https://cloud.google.com
 and sign in or create an account.

Set up billing (free tier credits available).

Step 2: Create a New Project

Navigate to Google Cloud Console → Select a Project → New Project.

Name it (e.g., hotel-booking-mlops) and note the Project ID.

Step 3: Enable Required APIs

Enable the following APIs:

Cloud Storage API

AI Platform / Vertex AI API

Compute Engine API

Step 4: Create a Service Account

Go to IAM & Admin → Service Accounts → Create Service Account.

Name it (e.g., mlops-service-account) and assign roles:

Storage Admin

ML Engine Admin

Complete the creation.

Step 5: Generate a Key File

Click Actions → Manage Keys → Add Key → Create new key.

Choose JSON format and download the key file.
⚠️ Keep it secure.

Step 6: Set Environment Variable (Windows)
set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your-key.json"

2️⃣ Run ETL & Model Training (Windows)
2.1 **Run ETL Pipeline****
python pipeline/setup.py


2.2 **Train the Model**
python src/model_training.py


2.3 **Start the Flask Application**

Activate virtual environment first:

venv\Scripts\activate


Run Flask app:

**python app.py**


Open in browser:
http://localhost:5000
