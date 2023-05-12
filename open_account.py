# open_account

import mysql.connector as sql
con = sql.connect(host='localhost', user='root', passwd='9967639796', database='bank')
cur = con.cursor()

cur.execute('SELECT * FROM account;')
x = cur.fetchall()
if len(x)==0:
    acno = 1000000000
else:
    s = 'SELECT MAX(acno) FROM account;'
    cur.execute(s)
    data = cur.fetchone()
    no = data[0]
    acno = no + 1

print('Your Account Number is: ', acno)
name = input('Enter your name: ')
address = input('Enter your address: ')
phno = int(input('Enter your phone number: '))
if phno < 1000000000 or phno > 9999999999:
    phno = int(input('Please enter a valid phone number: '))
pan = input('Enter your PAN number: ')
if len(pan) != 10:
    pan = input('Please enter a valid PAN number: ')
actype = input('Enter the type of account you wish to open (savings(s)/current(c)): ')
actype = actype.upper()
open_date = input('Enter the date of opening (yyyy-mm-dd): ')
inp = input('How would you like to make the initial deposit? (cheque(ch)/cash(ca)): ')    
inp = inp.upper()
if inp == 'CH':
    cheque_no = int(input('Enter your cheque number (6 digit): '))
    if cheque_no < 100000 or cheque_no > 999999:
        cheque_no = int(input('Please enter a valid cheque number: '))
open_bal = int(input('Enter the opening balance (minimum 1000): '))
if open_bal < 1000:
    open_bal = int(input('Please abide by the minimum balance criteria: '))

if inp == 'CH':
    s = "INSERT INTO account VALUES({},'{}','{}',{},'{}','{}','{}',{},{},NULL);".format(acno, name, address, phno, pan, actype, open_date, cheque_no, open_bal)
else:
    s = "INSERT INTO account VALUES({},'{}','{}',{},'{}','{}','{}',NULL,{},NULL);".format(acno, name, address, phno, pan, actype, open_date, open_bal)

cur.execute(s)
con.commit()

if inp == 'CH': 
    u = "INSERT INTO trans VALUES({}, '{}', 'd', {}, {})".format(acno, open_date, cheque_no, open_bal)
else:
    u = "INSERT INTO trans VALUES({}, '{}', 'd', NULL, {})".format(acno, open_date, open_bal)

cur.execute(u)
con.commit()

print('Account created successfully...')

import account_details
cur.close()
con.close()

        
