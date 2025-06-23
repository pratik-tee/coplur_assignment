import sqlite3
conn=sqlite3.connect("db2.db")
conn.execute("UPDATE tableA set usname='XYZ' where usid=4")
conn.commit()
conn.close()