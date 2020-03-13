#Setosa
counter=`cut setosa.txt -f3 -d"," | paste -sd"+" | bc `

qnt=`wc -l setosa.txt | cut -d' ' -f1`

echo "setosa petal average length ";echo "scale=3;$counter/$qnt" | bc




#Virginica

counter=`cut virginica.txt -f3 -d"," | paste -sd"+" | bc `

qnt=`wc -l virginica.txt | cut -d' ' -f1`

echo "virginica petal average length ";echo "scale=3;$counter/$qnt" | bc





#Versicolor

counter=`cut versicolor.txt -f3 -d"," | paste -sd"+" | bc `

qnt=`wc -l versicolor.txt | cut -d' ' -f1`

echo "versicolor petal average length ";echo "scale=3;$counter/$qnt" | bc


