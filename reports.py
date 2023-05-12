# reports

import mysql.connector as sql
con = sql.connect(host='localhost', user='root', passwd='9967639796', database='bank')
cur = con.cursor()

print('\n', '='*20, 'Reports', '='*20, '\n')
print('\n1\tSavings Accounts\n2\tCurrent Accounts\n3\tReturn to Account Holder Details\n')
ch = int(input('Enter your choice: '))

while ch != 3:
    if ch == 1:
        import savings_acc

    elif ch == 2:
        import current_acc

import account_details
cur.close()
con.close()



