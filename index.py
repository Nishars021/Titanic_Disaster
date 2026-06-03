import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# print(train.head()) #Loads the first rows to check if those r correct
# # print(test.head())
# print(train.info())
# print(train.describe())

#Data Cleaning
#Filling missing values of Age
# train["Age"] = train["Age"].fillna(train["Age"].median())
# test["Age"] = test["Age"].fillna(test["Age"].median())
# print(train["Age"])

#Filling missing values of Embarked
# train["Embarked"] = train["Embarked"].fillna(train["Embarked"].mode()[0])
# print(train["Embarked"])

#Filling missing values of Fare
train["Fare"] = train["Fare"].fillna(train["Fare"].median())
print(train["Fare"])