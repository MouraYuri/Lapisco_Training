>out.txt
awk '{print length}' names.txt  >> out.txt
paste out.txt names.txt -d',' | sort | cut -d',' -f2

