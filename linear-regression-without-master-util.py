import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import joblib

import matplotlib.pyplot as plt

# create a MinMaxScaler object
scaler = MinMaxScaler()

# Load the dataset
df = pd.read_csv('data/final-test-data-without-master.csv')

# normalize the independent variables
normalized_df = scaler.fit_transform(df.iloc[:, :-1])

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(normalized_df, df.iloc[:, -1], test_size=0.2)

# Fit the linear regression model to the training data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = regressor.predict(X_test)

# Evaluate the model's performance
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))

coefficients = regressor.coef_
print(coefficients)

intercept = regressor.intercept_
print(intercept)

# Sample
X_new = [[2, 4, 2460314074.985385, 311636.2853386947]]
X_new_normalized = scaler.transform(X_new)

# Make predictions
y_new_pred = regressor.predict(X_new_normalized)
print(y_new_pred)  # actual = 8.508

# Save the model
joblib.dump(regressor, 'models/analytical-model-v8-without-master-util.joblib')

# Plot the predicted values against the actual values
plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='green', linewidth=2, label='y=x')
plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Power Consumption')
plt.ylabel('Predicted Power Consumption')
plt.show()
