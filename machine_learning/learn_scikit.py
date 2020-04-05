import numpy as np 
from sklearn.linear_model import Perceptron
from sklearn import datasets
from matplotlib import pyplot as plt

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[0],[0],[1]])

pc = Perceptron(tol=1e-3)

irisDataset = datasets.load_iris()
firstClass = np.where(irisDataset.target==0)
secondClass = np.where(irisDataset.target==1)
trainIndexes = np.append(firstClass, secondClass)


'''plt.scatter(irisDataset.data[firstClass,0], irisDataset.data[firstClass,1], color="g")
#plt.scatter(irisDataset.data[secondClass,0], irisDataset.data[secondClass,1], color="b")
plt.show()'''

pc.fit(irisDataset.data[trainIndexes], irisDataset.target[trainIndexes])

print(pc.score(irisDataset.data[trainIndexes], irisDataset.target[trainIndexes]))
