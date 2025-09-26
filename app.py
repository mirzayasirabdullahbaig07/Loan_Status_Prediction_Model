# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ------------------------------
# Page configuration
# ------------------------------
st.set_page_config(
    page_title="💰 Loan Approval Predictor",
    page_icon="💳",
    layout="wide"
)

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("About This App")
st.sidebar.info(
    """
    **Loan Approval Prediction App**  
    Predict whether a loan will be approved using a pre-trained SVM model.  
    You can use a CSV dataset for batch predictions or input single applicant data.
    """
)
st.sidebar.title("About Me")
st.sidebar.info(
    """
    **Mirza Yasir Abdullah Baig**  

    - [LinkedIn](https://www.linkedin.com/in/mirza-yasir-abdullah-baig/)  
    - [GitHub](https://github.com/mirzayasirabdullahbaig07)  
    - [Kaggle](https://www.kaggle.com/mirzayasirabdullah07)  
    """
)

# ------------------------------
# Load Model
# ------------------------------
if os.path.exists("loan_model.joblib"):
    model_data = joblib.load("loan_model.joblib")
    model = model_data['model']
    model_columns = model_data['columns']
else:
    st.error("Model file loan_model.joblib not found!")
    st.stop()

# ------------------------------
# Tabs for Single and Batch Prediction
# ------------------------------
tab1, tab2 = st.tabs(["Single Applicant", "Batch Prediction (CSV)"])

# ------------------------------
# Single Applicant Prediction
# ------------------------------
with tab1:
    st.header("Predict Loan Approval for Single Applicant")
    with st.form("single_form"):
        col1, col2 = st.columns(2)
        with col1:
            Gender = st.selectbox("Gender", ["Male", "Female"])
            Married = st.selectbox("Married", ["Yes", "No"])
            Dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)
            Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
            Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
            ApplicantIncome = st.number_input("Applicant Income", min_value=0, value=2500)
        with col2:
            CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0, value=0)
            LoanAmount = st.number_input("Loan Amount (in thousands)", min_value=0, value=100)
            Loan_Amount_Term = st.number_input("Loan Amount Term (in months)", min_value=12, value=360)
            Credit_History = st.selectbox("Credit History", [1, 0])
            Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

        submit_button = st.form_submit_button("Predict Loan Status")

    if submit_button:
        input_df = pd.DataFrame([{
            'Gender': 1 if Gender=="Male" else 0,
            'Married': 1 if Married=="Yes" else 0,
            'Dependents': Dependents,
            'Education': 1 if Education=="Graduate" else 0,
            'Self_Employed': 1 if Self_Employed=="Yes" else 0,
            'ApplicantIncome': ApplicantIncome,
            'CoapplicantIncome': CoapplicantIncome,
            'LoanAmount': LoanAmount,
            'Loan_Amount_Term': Loan_Amount_Term,
            'Credit_History': Credit_History,
            'Property_Area': {"Rural":0,"Semiurban":1,"Urban":2}[Property_Area]
        }])

        input_df = input_df.reindex(columns=model_columns, fill_value=0)
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Not Approved")

# ------------------------------
# Batch Prediction
# ------------------------------
with tab2:
    st.header("Batch Prediction from CSV")
    uploaded_file = st.file_uploader("Upload CSV with loan applicants data", type=["csv"], key="batch_csv")

    use_sample = st.checkbox("Use Sample CSV", key="sample_csv")
    if use_sample:
        sample_csv_path = "dataset.csv"
        if os.path.exists(sample_csv_path):
            uploaded_file = sample_csv_path
        else:
            st.error("Sample CSV not found!")

    if uploaded_file:
        batch_data = pd.read_csv(uploaded_file)
        st.subheader("Uploaded CSV Preview")
        st.dataframe(batch_data.head(10))

        if st.button("Predict for CSV"):
            # ------------------------------
            # Preprocessing missing values
            # ------------------------------
            # Replace '3+' in Dependents with 4
            batch_data['Dependents'] = batch_data['Dependents'].replace('3+', 4)

            # Convert numeric columns to float
            numeric_cols = ['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Dependents']
            for col in numeric_cols:
                batch_data[col] = pd.to_numeric(batch_data[col], errors='coerce')

            # Fill numeric missing values with median
            for col in numeric_cols:
                batch_data[col] = batch_data[col].fillna(batch_data[col].median())

            # Fill categorical missing values with mode
            categorical_cols = ['Gender','Married','Education','Self_Employed','Property_Area']
            for col in categorical_cols:
                batch_data[col] = batch_data[col].fillna(batch_data[col].mode()[0])

            # Map categorical columns
            batch_data['Gender'] = batch_data['Gender'].map({'Male':1,'Female':0})
            batch_data['Married'] = batch_data['Married'].map({'Yes':1,'No':0})
            batch_data['Education'] = batch_data['Education'].map({'Graduate':1,'Not Graduate':0})
            batch_data['Self_Employed'] = batch_data['Self_Employed'].map({'Yes':1,'No':0})
            batch_data['Property_Area'] = batch_data['Property_Area'].map({'Urban':2,'Semiurban':1,'Rural':0})

            # Align columns with training model
            batch_features = batch_data.reindex(columns=model_columns, fill_value=0)

            # Predict
            batch_predictions = model.predict(batch_features)
            batch_data['Predicted_Loan_Status'] = np.where(batch_predictions==1, 'Approved ✅', 'Not Approved ❌')

            st.subheader("Batch Prediction Results")
            st.dataframe(batch_data.head(10))

            # Approval statistics
            st.subheader("Approval Statistics")
            st.bar_chart(batch_data['Predicted_Loan_Status'].value_counts())

            # Download button
            csv_pred = batch_data.to_csv(index=False)
            st.download_button(
                label="📥 Download Batch Predictions",
                data=csv_pred,
                file_name="batch_predictions.csv",
                mime="text/csv"
            )
