import random
import DatabaseBank as db

while (True):
    
    print ('''Welcome To SINTU RODE LINE BANK
              
              0. Exit
              1. OPEN BANK ACCOUNT
              2. DEPOSIT 
              3. WITHDRAW
              4. CHAHGE NAME
              5. DISPLAY TRANSACTION DETAILS
              6. CLOSE ACCOUNT
              ''')

    choice=int(input('ENTER YOUR CHOICE : '))
    if choice ==0:
        break
    elif choice == 1:
        db.bank_detail()
    elif choice==2:
        db.deposit()
    elif choice==3:
        db.withdraw()
    elif choice==4:
        db.changename()
   
    elif choice==5:
        pass                                         #Can be used to avoid compilation errors
    elif choice==6:
        db.removeaccount()
        
    else:
        print("INVALID")
