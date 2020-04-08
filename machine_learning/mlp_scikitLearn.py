import numpy as np 
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn import datasets
from matplotlib import pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from random import randint

idx = randint(0,30)


X = datasets.load_iris().data
y = datasets.load_iris().target

#Hold-out split
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2)

for train_index, test_index in sss.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

mlpc = MLPClassifier(solver="sgd", learning_rate="adaptive", hidden_layer_sizes=(100),tol=1e-5, max_iter=500)

mlpc.fit(X_train, y_train)

print("score => ",mlpc.score(X_test, y_test))

print("predicted => ", mlpc.predict([X_test[idx]]))
print("Real label => ", y_test[idx])