import pandas as pd 
import random
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv("data\housing.csv")
# print(df.isnull().sum())
# EDA process
mean_bedrooms = df["total_bedrooms"].mean()
std_bedrooms = df["total_bedrooms"].std()

print(mean_bedrooms, std_bedrooms)
# fill the missing values
random_values = np.random.randint(118,900,207).tolist()
df["total_bedrooms"]= df["total_bedrooms"].fillna(np.random.choice(random_values))

# Encoding the string data: 
proximity = pd.get_dummies(df["ocean_proximity"], drop_first=True).astype(int)
concat = pd.concat([df, proximity], axis=1)

concat.drop("ocean_proximity", axis=1, inplace=True)
concat.drop("longitude", axis=1, inplace=True)
concat.drop("total_rooms", axis=1, inplace=True)
concat.drop("population", axis=1, inplace=True)

# split data into test and train: 
x= concat.drop("median_house_value", axis=1)
y = concat["median_house_value"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
compare = pd.DataFrame({"Actual" : y_test, "predicted" : y_pred})
print(compare)
score = model.score(x_test, y_test)
print(score)
mse = mean_squared_error(y_test, y_pred)
print(mse)
r2_score = r2_score(y_test, y_pred)
print(r2_score)
mae = mean_absolute_error(y_test, y_pred)
print(mae)
