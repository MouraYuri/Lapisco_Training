wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names

> virginica.txt
cat iris.data | grep -e "Iris-virginica" | sort -t',' >> virginica.txt

> versicolor.txt
cat iris.data | grep -e "Iris-versicolor" | sort -t',' >> versicolor.txt

> setosa.txt
cat iris.data| grep -e "Iris-setosa" | sort -t',' >> setosa.txt

