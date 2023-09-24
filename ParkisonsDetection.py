import numpy as np
import pandas as pd
import os, sys
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df=pd.read_csv('parkinson.xls', delimiter=',')
print(df.head())
print(df.columns())

##Statistical information about data
print(df.describe())

##Check for null and duplicate values
print(df.isnull().sum())
print(df.duplicated().sum())


##Get features and labels
features=df.loc[:, df.columns!='status'].values[:, 1:]
labels=df.loc[:, 'status'].values
##print(features)
##print(labels)

##Get count of each label (0 and 1) in 'labels'
print(labels[labels==1].shape[0], labels[labels==0].shape[0])

##Scale the features to between -1 and 1
scaler=MinMaxScaler((-1, 1))
x=scaler.fit_transform(features)
y=labels

##Split the dataset
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=7)

##Train the model
model=XGBClassifier()
model.fit(x_train, y_train)

##Calculate the accuracy
y_pred=model.predict(x_test)
print(accuracy_score(y_test, y_pred)*100)
