# 1-  Qual o tempo de execução na inserção de 10000 tuplas com o autocommit True e False?
# Explique o que aconteceu. OBS: rodar 5 vezes e fazer a média e desvio padrão dos tempos de execução

# 2- Abra dois terminais e execute, ao mesmo tempo,  o código da questão anterior com o  autocommit False. 
# Além disso, setar o nível de isolamento SERIALIZABLE. Reportem o tempo (5 execuções com o desvio padrão).
# Explique o que acontece na prática neste caso? 

import psycopg2
from psycopg2 import extensions
import time
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

    # n = int(input("Quantas inserções fazer? "))

    conn.autocommit = False

    cur = conn.cursor()
    starttime = time.time() # time
    data = 100000
    for i in range(100000):
        # id = int(input("Qual o id desta pessoa? "))
        # nome = str(input("Qual o nome desta pessoa? "))
        # cpf = int(input("Qual seu CPF? "))
        # ender = str(input("O logradouro? "))
        psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE
        cur.execute("insert into cliente values (%s, %s, %s, %s)", (data, "Alessandro Souza", 5455445, "Rua dos caídos"))
        data+=1
        # vetor.append([id, nome, cpf, ender])
    conn.commit()
    cur.close()

    print("time is ", (time.time() - starttime)) # time

    # cur = conn.cursor()
    # cur.execute("truncate table cliente")
    # conn.commit()
    # cur = conn.cursor()
    # cur.execute("select * from cliente")
    # rows = cur.fetchall()
    # cur.execute("select count(*) from cliente")
    # count = cur.fetchall()
    # count = count[0][0]
    # cur.close()
    
    # print("A tabela escontra-se da seguinte forma:\n")
    # print("═════════════════════════════════")
    # for i in range(count):
    #     print("Tupla ", i)
    #     print("id: ", rows[i][0])
    #     print("Nome: ", rows[i][1])
    #     print("CPF: ", rows[i][2])
    #     print("Logradouro: ", rows[i][3])
    #     print("═════════════════════════════════") 

except psycopg2.errors.lookup("23505"):
    print("O id", id,"não pode ser inserido pois já existe")
    print("Todas as inserções foram canceladas!")

except psycopg2.DatabaseError as error:
    print(error)

finally:
    if conn is not None:
        conn.close()