# 8. Read a CSV using pandas and print the first 5 rows
import pandas as pd
df = pd.read_csv("students.csv")
print(df.head())
