import pandas as pd 
import numpy as np 


def getHoldOutSets(dataframe, trainPercent, shuffle=False):
    if trainPercent > 1 or trainPercent < 0: return

    if shuffle:
        dataframe = dataframe.sample(frac=1)
    
    ctlr = int(trainPercent*len(dataframe))

    x_train, x_test  = dataframe.iloc[:ctlr,:-1],dataframe.iloc[ctlr-1:,:-1]
    
    y_train, y_test = dataframe.iloc[:ctlr,-1],dataframe.iloc[ctlr-1:,-1]

    return x_train, x_test, y_train, y_test
    

df = pd.read_csv('./sql_pandas/PANDAS/dataset/iris.data')


x_train, x_test, y_train, y_test = getHoldOutSets(df, 0.8)