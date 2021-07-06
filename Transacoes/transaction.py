# Construa uma aplicação em uma linguagem de programação capaz de executar N inserções usando uma transação
# na tabela “Cliente”. A aplicação deve ser capaz também de listar a tabela após as inserções. 
# Trate a exceção no caso  de uma inserção de uma chave já existente. 
import psycopg2
conn = None
id
try:
    conn = psycopg2.connect(
        database = "atividade",
        user = "postgres",
        password = "741258",
        host = "127.0.0.1",
        port = "5432"
    )

    n = int(input("Quantas inserções fazer? "))
    # vetor = []
    
    cur = conn.cursor()
    for i in range(n):
        id = int(input("Qual o id desta pessoa? "))
        nome = str(input("Qual o nome desta pessoa? "))
        cpf = int(input("Qual seu CPF? "))
        ender = str(input("O logradouro? "))
        cur.execute("insert into cliente values (%s, %s, %s, %s)", (id, nome, cpf, ender))
        # vetor.append([id, nome, cpf, ender])
    conn.commit()
    cur.close()

    cur = conn.cursor()
    cur.execute("select * from cliente")
    rows = cur.fetchall()
    cur.execute("select count(*) from cliente")
    count = cur.fetchall()
    count = count[0][0]
    cur.close()
    
    print("A tabela escontra-se da seguinte forma:\n")
    print("═════════════════════════════════")
    for i in range(count):
        print("Tupla ", i)
        print("id: ", rows[i][0])
        print("Nome: ", rows[i][1])
        print("CPF: ", rows[i][2])
        print("Logradouro: ", rows[i][3])
        print("═════════════════════════════════") 

except psycopg2.errors.lookup("23505"):
    print("O id", id,"não pode ser inserido pois já existe")
    print("Todas as inserções foram canceladas!")

except psycopg2.DatabaseError as error:
    print(error)

finally:
    if conn is not None:
        conn.close()