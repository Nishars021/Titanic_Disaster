import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
print(train.head()) #Loads the first rows to check if those r correct
print(test.head())
