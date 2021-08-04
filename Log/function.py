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

def truncate_data(cur, conn):
    cur.execute("truncate table dados")
    i = 0
    while (True):
        dadoA = ''
        dadoB = ''
        dadoA = dadoA + log[i][4] + log[i][5]
        dadoB = dadoB + log[i+2][4] + log[i+2][5]
        cur.execute("insert into dados values (%s, %s, %s)", (log[i][2], dadoA, dadoB))
        conn.commit()
        if log[i+3] == '\n':
            break
        i+=1