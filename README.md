# Loan Default Prediction

“Loan Default Prediction” is a machine learning based project that predicts whether a person
can default a loan in future or not if one is sanctioned to them.
Loans, EMIs, Credit Cards have become one of the important parts of our financial institutions
and our lives. These are also one of the major sources of income for banks and government,
however banks and financial institutions always do a risk check of an individual or an entity
before providing a loan.
This risk check is done by checking the CIBIL Transunion score of an individual, which often
gets affected for an individual if banks do a repeated Score Check, while also for some banks
there is also a lengthy and hefty process of checking whether a person is eligible for a loan or
not and whether they can repay their loan on time or not.
Our Project aims to deep dive into how there Scoring algorithms are designed which check
whether a person can default on their loan or not, what factors are in play and how an end user
can themselves check whether they are eligible for loan or not without wasting bank’s time and
hurting their CIBIL Score. So, we imported the necessary modules that we are going to use in
this project. We imported the modules: -
1. Numpy, pandas
2. Matplotlib (for visualization)
3. train_test_split from scikit(for splitting the datset)
4. SVM from Scikit (our models)
5. Accuracy_score from Scikit(to check the accuracy of the model)
6. Joblib for exporting the model
7. Streamlit for deploying the project as webapp
Our dataset has features like gender, employment status, area of residence, Credit Type,
Income, Loan Amount Requested, Tenure etc.
We have used the Google Collaboratory to do this project. We imported the datasets,
explored the structure of the dataset, learned about top and bottom 5 rows. We got to know

We checked for the null values which we dealt with. So, we started to visualize the data from
which we concluded what factors affect loan approval of an individual. After that we changed
the categorical data into numerical data. The dataset was normalized from the first so we need
not normalize it. We split the dataset into a training set and a testing set.
After the splitting, we used the SVM to evaluate the training model. The model is then trained.
We passed the testing dataset into the model and saw the result. To make it a user-friendly
platform we used Streamlit package to make the webapp.
Hence, the user needs to enter various details about themselves and hit the submit button to get
the result whether bank can approve their loan or not.
In this way, we served the problem statement of our project. 


The Project is Deployed on Streamlit Cloud
## <a href="https://tshankar35-loandefaultpred-home-h2791h.streamlit.app/">Click Here to Visit the Deployed Project</a>
