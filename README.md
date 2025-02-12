# 🚀 End-to-End ML Pipeline with Airflow & Docker

This project automates the entire **Machine Learning (ML) workflow** using **Apache Airflow** inside a **Docker container**. The pipeline includes **data preprocessing, model training, and evaluation**, all scheduled using Airflow.

---

## 📂 **Project Structure**
```
ml_pipeline_project/  
│── dags/                  # Airflow DAGs (workflow scripts)  
│   ├─ ml_pipeline.py     # Main Airflow DAG file  
│── scripts/               # Python scripts for each step  
│   ├─ download_data.py   # Step 1: Download & preprocess data  
│   ├─ train_model.py     # Step 2: Train model  
│   └─ evaluate_model.py  # Step 3: Evaluate model  
│── models/                # Trained ML models  
│── data/                  # Raw & processed data  
│── logs/                  # Logs generated from Airflow  
│── Dockerfile             # (Optional) Custom Docker setup  
│── requirements.txt       # Python dependencies  
│── docker-compose.yaml    # Airflow setup  
│── README.md              # Project explanation  
```

---

## 🔧 **Setup Instructions**
### **1️⃣ Prerequisites**
Ensure you have the following installed:
- **Docker** (Running in the background)
- **Docker Compose**
- **VS Code (or any code editor)**

---

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/onehungrybird/airflow_ml_pipeline.git
cd ml_pipeline_project
```

---

### **3️⃣ Setup and Run Airflow**
Run the following to start Airflow in Docker:
```bash
docker-compose up -d
```
This will:
✅ Start Airflow Scheduler & Web Server  
✅ Install required dependencies (e.g., `scikit-learn`, `pandas`)  

Once running, access **Airflow UI** at:  
🔗 **http://localhost:8080**

---

### **4️⃣ Trigger the ML Pipeline**
1. Open **Airflow UI** (`http://localhost:8080`).
2. Find the DAG **`ml_pipeline`**.
3. Click **"Trigger DAG"** to start the pipeline manually.

This executes:
✅ **Step 1:** Download & preprocess data (`download_data.py`)  
✅ **Step 2:** Train the model (`train_model.py`)  
✅ **Step 3:** Evaluate the model (`evaluate_model.py`)  

---

## 📊 **Verify the Outputs**
### **Check the Trained Model**
The trained model will be saved in:
```
models/iris_model.pkl
```

### **Check Evaluation Metrics**
Model accuracy is logged in:
```
logs/metrics.txt
```
To check:
```bash
cat logs/metrics.txt
```

---

## 🛠 **Stopping and Restarting Airflow**
To **stop** all services:
```bash
docker-compose down
```
To **restart**:
```bash
docker-compose up -d
```

To **reset Airflow completely** (if needed):
```bash
docker-compose down --volumes --remove-orphans
docker-compose up -d
```

---

## 📝 **Future Enhancements**
- [ ] **Deploy on AWS** (S3 for storage, SageMaker for training)
- [ ] **Add CI/CD with GitHub Actions**
- [ ] **Integrate MLflow for model tracking**
- [ ] **Add feature selection & hyperparameter tuning**

---

## 📌 **Contributing**
Feel free to submit **pull requests** or report issues.

🔗 **Author:** Manish Sahu
🔗 **GitHub:** https://github.com/onehungrybird/airflow_ml_pipeline.git 
```

---

### 🚀 **Next Steps**
✅ **Copy and paste this `README.md` into your project**  
✅ **Push to GitHub:**
```bash
git add README.md
git commit -m "Added project README"
git push origin main
```
✅ **Share your repo link if you'd like feedback!**  

Let me know if you need any modifications. 🚀🔥

