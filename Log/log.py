from function import *

conn = connect_database()
cur = conn.cursor()



truncate_data(cur, conn)
cur.close()
close_database(conn)
