🚢 Titanic Survival Prediction using Machine Learning

📌 Project Overview

This project is based on Kaggle's Titanic - Machine Learning from Disaster competition. The objective is to build a machine learning model that predicts whether a passenger survived the Titanic disaster using passenger information such as age, gender, ticket class, fare, and family details.

The project follows a complete machine learning workflow, including data preprocessing, handling missing values, feature engineering, model training, prediction generation, and submission file creation.

🎯 Objective

Predict passenger survival on the Titanic using historical passenger data and machine learning techniques.

📊 Dataset

The dataset contains information about Titanic passengers, including:

PassengerId, 
Pclass (Passenger Class), 
Name, 
Sex, 
Age, 
SibSp (Siblings/Spouses aboard), 
Parch (Parents/Children aboard), 
Ticket, 
Fare, 
Cabin, 
Embarked, 
Survived (Target Variable).

Dataset Source: Kaggle Titanic Competition

🛠️ Technologies Used
Python, 
Pandas, 
NumPy, 
Scikit-Learn, 
Random Forest Classifier.


⚙️ Project Workflow
1. Data Loading : Imported training and testing datasets using Pandas.
2. Data Cleaning : Filled missing Age values using Median,
Filled missing Embarked values using Mode,
Filled missing Fare values using Median.
3. Data Preprocessing : Converted categorical values into numerical values:
Male → 0,
Female → 1,
S → 0,
C → 1,
Q → 2.
4. Feature Selection : Selected the following features:
Pclass,
Sex,
Age,
Embarked,
Fare,
SibSp,
Parch.
5. Model Training : Trained a Random Forest Classifier using the training dataset.

6. Prediction : Generated survival predictions for the test dataset.

7. Submission : Created a Kaggle-compatible submission file containing:
PassengerId, Survived

📈 Machine Learning Model : 

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier
(

    n_estimators=100,
    
    random_state=42
)


🚀 How to Run : 

pip install pandas numpy scikit-learn

python index.py

🎓 Learning Outcomes

Through this project, I learned :
Data Cleaning,
Handling Missing Values,
Feature Engineering,
Data Preprocessing,
Machine Learning Fundamentals,
Random Forest Classification,
Kaggle Competition Workflow,
Model Training and Prediction.

🏆 Kaggle Competition : This project is based on the Kaggle competition --> Titanic - Machine Learning from Disaster

(The competition serves as an introduction to machine learning and predictive modeling using real-world data.)

👩‍💻 Author : Nisha R S
