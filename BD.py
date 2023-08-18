import sqlite3


conn = sqlite3.connect("Todoliste.db")
cur = conn.cursor()
#req = "CREATE TABLE Todo (id integer PRIMARY KEY AUTOINCREMENT,tache text,v	boolean,T boolean)"
req = "UPDATE Todo SET T=true WHERE id=6"
cur.execute(req)
conn.commit()
conn.close()

'''''
conn = sqlite3.connect("Todoliste.db")
cur = conn.cursor()
req = "select*from Todo"
result = cur.execute(req)

for row in result:
    print(row[0], row[1])
cur.execute(req)
conn.commit()
conn.close()
'''''