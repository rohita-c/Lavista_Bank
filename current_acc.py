# current_acc

import mysql.connector as sql
con = sql.connect(host='localhost', user='root', passwd='9967639796', database='bank')
cur = con.cursor()

r = "SELECT * FROM account WHERE actype = 'c';"
cur.execute(r)
data = cur.fetchall()
print("\n{} CURRENT ACCOUNT(S) AVAILABLE\n".format(cur.rowcount))
for d in data:
    print("\nAccount number:", d[0])
    print("Name:", d[1])
    print("Address:", d[2])
    print("Phone number:", d[3])
    print("PAN number:", d[4])
    print("Account opened on:", d[6])
    if d[7] is not None:
        print("Cheque number:", d[7])
    print("Opening balance: Rs.", d[8])
    if d[9] is not None:
        print("Account closed on:", d[9])

import reports
cur.close()
con.close()


