import sqlite3
con=sqlite3.connect("db2.db")
con.execute('''
             Create table tableC(
                  usid INTEGER PRIMARY KEY AUTOINCREMENT,
                 Employee_name VARCHAR(100),
                 phone_no INT(100),
                 department VARCHAR(50),
                 e_mail VARCHAR(50)
             )
             ''')
con.close()