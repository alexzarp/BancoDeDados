from function import *

conn = connect_database()
cur = conn.cursor()
cur.execute("truncate table dados")

# coluna | id | valor
# animals.append('guinea pig')
data = []
# nesse momento para simplicar, desconsiderei que o id tivesse mais de 1 dígito
for i in range(True):
    n = 1

    number_complete = ""
    number = 4
    while(True):
        if num_pattern(log[i][number]):
            number_complete += log[i][number]
        else:
            break
        number+=1

    data.append([log[i][0], log[i][2], number_complete])

    for n in range(True):
        if(data[i][0] == log[n][0]):
            data.append([log[n][0], log[n][2], number_complete])
            continue
        else:
            data.append([log[n][0], log[n][2], number_complete])
            break

    if log[i][0] != log[i+1][0]:
        break
    # else:
    #     break
    
print(data)


cur.close()
close_database(conn)
