import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import joblib

# Load the dataset
df = pd.read_csv('data/final-test-data-with-headers.csv')

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:, -1], test_size=0.2)

# create a MinMaxScaler object
scaler = MinMaxScaler()

# normalize the independent variables
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.fit_transform(X_test)

# Load the model
loaded_model = joblib.load('models/analytical-model-v8.joblib')

# Sample
X_new = [[1187612200.712264,673290.5449273121,2,4,2460314074.985385,311636.2853386947]]
X_new_normalized = scaler.transform(X_new)

# Make predictions
y_new_pred = loaded_model.predict(X_new_normalized)
print(y_new_pred)  # actual = 8.508