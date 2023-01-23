import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

dataset = pd.read_csv('LoanPrediction.csv')
dataset.drop(columns=['Unnamed: 0'],inplace=True)
st.title("Data Preprocessing and Visualisation")
st.header("Dataset Head")
st.write(dataset.head())
st.header("The Shape of DataSet is: ")
st.write(dataset.shape)
st.header("Columns are: ")
st.write(dataset.columns)
fig = plt.figure(figsize=(10,4))
sns.countplot(x='Education',hue='Loan_Status',data=dataset)
st.pyplot(fig)
sns.countplot(x='Married',hue='Loan_Status',data=dataset)
st.pyplot(fig)
sns.countplot(x='Dependents',hue='Loan_Status',data=dataset)
st.pyplot(fig)
sns.countplot(x='Credit_History',hue='Loan_Status',data=dataset)
st.pyplot(fig)
