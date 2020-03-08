import pandas as pd 
from matplotlib import pyplot as plt 


df = pd.read_csv('./sql_pandas/PANDAS/dataset/iris.data')

'''
We can verify if the dataset has outliers with boxplots
'''
for x in range(len(df.columns)-1):
    plt.figure()
    plt.boxplot(df.iloc[:,x])


plt.show()
