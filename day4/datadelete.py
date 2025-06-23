import sqlite3
conn=sqlite3.connect("db2.db")


id=input("select ID to delete")
conn.execute("DELETE FROM tableA where usid="+ id)

conn.commit()
conn.close()