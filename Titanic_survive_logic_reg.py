import pandas as pd
import random
import numpy as np
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as plt
#1 DATA GATHERING
df = pd.read_csv("E:/S.K.Muthu/excel/titanic_dataset.csv")
df.drop("Cabin", axis=1, inplace=True)

#  EDA PROCESS
# survived and not survived person lists and counts men and women wise
survived = pd.crosstab(df["Sex"], df["Survived"])
sex_counts = df.groupby(["Sex", "Survived"]).size()
print(sex_counts)
# women who survived and not survived
women = df[df["Sex"] == "female"]
women_sur = women[women["Survived"] == 1]
women_not_sur = women[women["Survived"] == 0]

# men who survived and not survived
men = df[df["Sex"] == "male"]
men_sur = df[df["Survived"] == 1]
men_not_sur = men[men["Survived"] == 0]



# DATA FEATURING:
# fill null values
count = df["Embarked"].value_counts()
df["Embarked"] = df["Embarked"].fillna("S")
mean = df["Age"].mean()
median = df["Age"].median()
std = df["Age"].std()
random_ages = np.random.randint(mean-std, mean+std, 263)
# random_ages_df = pd.DataFrame(random_ages)
age_copy = df["Age"].copy()
age_copy[np.isnan(age_copy)] = random_ages
df["Age"] = age_copy
df.dropna(inplace=True)

# Feature Transform
df["Sex"] = df["Sex"].map({"male": 1, "female": 0})
enoding_embarked = pd.get_dummies(df["Embarked"], drop_first=True).astype(int)
df = pd.concat([df, enoding_embarked], axis=1)
df.drop(["PassengerId", "Name", "Ticket", "Embarked",], axis=1, inplace=True)

# MODEL BUILDING

# split the data as train and test
X = df.drop("Survived", axis=1)
Y = df["Survived"]
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.2, random_state=43)
model = LogisticRegression(max_iter=1000)
model.fit(Xtrain, Ytrain)

ypred = model.predict(Xtest)
score = model.score(Xtest, Ytest)
print(f'model score {score}')
# TEST UNSEEN DATA
rose = [[1,0,20,0,0,146,0,1]]
jack = [[1,1,22,0,0,142,0,1]]
rose_status = model.predict(rose)
jack_status = model.predict(jack)

if jack_status == 1:
    print("jack was survived")
else:
    print("jack was not survived")
if rose_status == 1:
    print("rose was survived")
else:
    print("rose was not survived")

#VALIDATE THE MODEL
# find accuracy of model
acc_score =  accuracy_score(Ytest, ypred)
print(f'accuracy score of predicted model {acc_score}')
matrix = confusion_matrix(Ytest,ypred)
print(matrix)
#                           Actual       model
# True positive = 152 >> 1  survived    | survived
# True Negative = 15 >> 0   survived    | survived
# False positive 117 >> 0  Not survived | Not survived
# False Negative 15 >> 1   survived     | Not survived

classi_report = classification_report(Ytest,ypred)
print((classi_report))






