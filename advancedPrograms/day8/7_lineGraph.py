import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students.csv')

plt.plot(df['Name'], df['Age'], marker='o', label='Age')
plt.plot(df['Name'], df['Marks'], marker='s', label='Marks')

plt.xlabel('Student Name')
plt.ylabel('Value')
plt.title('Multi-Line Graph: Age and Marks')
plt.legend()
plt.grid(True)
plt.show()