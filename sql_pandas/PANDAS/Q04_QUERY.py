import pandas as pd 
import numpy as np 



df = pd.read_csv('./sql_pandas/PANDAS/dataset/titanic.csv')

indexes1 = np.where(df.loc[:,'Age'] <= 18)

indexes2 = np.where(df.loc[:,'Age'] > 18)
indexes3 = np.where(df.loc[:,'Age'] > 65)


idx = indexes1 + tuple([[4 for x in range(len(indexes1[0]))]])
print(df.iloc[idx])

#df.iloc[np.where(df.loc[:,'Age']<=18)] = "Criança"
#df.iloc[indexes] = "Criança"


#print('result',result)
