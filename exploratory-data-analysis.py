import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# global mapping of parameters for plot axes
parameter_map = {'master_cpu_util': "Master CPU \nUtilization (nano cores)",
                 'master_memory_util': "Master Memory \nUtilization (KB)",
                 'num_of_worker_nodes': "Number of Worker Nodes",
                 'num_of_containers': "Number of Containers",
                 'container_cpu_util_sum': "Container CPU \nUtilization Sum (nano cores)",
                 'container_memory_util_sum': "Container Memory \nUtilization Sum (KB)",
                 'power': "Power [W]"
                 }


# Function to plot input parameters against power
def plot_and_save(input_parameter):
    global parameter_map
    plot = sns.pairplot(df, x_vars=[input_parameter], y_vars=['power'], diag_kind='kde')
    plot.set(xlabel=parameter_map[input_parameter], ylabel='Power [W]')
    plt.subplots_adjust(bottom=0.3)
    plt.savefig('figures/eda-' + input_parameter + '.pdf', format='pdf')
    plt.show()


# Load the data into a Pandas dataframe
df = pd.read_csv('data/final-test-data-with-headers.csv')

# Check for missing values and handle them
df.isnull().sum()
df = df.fillna(df.mean())

# Calculate basic statistics
df.describe()

# Retrieve the headers of the csv file
headers = df.columns

# Create visualizations
for header in headers:
    plot_and_save(header)
