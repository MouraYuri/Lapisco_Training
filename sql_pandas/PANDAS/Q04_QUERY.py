import pandas as pd 
import numpy as np 

df = pd.read_csv('./sql_pandas/PANDAS/dataset/titanic.csv')

criançasIdx = np.where(df.loc[:,'Age'] <= 18)

idosoIdx = np.where(df.loc[:,'Age'] > 65)

for x in criançasIdx: df.loc[x, 'Age'] = "Criança"

for x in range(len(df)):
    if x not in criançasIdx[0] and x not in idosoIdx[0]:
        df.loc[x, 'Age'] = "Adulto"

for x in idosoIdx: df.loc[x, 'Age'] = "Idoso"


with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df.loc[:]['Age'])
