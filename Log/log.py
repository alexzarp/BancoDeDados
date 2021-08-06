from function import *

conn = connect_database()
redo = []
# conn.commit()
# cur.close()
try:
    i = 5
    save = 0
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
                    cur.execute("update dados set a = " + str(dataLog) + "where id =" + str(log[save][4]))
                    print("A tupla id =",log[save][4],"coluna a, foi atualizada para o dado:",str(dataLog))
                    dataLog = log[save][1] + log[save][2]
                    redo.append(dataLog)
            else: # B
                dataLog = log[save][8] + log[save][9]
                if rows[0][2] != dataLog:
                    cur.execute("update dados set b = " + str(dataLog) + "where id =" + str(log[save][4]))
                    print("A tupla id =",log[save][4],"coluna b, foi atualizada para o dado:",str(dataLog))
                    dataLog = log[save][1] + log[save][2]
                    redo.append(dataLog)   
        
        elif commit_pattern(log[save]):
            conn.commit()

        save+=1

    # cur.close()
except psycopg2.DatabaseError as error:
    print(error)

for i in range(len(log)):
    if start_CKPT_pattern(log[i]):
        index = log[i].find('(')
        # print(log[i].find('trator'))
        dataLog = log[i][index+1] + log[i][index+2]
        for j in range(len(redo)):
            if dataLog == redo[j]:
                # print(dataLog, redo[j])
                index+=3
                print('Transação', redo[j] ,'realizou Redo')
            else:
                # print(dataLog, redo[j])
                index+=3
                print('Transação', redo[j] ,'não realizou Redo')
            
            dataLog = log[i][index+1] + log[i][index+2]

            if (log[i][index] == ')'):
                break
        break

truncate_data(cur, conn)
close_database(conn)

