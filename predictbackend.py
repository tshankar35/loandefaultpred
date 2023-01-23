import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import joblib
dataset = pd.read_csv('LoanPrediction.csv')
X =  dataset.drop(columns=['Unnamed: 0','Loan_ID','Loan_Status','Gender'],axis=1)
Y = dataset['Loan_Status']
print (X.columns)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=11)
classifier = svm.SVC(kernel = 'linear')
classifier.fit(X_train,Y_train)
filename="model.sav"
joblib.dump(classifier,filename)