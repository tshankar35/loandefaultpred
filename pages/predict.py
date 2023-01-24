import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import joblib
import streamlit as st
st.title("Lets see the bank can give you loan")

with st.form('form1',clear_on_submit=False):
    col1,col2 = st.columns(2)
    with col1:  
        gender = st.radio("Gender",["Male","Female"])
        married = st.radio("Married",["Yes","No"])
        Education = st.radio("Education",["Graduate","Not Graduate"])
        Self_Employed = st.radio("Self_Employed",["Yes","No"])
        Property = st.selectbox("Property",["Rural","Semi-Urban","Urban"])
    with col2:
        Dependents = st.selectbox("Dependents",[0,1,2,3])
        Income = st.text_input("Your Yearly Income in thousands")
        CoapplicantIncome=st.text_input("Your Guarrantor's Yearly Income in thousands")
        Loan = st.text_input("Your Loan Amount")
        Tenure = st.selectbox("Tenure in Year",[1,2,5,10,15,20,30])
        Credit = st.radio("Have A Credit History i.e. previous open loans?",['Yes','No'])
        

    submit = st.form_submit_button("Submit")


    if submit:
        if gender == "Male":
            gender = 0
        else:
            gender = 1
        if married == "Married":
            married = 1
        else:
            married = 0
        if Education == "Graduate":
            Education = 1
        else:
            Education = 0
        if Self_Employed == "Yes":
            Self_Employed=1
        else:
            Self_Employed=0
        if Property == "Rural":
            Property=0
        elif Property == "Semi-Urban":
            Property=1
        else:
            Property=2
        if Credit == "Yes":
            Credit = 1
        else:
            Credit=0
        Tenure=Tenure*12.0
        loaded_model = joblib.load("./model.sav")
        result = loaded_model.predict([[married,Dependents,Education,Self_Employed,float(Income),float(CoapplicantIncome),float(Loan),Tenure, Credit,Property]])
        st.header(result)
        if result[0]==1:
            st.title("Your Loan has a Good Chance of Approval and the Bank Believes You Can Repay it on time")
        else:
            st.title("Sorry Bank Cannot Approve Your Loan")


