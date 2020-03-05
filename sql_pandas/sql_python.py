import mysql.connector as dbCon #Database connection
from datetime import date, time


cnx = dbCon.connect(user='root', database='lapisco_training', password='admin')
cursor = cnx.cursor()


add_novela = ("INSERT INTO tbNovela (codigo_novela, nome_novela, data_primeiro_capitulo, data_ultimo_capitulo, horario_exibicao)" +
"VALUES (%s,%s,%s,%s,%s)")

add_novela_args = (0, "O caralho de asa",date(2020, 3, 4), date(2020,12,17), time(16,30))

cursor.execute(add_novela, add_novela_args)


cursor.close()
cnx.close()