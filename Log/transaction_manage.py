import psycopg2
from function import * 

conn = connect_database()
log = log.readlines()
i = 5
for i in range(log):
  if log[i] == "\n":
      break

  if commit_pattern(log[i]):
    print("A transação T"+ "Realizou redo")

  if start_CKPT_pattern(log[i]):
    
  if transaction_pattern(log[i]):

  if 