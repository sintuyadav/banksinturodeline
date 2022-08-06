import random           #to input random num in given num 
import string
from tkinter import N     #to add GUI appliction 
from unicodedata import decimal
import pymysql
from decimal import Decimal
cur = None # temporary memory
conn = None # to connect python and database

def creating_data():
    global cur,conn   # Global declareation 
    try:         # Exception handeling

        conn = pymysql.connect(port=3306,
                                user = 'root',
                                database = 'sintubank',
                                host = 'localhost',
                                password  ='')
        print ('database connected')
    except:
        print ('database not connected')
    
    cur = conn.cursor()
#db_connect()    # DB conection 

def cursor_close():
    cur.close()

def connection_close():
    conn.close()

def bank_detail():             # input all details name,num,ADnum,add,Email,MiinBal

        creating_data()
        name = input('Enter your name: ')
        adhar = int(input('Enter your Adhaar number: '))
        phone = int(input('Enter your mobile number: '))
        address = input('Enter your address: ')
        email = input('Enter your Email: ')
        number = string.digits
        num=list(number)
        random.shuffle(num)
        account_number="".join(num)
        deposit_amount = Decimal(input('Enter opening balance amount: '))
        withdraw=0
        deposit=0
        n=0
        while(n<=0):
            if deposit_amount>5000:
                print(" ACCOUNT OPENED SUCCESSFULLY ")
                sql1 = f'insert into bank(name,adhar,phone,address,email,account_number,opening_balance) values("{name}",{adhar},{phone},"{address}","{email}",{account_number},{deposit_amount})'
                sql2= f' insert into transaction(opening_balance, withdrawal_amount,balance_amount,name,deposit_amount) values ({deposit_amount},{withdraw},{deposit_amount},"{name}",{deposit})'
                cur.execute(sql1)
                cur.execute(sql2) 
                conn.commit()      #to allow chanf=ge in DB
                cursor_close()
                connection_close()

            else:
                print("MINIMUM OPENING BALANCE AMOUNT IS 5000 ")
                break

            n+=1
               
        
def deposit():
    creating_data()
    tid=int(input("Enter Your Bank Id: "))
    name=input("Enter Your Name: ")
    n=0
    while(n<=0):
        deposit=Decimal(input("enter the amount you want deposit: "))
        if deposit<5000:
            print("MINIMUM AMOUNT TO BE DEPOSITED IS 5000")
            break
        else:
            sql=f'select opening_balance from transaction where name="{name}"'
            cur.execute(sql)
            data=cur.fetchone()
            balance=data[0]+deposit
            
            sql1=f'update transaction set deposit_amount={deposit} where TID={tid}'
            sql2=f'update transaction set balance_amount={balance} where TID={tid}'
            cur.execute(sql1)
            cur.execute(sql2)
            print('AMOUNT SUCCESSFULLY DEPOSITED')
            conn.commit()
            cursor_close()
            connection_close()

        n+=1

    
def withdraw():
    creating_data()
    tid=int(input("enter your bank id: "))
    name=input("enter your name: ")
    n=0
    withdraw=Decimal(input("enter the amount you want withdraw: "))

    sql=f'select deposit_amount from transaction where name="{name}"'
    cur.execute(sql)
    data=cur.fetchone()
    while(n<=0):
        if(data[0]-withdraw)>=5000:
            balance=data[0]-withdraw
            sql1=f'update transaction set balance_amount={balance} where TID={tid}'
            sql2=f'update transaction set withdrawal_amount={withdraw} where TID={tid}'
            print("AMOUNT WITHDRAWL SUCCESSFULLY")
            cur.execute(sql1)
            cur.execute(sql2)
            conn.commit()
            cursor_close()
            connection_close()
            
        else:
            print("MINIMUM AMOUNT TO BE MAINTAINED IN ACCOUNT IS 5000")
            break
        n+=1

def changename():
    tid=int(input("enter your transaction id: "))
    id=int(input("enter your bank id: "))
    name=input("enter the new name you want to update: ")
    creating_data()
    try:
        sql1=f'update transaction set name="{name}" where TID={tid}'
        sql2=f'update bank set name="{name}" where ID={id}'
        print("OWNER NAME CHANGED SUCCESSFULLY")
    except:
        print("NAME NOT CHANGED")
    cur.execute(sql1)
    cur.execute(sql2)
    conn.commit()
    cursor_close()
    connection_close()

def transdetail():
    tid=int(input("enter your transaction id: "))
    creating_data()

    sql=f"select name, deposit_amount,withdrawal_amount, balance_amount  from transaction where TID={tid}"
    cur.execute(sql)
    record=cur.fetchone()
    for data in record:
        #print(data)
        print(data[0])
        

        '''
        output=f'name={data[0]}\n Depositamount={data[1]}\nWithdrawalamount={data[2]}\nBalanceamount={data[3]}'
        print(output)
        #print(data)
    #print(record)
       '''
#transdetail()


def removeaccount():
    tid=int(input("enter your transaction id to remove: "))
    id=int(input("enter your bank id: "))
    creating_data()
    
    sql=f'delete from transaction where TID={tid}'
    sql2=f'delete from bank where ID={id}'
    

    cur.execute(sql)
    cur.execute(sql2)
    conn.commit()
    print("ACCOUNT IS REMOVED PERMANENTLY")
    cursor_close()
    connection_close()
