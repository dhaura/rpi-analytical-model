import csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import joblib
from matplotlib import pyplot as plt


def train_model(dataset_path, X_sample, y_sample, version, normalize):

    # Load the dataset
    df = pd.read_csv('../data/' + dataset_path)

    if normalize:
        # create a MinMaxScaler object
        scaler = MinMaxScaler()

        # normalize the independent variables
        normalized_df = scaler.fit_transform(df.iloc[:, :-1])

        # Split the dataset into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(normalized_df, df.iloc[:, -1], test_size=0.2)
    else:
        # Split the dataset into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:, -1], test_size=0.2)

    # Fit the linear regression model to the training data
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = regressor.predict(X_test)

    # Evaluate the model's performance
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    with open('../models/metrics/analytical-model-lr-' + version + '-metrics.csv', 'w', newline='') as metrics_file:
        csv_writer = csv.writer(metrics_file)
        csv_writer.writerow(['MAE', mae])
        csv_writer.writerow(['MSE', mse])
        csv_writer.writerow(['R-squared', r2])

        print("MAE:", mae)
        print("MSE:", mse)
        print("R-squared:", r2)
        print()

    # Retrieve trained coefficients
    coefficients = regressor.coef_

    # Retrieve trained constant coefficient of the bias term
    intercept = regressor.intercept_

    coefficients_list = list(coefficients)
    coefficients_list.insert(0, intercept)

    with open('../models/coefficients/analytical-model-lr-' + version + '-coefficients.csv', 'w', newline='') as coefficients_file:
        csv_writer = csv.writer(coefficients_file)
        print("Coefficients: ")
        for i in range(len(coefficients_list)):
            csv_writer.writerow(["C" + str(i + 1), coefficients_list[i]])
            print("C" + str(i + 1) + ": ", coefficients_list[i])
        print()

    # Sample testing
    if normalize:
        X_sample_normalized = scaler.transform(X_sample)

        # Make predictions
        y_sample_pred = regressor.predict(X_sample_normalized)
    else:
        # Make predictions
        y_sample_pred = regressor.predict(X_sample)

    print("Sample Input: ", X_sample)
    print("Actual Power: ", y_sample)
    print("Predicted Power: ", y_sample_pred[0])
    print()

    # Save the model
    joblib.dump(regressor, '../models/analytical-model-lr-' + version + '.joblib')

    # Plot the predicted values against the actual values
    plot_and_save(y_test, y_pred, version)


# Function to plot the predicted values against the actual values
def plot_and_save(y_test, y_pred, version):

    plt.scatter(y_test, y_pred, color='blue')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='green', linewidth=2, label='y=x')
    plt.title('Actual vs. Predicted Values')
    plt.xlabel('Actual Power Consumption')
    plt.ylabel('Predicted Power Consumption')
    plt.savefig('../figures/actual-vs-predictions/lr-' + version + '.pdf', format='pdf')
    plt.show()
