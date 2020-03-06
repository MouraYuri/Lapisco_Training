import mysql.connector as bdCon

cnx = bdCon.connect(user='root', password='admin', database='lapisco_training')

cursor = cnx.cursor(buffered=True)

querie = "SELECT nome_ator FROM tbAtor WHERE cidade_ator LIKE 'M%'"

cursor.execute(querie)
print(cursor.fetchall())


cursor.close()
cnx.close()