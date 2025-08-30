import streamlit as st
import pandas as pd
import joblib
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import sklearn.metrics as metrics


# with open("Models/model.pkl", "rb") as f:
#     model = pickle.load(f)

model = joblib.load("Models/model.joblib")

st.title('Fraud Detection Prediction App')

st.markdown("Please enter the transaction details and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value = 0.0, value = 10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value = 0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value = 0.0, value = 0.0)

if st.button('Predict'):
    input_data = pd.DataFrame(
        [
            {
                "type": transaction_type,
                "amount": amount,
                "oldbalanceOrg": oldbalanceOrg,
                "newbalanceOrig": newbalanceOrig,
                "oldbalanceDest": oldbalanceDest,
                "newbalanceDest": newbalanceDest
            }
        ]
    )

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("This Transaction can be Fraud")
    else:
        st.success("This Transaction looks like it is not a Fraud")
