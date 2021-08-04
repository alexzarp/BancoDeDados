from function import *

conn = connect_database()
redo = []
try:
    
# conn.commit()
# cur.close()
    i = 5
    save = i
    while(log[i] != '\n'): # tudo isso aqui (eu testei) pra achar o <start T3>
        if start_CKPT_pattern(log[i]):
            transaction = log[i][13]
            save = i
            i = 5
            while(True):
                if (log[i][7] == 'T' and log[i][8] == transaction):
                    save = i
                    break
                i+=1
            break
        i+=1

    while(log[save] != '\n'):
        if start_pattern(log[save]):
            cur = conn.cursor()

        elif transaction_pattern(log[save]):
            cur.execute("select * from dados where id = %s", (log[save][4]))
            rows = cur.fetchall()
            
        save+=1

except psycopg2.DatabaseError as error:
    print(error)
    exit()

truncate_data(cur, conn)
close_database(conn)

