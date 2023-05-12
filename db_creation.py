# db_creation

import mysql.connector as sql
con = None
cur = None
try:
    msg = 'Error connecting to server: '
    con = sql.connect(host='localhost', user='root', passwd='9967639796')
    msg = 'Error creating a cursor: '
    cur = con.cursor()
    msg = 'Error creating a database: '
    cur.execute('CREATE DATABASE bank;')
    msg = 'Error committing to database: '
    con.commit()
    print('Database created...')
except sql.Error as err:
    print(msg + err.msg)
    if con is not None:
        con.rollback()
finally:
    if cur is not None:
        cur.close()
    if con is not None:
        con.close()

        
