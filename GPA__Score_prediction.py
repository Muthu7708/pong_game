import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
# upload the data
score = pd.read_csv("E:/S.K.Muthu/excel/GAP Prediction.csv")

x = score[['SAT']].values.reshape(-1,1)
y = score[['GPA']].values.reshape(-1,1)

# show the data
plt.scatter(x,y, color='red')
#plt.show()
# split the data test and train
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(y_train.shape,y_test.shape,x_test.shape,x_train.shape)
# initialize the model
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred_1 = y_pred.flatten()
y_test_1 = y_test.flatten()
print(y_test_1.shape,y_pred_1.shape)
#comp_pre = pd.DataFrame({"Actual": y_test_1, "predicted": y_pred_1})
#print(comp_pre)

mae = mean_absolute_error(y_test,y_pred)
print(mae)
mse = mean_squared_error(y_test,y_pred)
print(mse)
r2= r2_score(y_test,y_pred)
print(r2)
print(model.score(x,y))

#
# 0.1835815763263923
# 0.054774825873522025
# 0.16646430906927367

# 0.16268831265429598
# 0.05248610269753723
# 0.46949246374602127






