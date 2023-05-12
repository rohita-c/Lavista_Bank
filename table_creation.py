# table_creation

import mysql.connector as sql
con = None
cur = None
try:
    msg = 'Error establishing connection with database: '
    con = sql.connect(host='localhost', user='root', passwd='9967639796', database='bank')
    msg = 'Error creating a cursor: '
    cur = con.cursor()
    sent1 = '''CREATE TABLE account(acno BIGINT PRIMARY KEY,
              name VARCHAR(20), address VARCHAR(20), phno BIGINT,
              pan VARCHAR(10), actype VARCHAR(10), open_date DATE,
              cheque_no INT, open_bal BIGINT, close_date DATE);'''
    msg = 'Error creating the accounts table: '
    cur.execute(sent1)
    msg = 'Error committing table into the database: '
    con.commit()
    sent2 = '''CREATE TABLE trans(acno BIGINT, 
               trans_date DATE, dep_type VARCHAR(10), cheque_no INT,
               tot_bal BIGINT, FOREIGN KEY(acno) REFERENCES account(acno));'''
    msg = 'Error creating the transactions table: '
    cur.execute(sent2)
    msg = 'Error committing table into the database: '
    con.commit()
    print('Account and Trans tables created...')
except sql.Error as err:
    print(msg + err.msg)
    if con is not None:
        con.rollback()
finally:
    if cur is not None:
        cur.close()
    if con is  not None:
        con.close()

        
