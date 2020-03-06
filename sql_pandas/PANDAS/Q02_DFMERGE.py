import pandas as pd 
import numpy as np 

'''
Question:
Faça um merge de dois dataframes e crie uma nova coluna para indicar a que dataframe pertence
cada linha.

-Pela questão podemos inferir que será necessário fazer o uso da função pd.merge() usando um how='outer';
    outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
'''

def merge(df1, df2):
    #getting the index of df1 and df2
    indexDf1,indexDf2 = df1.index,df2.index

    #merging the dataframes
    result = pd.merge(df1,df2, left_index=True, right_index=True, how='outer')

    #finding where the row came from
    came_from = []
    for x in result.index:
        if x in indexDf2 and x in indexDf1:
            came_from.append('both')
            continue
        if x in indexDf1:
            came_from.append('left')
            continue
        else: came_from.append('right')

    #adding a new column with the search results
    result = result.assign(came_from = came_from)
    return result

#Creating dataframe 1 and dataframe 2
df1, df2 = [[1,2,3,'z0'],[4,5,6,'z1']], [['a','b','c'],['d','e','f']]
df1,df2 = pd.DataFrame(df1, index=[0,2]),pd.DataFrame(df2, index=[0,3])


result = merge(df1, df2)
print('result',result)