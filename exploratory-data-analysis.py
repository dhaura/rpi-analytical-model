import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into a Pandas dataframe
df = pd.read_csv('data/final-test-data-with-headers.csv')

# Check data types and convert if necessary
df.dtypes

# Check for missing values and handle them
df.isnull().sum()
df = df.fillna(df.mean())

# Calculate basic statistics
df.describe()

# Create visualizations
sns.pairplot(df)
sns.heatmap(df.corr(), annot=True)
plt.hist(df['power'], bins=10)
plt.savefig('figures/analytical-model-data-analysis.pdf', format='pdf')
plt.show()