import mysql.connector as bdCon

cnx = bdCon.connect(user='root', password='admin', database='lapisco_training')

cursor = cnx.cursor(buffered=True)

querie = "SELECT a.nome_novela, a.codigo_novela, COUNT(a.codigo_novela) as qnt_capitulos FROM tbNovela a INNER JOIN tbCapitulo b WHERE a.codigo_novela = b.codigo_novela GROUP BY a.codigo_novela"

cursor.execute(querie)
print(cursor.fetchall())


cursor.close()
cnx.close()