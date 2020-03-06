import pandas as pd 
import numpy as np 

#reading a csv file
df = pd.read_csv('./sql_pandas/PANDAS/dataset/titanic.csv')

print(df.query('Age > 27 & Survived == 1'))
print(len(df.query('Age > 27 & Survived == 1')), "Survived and had more than 27 years old")