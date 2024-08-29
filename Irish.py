import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score

df = pd.read_csv("data\iris.csv")
# print(df.isnull().sum())

# split data into train and test
x = df.drop("Species", axis=1)
y = df["Species"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
compare = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

# find unseen data 
randam = [[5.1,3.5,1.4,0.2]]

status = model.predict(randam)
print(status)

#find accuracy
score = model.score(x_test, y_test)
print(f'model score {score}')

classification_report = classification_report(y_test, y_pred)
print("Classification Report: \n", classification_report)    

confusion_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix : \n',confusion_matrix)

accuracy_score = accuracy_score(y_test, y_pred)
print("Accuracy Score:", accuracy_score)

f1_score = f1_score(y_test, y_pred, average="macro")
print("F1 Score:", f1_score)

precision_score = precision_score(y_test, y_pred, average="macro")
print("Precision Score:", precision_score)

recall_score = recall_score(y_test, y_pred, average="macro")
print("Recall Score:", recall_score)



