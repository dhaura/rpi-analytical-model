import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import joblib

# create a MinMaxScaler object
scaler = MinMaxScaler()

# Load the dataset
df = pd.read_csv('../data/final-test-data-with-headers.csv')

# normalize the independent variables
normalized_df = scaler.fit_transform(df.iloc[:, :-1])

# Load the model
loaded_model = joblib.load('../models/analytical-model-v8.joblib')

# Sample
X_new = [[1187612200.712264, 673290.5449273121, 2, 4, 2460314074.985385, 311636.2853386947]]
X_new_normalized = scaler.transform(X_new)

# Make predictions
y_new_pred = loaded_model.predict(X_new_normalized)
print(y_new_pred)  # actual = 8.508
