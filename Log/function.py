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

def num_pattern(num):
   pattern = r"[0-9]"
   return bool(re.match(pattern, num))

# def num_complete(i):
#     number_complete = ""
#     number = 4
#     while(True):
#         if num_pattern(log[i][number]):
#             number_complete += log[i][number]
#         else:
#             break
#         number+=1
#     return num_complete