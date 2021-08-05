from function import *

conn = connect_database()
redo = []
# conn.commit()
# cur.close()
try:
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
            # print(rows)
            dataLog = ""
            if log[save][6] == 'A':
                dataLog = log[save][8] + log[save][9]
                if rows[0][1] != dataLog:
                    cur.execute("update dados set a = %s where id = %s"), (dataLog, log[save][4])
                    dataLog = log[save][1] + log[save][2]
                    redo.append(dataLog)
            else: # B
                dataLog = log[save][8] + log[save][9]
                if rows[0][2] != dataLog:
                    cur.execute("update dados set b = %s where id = %s"), (dataLog, log[save][4])
                    dataLog = log[save][1] + log[save][2]
                    redo.append(dataLog)   
        
        save+=1

except psycopg2.DatabaseError as error:
    print(error)
    exit()

print(redo)
truncate_data(cur, conn)
close_database(conn)

