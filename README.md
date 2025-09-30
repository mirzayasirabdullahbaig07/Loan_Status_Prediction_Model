# 💰 Loan Status Prediction App

An **AI-powered web application** built with **Streamlit** that predicts whether a loan application will be **Approved ✅** or **Not Approved ❌** based on applicant details and financial information.

---

## 🚀 Demo
🔗 [Live App on Streamlit](https://loanstatusprediction07.streamlit.app/)

## 🚀 Video Demo
[https://github.com/user-attachments/assets/e596b16c-7cc1-4b2c-aba9-b769dd540732](https://github.com/user-attachments/assets/e596b16c-7cc1-4b2c-aba9-b769dd540732)

---

## 📌 Features
- Predicts **Loan Approval Status** using a trained **SVM (Support Vector Machine)** model.  
- **Single Applicant Prediction** – Enter details manually to check loan status.  
- **Batch Prediction** – Upload a CSV file with multiple applicants for bulk predictions.  
- Handles **missing values & categorical encoding** automatically.  
- Provides clear and **visual approval statistics**.  
- Includes an **About Me** sidebar with portfolio links.  

---

## 🔍 Usage
1. Open the app in your browser.  
2. Choose between:  
   - **Single Applicant** → Fill out the form with applicant details.  
   - **Batch Prediction** → Upload a CSV file containing applicant data.  
3. Click **Predict Loan Status**.  
4. Get results:  
   - ✅ **Approved** → Loan will be approved.  
   - ❌ **Not Approved** → Loan application rejected.  

---

## 📊 Dataset
The model is trained on the **Loan Prediction Dataset** (commonly used in ML competitions like [Kaggle Loan Prediction](https://www.kaggle.com/datasets/ninzaami/loan-predication)).  

- **Classes**:  
  - `1` → Approved ✅  
  - `0` → Not Approved ❌  

- **Features Used**:  
  - Gender  
  - Married  
  - Dependents  
  - Education  
  - Self_Employed  
  - ApplicantIncome  
  - CoapplicantIncome  
  - LoanAmount  
  - Loan_Amount_Term  
  - Credit_History  
  - Property_Area  

---

## ⚙️ Tech Stack
- **Python 3.9+**  
- **Streamlit** (Frontend Web App)  
- **NumPy & Pandas** (Data Processing)  
- **Scikit-learn** (Model Training – SVM)  
- **Seaborn & Matplotlib** (EDA & Visualization)  
- **Joblib** (Model Serialization)  

---

## 📸 Screenshots
### 🏠 Home Page
<img width="1894" height="789" alt="image" src="https://github.com/user-attachments/assets/bafb99cf-1dbe-4eef-a677-420b1cb0da92" />


### ✅ Prediction Result
<img width="1886" height="825" alt="image" src="https://github.com/user-attachments/assets/522707e0-cae0-4874-81ba-f8948d9a99cf" />


---

## 👨‍💻 Author
**Mirza Yasir Abdullah Baig**  

- 🌐 [Kaggle](https://www.kaggle.com/mirzayasirabdullah07)  
- 💼 [LinkedIn](https://www.linkedin.com/in/mirza-yasir-abdullah-baig/)  
- 💻 [GitHub](https://github.com/mirzayasirabdullahbaig07)  

---

## ❤️ Acknowledgements
- [Loan Prediction Dataset – Kaggle](https://www.kaggle.com/datasets/ninzaami/loan-predication)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Scikit-learn](https://scikit-learn.org/stable/)  

---

## ⚠️ Disclaimer
This project is for **educational purposes only** and should **NOT** be used for actual financial decision-making.  

---
