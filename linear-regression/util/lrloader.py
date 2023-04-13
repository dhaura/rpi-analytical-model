import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import joblib


def load_and_predict(dataset_path, X, y, version, normalize):
    # Load the dataset
    df = pd.read_csv('../data/' + dataset_path)

    # Load the model
    loaded_model = joblib.load('../models/analytical-model-lr-' + version + '.joblib')

    if normalize:
        # create a MinMaxScaler object
        scaler = MinMaxScaler()

        # normalize the independent variables
        normalized_df = scaler.fit_transform(df.iloc[:, :-1])

        X_normalized = scaler.transform(X)

        # Make predictions
        y_pred = loaded_model.predict(X_normalized)
    else:
        y_pred = loaded_model.predict(X)

    print("Sample Input: ", X)
    print("Actual Power: ", y)
    print("Predicted Power: ", y_pred[0])
    print()

    return y_pred
