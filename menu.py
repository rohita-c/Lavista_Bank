# menu

import sys
print('\n', '~'*20, ' Lavista Bank Welcomes You', '~'*20, '\n')
print('\n1\tAccount Holder Details\n2\tTransaction Details\n3\tBalance Enquiry\n4\tExit\n')
ch = int(input('Enter your choice: '))
while ch != 4:
    if ch == 1:
        import account_details
    elif ch == 2:
        import transac
    elif ch == 3:
        import bal_enq
sys.exit()



