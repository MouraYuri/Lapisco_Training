import mysql.connector as dbCon #Database connection
from datetime import date, time

#this command establish the connection with mySql database
cnx = dbCon.connect(user='root', database='lapisco_training', password='admin')


#To use DDL you need to define an object called cursor
cursor = cnx.cursor()



''' 
Adding registers to tbNovelas 

add_novela = ("INSERT INTO tbNovela (codigo_novela, nome_novela, data_primeiro_capitulo, data_ultimo_capitulo, horario_exibicao) VALUES (%s,%s,%s,%s,%s)")

add_novela_args1 = (0, "Todo mundo vai morrer",date(2020, 3, 4), date(2020,12,17), time(16,30))
add_novela_args2 = (1,"Shoraste:",date(2019, 7, 15), date(2020,8,17), time(18,30))
add_novela_args3 = (2,"Elon Musk e o Agiota",date(2010, 3, 26), date(2022,1,3), time(22,00))


cursor.execute(add_novela, add_novela_args1)
cursor.execute(add_novela, add_novela_args2)
cursor.execute(add_novela, add_novela_args3)
'''

'''
Adding registers to tbAtor

add_tbAtor = ("INSERT INTO tbAtor (codigo_ator, nome_ator, idade, cidade_ator, salario_ator, sexo_ator) VALUES (%s,%s,%s,%s,%s,%s)")

add_tbAtor_args1 = (10,"Mc gorilla", 26,"Itapiúna", 26650.75, "H")
add_tbAtor_args2 = (11,"Donald Trump", 91,"Quixadá", 106.50, "H")
add_tbAtor_args3 = (12,"Ada Lovelace", 24,"Bom Jardim", 12764.78, "M")

cursor.execute(add_tbAtor, add_tbAtor_args1)
cursor.execute(add_tbAtor, add_tbAtor_args2)
cursor.execute(add_tbAtor, add_tbAtor_args3)
'''

'''
Adding registers to tbCapitulo

add_tbCapitulo = ("INSERT INTO tbCapitulo (codigo_capitulo, nome_capitulo, data_exibicao_capitulo, codigo_novela) VALUES (%s,%s,%s,%s)")

add_tbCapitulo_args1 = (100,"rock lee Vs gaara", date(2020, 4, 14), 0)
add_tbCapitulo_args2 = (101,"A terra é plana", date(2020, 7, 23), 0)
add_tbCapitulo_args3 = (103,"malditos latifundiários", date(2012, 12, 12), 2)

cursor.execute(add_tbCapitulo, add_tbCapitulo_args1)
cursor.execute(add_tbCapitulo, add_tbCapitulo_args2)
cursor.execute(add_tbCapitulo, add_tbCapitulo_args3)
'''

'''
Adding registers to tbPersonagem 

add_tbPersonagem = ("INSERT INTO tbPersonagem (codigo_personagem, nome_personagem, idade_personagem, situacao_fnanceira_personagem, codigo_ator) VALUES (%s,%s,%s,%s,%s)")

add_tbPersonagem_args1 = (400, "Xiao Mi",42,"ruim", 11)
add_tbPersonagem_args2 = (401, "Xin jing ping",57,"Boa", 11)
add_tbPersonagem_args3 = (403, "Batman",32,"Muito Boa", 12)

cursor.execute(add_tbPersonagem, add_tbPersonagem_args1)
cursor.execute(add_tbPersonagem, add_tbPersonagem_args2)
cursor.execute(add_tbPersonagem, add_tbPersonagem_args3)
'''

'''
Adding registers to tbNovelaPersonagem 

add_tbNovelaPersonagem = ("INSERT INTO tbNovelaPersonagem (codigo_personagem, codigo_novela) VALUES (%s,%s)")

add_tbNovelaPersonagem_args1 = (400,0)
add_tbNovelaPersonagem_args2 = (401,2)
add_tbNovelaPersonagem_args3 = (403,1)

cursor.execute(add_tbNovelaPersonagem, add_tbNovelaPersonagem_args1)
cursor.execute(add_tbNovelaPersonagem, add_tbNovelaPersonagem_args2)
cursor.execute(add_tbNovelaPersonagem, add_tbNovelaPersonagem_args3)
'''

#Commit is needed to finish an insert action
cnx.commit()



cursor.close()
cnx.close()