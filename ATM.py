import getpass
import string
import os


users=['user','user2','user3']
pins=['1234','2222','4321']
amounts=[1000,2000,3000]
count=0

while True:
    user=input('\nENTER USER NAME:')
    user=user.lower()
    if user in users:
        if user==users[0]:
            n=0
        elif user==users[1]:
            n=1
        else:
            n=2
        break
    else:
        print('invalid username')
while count<3:
    pin=str(getpass.getpass('please enter pin:'))
    if pin.isdigit():
        if user=='user1':
            if pin==pins[0]:
                break   
            else:
                count+=1
                print('invalid pin')
        if user=='user2':
            if pin==pins[1]:
                break
            else:
                count+=1
                print('invalid pin')
        if user=='user3':
            if pin==pins[2]:
                break
            else:
                count+=1
                print('invalid pin')
    else:
        print('pin consist of 4 digit ')
        count+=1

if count==3:
    print('3 unsuccesful pin attempts,exiting')
    exit()
print('Login Succesful,continue')
print(str.capitalize(users[n]),'Welcome to ATM')
while True:
    response=input('select from following options: \nstatement_(S) \nwithdraw_(W) \nlodgement_(L) \nchange pin_(P) \nQuit_(Q) \n: ').lower() 
    valid_response=['s','w','l','p','q']
    response=response.lower()
    if response=='s':
        print(str.capitalize(users[n]),'you have',amounts[n],'rupees of your account.')
    elif response=='w':
        cash_out=int(input('enter you would like to withdraw: '))
        if cash_out%10 !=0:
            print("amount you want to withdraw must to match 10 rupees notes")
        elif cash_out>amounts[n]:
            print('you have insufficient balance')
        else:
            amounts[n]=amounts[n]-cash_out
            print('your new balance is :',amounts[n],'rupee')
    elif response=='1':
        cash_in=int(input('enter amount you want to lodge: '))
        if cash_in%10 !=0:
            print('amount you want to lodge must to match 10 rupees notes')
        else:
            amounts[n]=amounts[n]+cash_in
            print('your new balance is: ',amounts[n],'rupee')
    elif response=='p':
        new_pin=str(getpass.getpass('enter a new pin: '))
        if new_pin.isdigit() and new_pin !=pins[n] and len(new_pin)==4:
            new_ppin=str(getpass.getpass('conform new pin: '))
            if new_ppin !=new_pin:
                print('pin mismatch') 
            else:
                print('new pin must consist of 4 digits \nand muist be differance to previous pin')
        elif response=='q':
            exit()
        else:
            print('response not valid')
        


        


