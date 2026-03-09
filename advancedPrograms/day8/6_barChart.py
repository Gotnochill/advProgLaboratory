import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students.csv')

plt.bar(df['Name'] , df['Age'])
plt.xlabel('Students Name')
plt.ylabel('Age')
plt.title('Students Age chart')
plt.show()