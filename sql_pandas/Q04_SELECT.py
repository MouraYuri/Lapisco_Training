import mysql.connector as bdCon

cnx = bdCon.connect(user='root', password='admin', database='lapisco_training')

cursor = cnx.cursor(buffered=True)

querie = "SELECT * FROM tbAtor ORDER BY nome_ator ASC"

cursor.execute(querie)
print(cursor.fetchall())


cursor.close()
cnx.close()