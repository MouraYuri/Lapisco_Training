import mysql.connector as bdCon

cnx = bdCon.connect(user='root', password='admin', database='lapisco_training')

cursor = cnx.cursor(buffered=True)

querie = "SELECT * FROM tbNovela WHERE horario_exibicao IS NULL"

cursor.execute(querie)
print(cursor.fetchall())


cursor.close()
cnx.close()