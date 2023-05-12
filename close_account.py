# close_account

import mysql.connector as sql
con = sql.connect(host='localhost', user='root', passwd='9967639796', database='bank')
cur = con.cursor()

acno = int(input('Enter the account number whose account is to be closed: '))
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
x = input("\nEnter the date of closing (in yyyy-mm-dd form): ")

s = "UPDATE account SET close_date = '{}' WHERE acno = {};".format(x, acno)
cur.execute(s)
con.commit()
print('Account closed successfully...')

import account_details
cur.close()
con.close()


