import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# print(train.head())
#Loads the first rows to check if those r correct
print(test.head())
# print(train.info())
# print(train.describe())

# # Data Cleaning
# # Filling missing values of Age
# train["Age"] = train["Age"].fillna(train["Age"].median())
# test["Age"] = test["Age"].fillna(test["Age"].median())
# print(train["Age"])

# # Filling missing values of Embarked
# train["Embarked"] = train["Embarked"].fillna(train["Embarked"].mode()[0])
# print(train["Embarked"])

# # Filling missing values of Fare
# train["Fare"] = train["Fare"].fillna(train["Fare"].median())
# print(train["Fare"])

# #Converting te Text into Numbers as the machines cannot understand Text :
# #(Sex)
# train["Sex"] = train["Sex"].map({"male":0,"female":1})
# test["Sex"] = test["Sex"].map({"male":0,"female":1})
# print(train["Sex"])
# print(test["Sex"])
# #(Embarked)
# train["Embarked"] = train["Embarked"].map({"S":0,"C":1,"Q":2})
# test["Embarked"] = test["Embarked"].map({"S":0,"C":1,"Q":2})
# print(train["Embarked"])
# print(test["Embarked"])

# #Selecting Features :
# features = ["Pclass","Sex","Age","Embarked","Fare","SibSp","Parch",]

# #Prepare X & Y :
# x = train[features]
# y = train["Survived"]
# x_test = test[features]


