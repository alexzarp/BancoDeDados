import psycopg2
import re
log = open("entrada", "r")
log = log.readlines()

def connect_database():
    try:
        conn = psycopg2.connect (
            database = "log",
            user = "postgres",
            password = "741258",
            host = "127.0.0.1",
            port = "5432"
        )
        return conn

    except psycopg2.DatabaseError as error:
        print(error)
        exit()

def close_database(conn):
    if conn is not None:
        conn.close()

def start_pattern(log):
    pattern = r"^<start T[0-9]+>$"
    return bool(re.match(pattern, log))

def transaction_pattern(log):
    pattern = r"^<T[0-9]+,[0-9]+,[A-Z],[0-9]+>$"
    return bool(re.match(pattern, log))

def commit_pattern(log):
    pattern = r"^<commit T[0-9]+>$"
    return bool(re.match(pattern, log))

def start_CKPT_pattern(log):
    pattern = r"^<Start CKPT"
    return bool(re.match(pattern, log))

def end_CKPT_pattern(log):
    pattern = r"^<End CKPT>$"
    return bool(re.match(pattern, log))

def number_pattern(log):
    pattern = r"[0-9]"
    return bool(re.match(pattern, log))

#a minha ideia era mais ou menos essa 
def find_commit(log):   
    commit_catch = [] #declara uma lista vazia pra pegar os commits
    for i in range(len(log)):
        found = log[i].find('Commit') #procura dentro do arquivo as referencias a commit e coloca dentro da variavel (não sei se precisa e também não sei como pegar exatamente a transação)
        #precisa de um jeito de retornar o nome da transação, o find só retorna -1 caso ele ache a string
        #provavelmente com o pattern é possivel
        commit_catch.append(found) #insere os elementos achados na lista 
        
        if end_CKPT_pattern(log) == True: #não tenho certeza quanto a essa condição, pode-se pensar em outro ponto de parada, pq se tiver mais que um checkpoint já azedou
            break

def truncate_data(cur, conn):
    cur = conn.cursor()
    cur.execute("truncate table dados")
    conn.commit()
    
    i = 0
    while(log[i][0] != 'B'):
        number = ''
        data = []
        if log[i][0] == 'A':
            j = 4
            while(log[i][j] != '\n'):
                if number_pattern(log[i][j]):
                    number = number + log[i][j]
                j+=1
            data.append(log[i][2])
            data.append(number)
            number = ''

            k = 0
            while(log[k][0] != '\n'):
                if log[k][0] == 'B' and data[0] == log[k][2]:
                    j = 4
                    while(log[k][j] != '\n'):
                        if number_pattern(log[k][j]):
                            number = number + log[k][j]
                        j+=1
                    data.append(number)
                    cur.execute("insert into dados values (%s, %s, %s)", (data[0], data[1], data[2]))
                    conn.commit()
                    break
                    
                
                k+=1
        i+=1

    cur.close()

# INSERT INTO films (code, title, did, date_prod, kind)
#     VALUES ('T_601', 'Yojimbo', 106, DEFAULT, 'Drama');