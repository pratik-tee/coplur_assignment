import sqlite3
conn=sqlite3.connect("db2.db")

conn.execute('''
             INSERT INTO tableC(Employee_name,phone_no,department)VALUES("avinash","987465","IT"),("prakash","64684894","Manufacture"),("vikash","6864
             85","transporti")
             ''')
conn.commit()

data=conn.execute("Select * FROM tableA")
for x in data:
     print(x)
conn.close()