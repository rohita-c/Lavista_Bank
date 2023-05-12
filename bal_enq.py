# bal_enq

import mysql.connector as sql
con = sql.connect(host='localhost', user='root', passwd='9967639796', database='bank')
cur = con.cursor()

acno = int(input('Enter the account number whose balance you require: '))
s = 'SELECT acno FROM trans;'
cur.execute(s)
data = cur.fetchall()
count=0
for i in data:
    if i[0] != acno:
        count += 1
if count==len(data):
    acno = int(input('The enter account number is not available in the database...\nPlease enter a valid account number: '))

t = 'SELECT * FROM account WHERE acno = {};'.format(acno)
cur.execute(t)
data = cur.fetchall()
for d in data:
    print("\nAccount number:", d[0])
    print("Name:", d[1])
    print("Address:", d[2])
    print("Phone number:", d[3])
    print("PAN number:", d[4])
    print("Account opened on:", d[6])
    print("Opening balance: Rs.", d[8])
    if d[9] is not None:
        print("Account closed on:", d[9])
    

q = "SELECT * FROM trans WHERE acno = {};".format(acno)
cur.execute(q)
data = cur.fetchall()

for d in data:
    print("Date of latest transaction:", d[1])
    if d[3] is not None:
        print("Cheque number:", d[3])
    print("Balance remaining:", d[4])
    
import menu
cur.close()
con.close()
