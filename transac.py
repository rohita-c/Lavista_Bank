# transac

import mysql.connector as sql
con = sql.connect(host='localhost', user='root', passwd='9967639796', database='bank')
cur = con.cursor()

print('\n', '='*20, 'Transaction Details', '='*20, '\n')

acno = int(input('Enter the account number where you wish to perform the transaction: '))
s = 'SELECT acno FROM account;'
cur.execute(s)
data = cur.fetchall()
count=0
for i in data:
    if i[0] != acno:
        count += 1
if count==len(data):
    acno = int(input('The enter account number is not available in the database...\nPlease enter a valid account number: '))

trans_date = input('Enter the date of transaction: ')
dep_type = input('Do you wish to deposit or withdraw? (d/w): ')
dep_type = dep_type.lower()

x = 'SELECT tot_bal FROM trans WHERE acno = {};'.format(acno)
cur.execute(x)
info = cur.fetchall()
for i in info:
    tot_bal = i[0]

if dep_type == 'd':
    dep = input('How would you like to make the deposit? (cheque(ch)/cash(ca)): ')    
    dep = dep.upper()
    if dep == 'CH':
        cheque_no = int(input('Enter your cheque number (6 digit): '))
        if cheque_no < 100000 or cheque_no > 999999:
            cheque_no = int(input('Please enter a valid cheque number: '))
    amt = int(input('Enter the amount to be deposited: '))
    tot_bal = tot_bal + amt

else:
    dep = 'XYZ'
    wit = int(input('Enter the amount to be withdrawn: '))
    if wit > tot_bal:
        wit = int(input('Not enough balance in your account... Re-enter the amount: '))
    tot_bal = tot_bal - wit


if dep_type == 'd' and dep == 'CH':
    t = "UPDATE trans SET trans_date = '{}' WHERE acno = {};".format(trans_date, acno)
    cur.execute(t)
    con.commit()
    t = "UPDATE trans SET dep_type = '{}' WHERE acno = {};".format(dep_type, acno)
    cur.execute(t)
    con.commit()
    t = "UPDATE trans SET cheque_no = {} WHERE acno = {};".format(cheque_no, acno)
    cur.execute(t)
    con.commit()
    t = "UPDATE trans SET tot_bal = {} WHERE acno = {};".format(tot_bal, acno)
    cur.execute(t)
    con.commit()

elif (dep_type == 'd' and dep == 'CA') or (dep_type == 'w' and dep == 'XYZ'):
    t = "UPDATE trans SET trans_date = '{}' WHERE acno = {};".format(trans_date, acno)
    cur.execute(t)
    con.commit()
    t = "UPDATE trans SET dep_type = '{}' WHERE acno = {};".format(dep_type, acno)
    cur.execute(t)
    con.commit()
    t = "UPDATE trans SET cheque_no = NULL WHERE acno = {};".format(acno)
    cur.execute(t)
    con.commit()
    t = "UPDATE trans SET tot_bal = {} WHERE acno = {};".format(tot_bal, acno)
    cur.execute(t)
    con.commit()


print('Transaction completed successfully...')

print('\n', '='*20, 'Receipt', '='*20, '\n')
print('Account number:', acno)
print("Date of transaction:", trans_date)
print("Transaction type:", dep_type)
if dep_type == 'd':
    print('Amount deposited:', amt)
else:
    print('Amount withdrawn:', wit)
print("Current balance:", tot_bal)

import menu
cur.close()
con.close()
