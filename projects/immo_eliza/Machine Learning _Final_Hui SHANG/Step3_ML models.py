import pandas as pd

df = pd.read_csv('./Data for Machine Learning.csv')

del df['Unnamed: 0']
del df['Unnamed: 0.1']
del df['Unnamed: 0.2']

df = df.drop_duplicates(inplace=True)

import numpy as np

X = df.drop(columns=['price']).to_numpy()
y = df['price'].to_numpy().reshape(-1, 1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.17, random_state=0 )


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from sklearn.metrics import mean_absolute_error, r2_score
#linear regression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(mae, r2)

#GradientBoostingRegressor
# Initialize and train the Gradient Boosting Regressor
model = GradientBoostingRegressor(n_estimators=800, learning_rate=0.08, max_depth=9, random_state=0)
model.fit(X_train, y_train.ravel())  # Flatten y_train to 1D array
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)
train_mae = mean_absolute_error(y_train, train_predictions)
test_mae = mean_absolute_error(y_test, test_predictions)
print(train_mae, test_mae)

train_r2 = r2_score(y_train, train_predictions)
test_r2 = r2_score(y_test, test_predictions)
print(train_r2, test_r2)

#RandomForestRegressor
model = RandomForestRegressor(n_estimators=400, random_state=0)
model.fit(X_train, y_train.ravel())  # Flatten y_train to 1D array

# Predict and calculate MAE
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)
train_mae = mean_absolute_error(y_train, train_predictions)
test_mae = mean_absolute_error(y_test, test_predictions)

# Calculate R2 score
train_r2 = r2_score(y_train, train_predictions)
test_r2 = r2_score(y_test, test_predictions)
print("Training Mean Absolute Error (MAE):", train_mae)
print("Testing Mean Absolute Error (MAE):", test_mae)
print("Training R2 Score:", train_r2)
print("Testing R2 Score:", test_r2)

#XGBoost
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.17, random_state=0)
model = XGBRegressor(n_estimators=420, learning_rate=0.05, max_depth=9, random_state=0)
model.fit(X_train, y_train.ravel())  # Flatten y_train to 1D array

# Predict and calculate MAE
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)
train_mae = mean_absolute_error(y_train, train_predictions)
test_mae = mean_absolute_error(y_test, test_predictions)

# Calculate R2 score
train_r2 = r2_score(y_train, train_predictions)
test_r2 = r2_score(y_test, test_predictions)
print("Training Mean Absolute Error (MAE):", train_mae)
print("Testing Mean Absolute Error (MAE):", test_mae)
print("Training R2 Score:", train_r2)
print("Testing R2 Score:", test_r2)

