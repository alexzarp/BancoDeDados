from function import *

conn = connect_database()
cur = conn.cursor()
cur.execute("truncate table dados")

# coluna | id | valor
# animals.append('guinea pig')
data = []
# desconsiderei id com mais de 1 dígito, e dado com mais/menos de 2 dígitos na hora do carregamento 
for i in range(True):
    number_complete = ''
    if log[i] == '\n':
        print('ola')
        break
    number_complete = number_complete + log[i][4] + log[i][5]
    data.append([log[i][0], log[i][2], number_complete])
    reg = i
    for reg in range(True):
        reg+=1
        if (log[reg][0] == log[i][0] and log[reg][2] == log[i][2]):
            number_complete = number_complete + log[reg][4] + log[reg][5]
            data.append([log[i][0], log[i][2], number_complete])

    
print(data)
# print(log)


cur.close()
close_database(conn)
