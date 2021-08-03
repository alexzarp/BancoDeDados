from function import *

conn = connect_database()
cur = conn.cursor()

i = transaction_pattern(log[6])
print(i)
i = commit_pattern(log[9])
print(i)
i = start_CKPT_pattern(log[16])
print(i)

truncate_data(cur, conn)
cur.close()
close_database(conn)