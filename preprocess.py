import numpy as np
import pandas as pd
from random import randint
dataset = pd.read_csv("C:\\Users\\tanay\\Downloads\\Project\\LoanPrediction.csv")
dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)
dataset.replace({"Gender":{"Male":0, "Female":1}},inplace=True)
dataset.replace({"Married":{"Yes":1,"No":0}},inplace=True)
dataset.replace({"Education":{"Graduate":1,"Not Graduate":0}},inplace=True)
dataset.replace({"Self_Employed":{"No":0,"Yes":1},'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2}},inplace=True)
dataset.replace({"Credit_History":{"1.0":1,"0.0":1}},inplace=True)
dataset = dataset.replace(to_replace='3+', value=3)
dataset['Gender'].fillna(dataset['Gender'].mode()[0],inplace=True)
dataset['Married'].fillna(dataset['Married'].mode()[0],inplace=True)
dataset['Dependents'].fillna(dataset['Dependents'].mode()[0],inplace=True)
dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0],inplace=True)
dataset['LoanAmount'].fillna(dataset['LoanAmount'].mean(),inplace=True)
dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mean(),inplace=True)
dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0],inplace=True)
dataset.to_csv('LoanPrediction.csv')
