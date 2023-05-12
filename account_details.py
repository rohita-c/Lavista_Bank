# account_details

print('\n', '='*20, 'Account Holder Details', '='*20, '\n')
print('\n1\tOpen Account\n2\tModify Account\n3\tClose Account\n4\tReports\n5\tReturn to Main Menu\n')
ch = int(input('Enter your choice: '))

while ch != 5:
    if ch == 1:
        import open_account
    elif ch == 2:
        import modify_account
    elif ch == 3:
        import close_account
    elif ch == 4:
        import reports
        
import menu


