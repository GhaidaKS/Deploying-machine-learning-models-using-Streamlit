import pandas as pd

train = pd.read_csv('data.csv')
train.head()
train['Gender']= train['Gender'].map({'Male':0, 'Female':1})
train['Married']= train['Married'].map({'No':0, 'Yes':1})
train['Loan_Status']= train['Loan_Status'].map({'N':0, 'Y':1})
##print (train.isnull().sum())
train = train.dropna()
##print (train.isnull().sum())

X = train[['Gender', 'Married', 'ApplicantIncome', 'LoanAmount', 'Credit_History']]
y = train.Loan_Status
X.shape, y.shape
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size = 0.25, random_state = 10)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(max_depth=4, random_state = 10)
model.fit(x_train, y_train)
from sklearn.metrics import accuracy_score
pred_y = model.predict(x_test)
print("TEST accuracy score : ",accuracy_score(y_test,pred_y)*100,'%')
pred_train = model.predict(x_train)
print("TRAIN accuracy score : ",accuracy_score(y_train,pred_train)*100,'%')
print()

import matplotlib.pyplot as plt

train['age'].value_counts(sort=True).plot.bar()
plt.show()
train['reason'].value_counts(sort=True).plot.bar()
plt.show()


import pickle
pickle_out = open("classifier.pkl", mode = "wb")
pickle.dump(model, pickle_out)
pickle_out.close()














