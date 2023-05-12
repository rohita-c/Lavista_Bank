# modify_account

import mysql.connector as sql
con = sql.connect(host='localhost', user='root', passwd='9967639796', database='bank')
cur = con.cursor()

acno = int(input('Enter the account number whose details are to be modified: '))
s = 'SELECT acno FROM account;'
cur.execute(s)
data = cur.fetchall()
count=0
for i in data:
    if i[0] != acno:
        count += 1
if count==len(data):
    acno = int(input('The enter account number is not available in the database...\nPlease enter a valid account number: '))

q = "SELECT * FROM account WHERE acno = {};".format(acno)
cur.execute(q)
data = cur.fetchone()
print("Your name is:", data[1])
print("Your address is:", data[2])
print("Your phone number is:", data[3])
print("Your PAN number is:", data[4])
print("Your account type is:", data[5])
print("You opened the account on:", data[6])
print("Your balance at the time of opening was: Rs.", data[8])

a = input('Do you wish to modify your name (yes(y)/no(n)): ')
a = a.upper()
if a == 'Y':
    name = input('Enter the modified name: ')
    a1 = "UPDATE account SET name = '{}' WHERE acno = {};".format(name, acno)
    cur.execute(a1)
    con.commit()

b = input('Do you wish to modify your address (yes(y)/no(n)): ')
b = b.upper()
if b == 'Y':
    address = input('Enter the modified address: ')
    b1 = "UPDATE account SET address = '{}' WHERE acno = {};".format(address, acno)
    cur.execute(b1)
    con.commit()

c = input('Do you wish to modify your phone number (yes(y)/no(n)): ')
c = c.upper()
if c == 'Y':
    phno = int(input('Enter your modified phone number: '))
    if phno < 1000000000 or phno > 9999999999:
        phno = int(input('Please enter a valid phone number: '))
    c1 = "UPDATE account SET phno = {} WHERE acno = {};".format(phno, acno)
    cur.execute(c1)
    con.commit()

d = input('Do you wish to modify your account type (yes(y)/no(n)): ')
d = d.upper()
if d == 'Y':
    actype = input('Enter the modified account type (savings(s)/current(c)): ')
    d1 = "UPDATE account SET actype = '{}' WHERE acno = {};".format(actype, acno)
    cur.execute(d1)
    con.commit()

print('Details modified successfully...')

import account_details
cur.close()
con.close()

