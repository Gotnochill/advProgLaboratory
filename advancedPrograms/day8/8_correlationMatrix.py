import pandas as pd

df = pd.read_csv('students.csv')

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include='number')
corr_matrix = numeric_df.corr()

print("Correlation matrix:")
print(corr_matrix)