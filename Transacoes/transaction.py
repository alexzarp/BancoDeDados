# Construa uma aplicação em uma linguagem de programação capaz de executar N inserções usando uma transação
# na tabela “Cliente”. A aplicação deve ser capaz também de listar a tabela após as inserções. 
# Trate a exceção no caso  de uma inserção de uma chave já existente. 
import psycopg2
conn = None
try:
    conn = psycopg2.connect(
        database="atividade",
        user = "postgres",
        password = "741258",
        host = "127.0.0.1",
        port = "5432"
    )

    n = int(input("Quantas inserções fazer? "))
    vetor = []
    for i in range(n):
        id = int(input("Qual o id desta pessoa? "))
        nome = str(input("Qual o nome desta pessoa? "))
        cpf = int(input("Qual seu CPF? "))
        ender = str(input("O logradouro? "))
        vetor.append([id, nome, cpf, ender])

    cur = conn.cursor()
    for i in range(n):
        id = vetor[i][0]
        nome = vetor[i][1]
        cpf = vetor[i][2]
        ender = vetor[i][3]
        cur.execute("insert into cliente values (%s, %s, %s, %s)", (id, nome, cpf, ender))
    conn.commit()
    cur.close()

except psycopg2.DatabaseError as error:
    print(error)

finally:
    if conn is not None:
        conn.close()