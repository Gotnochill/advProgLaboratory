import pandas as pd

df = pd.read_csv('students.csv')

filtered_df = df[ (df['Grade'] == 'A') | (df['Grade'] == 'O') ]
print(filtered_df)