import os,time,random
from dotenv import load_dotenv
def loginpage():
    time.sleep(1)
    os.system('cls')
    user = input('USER_NAME: ')
    password = input('PASSWORD: ')
   
    keys = load_dotenv('nbv.env')
    if user in keys:
        print('user name does not exist')
        return
    salt = random.randint(1000, 9999)
    newp =f'{password} {salt}'
    newp = hash(newp)
    if load_dotenv[user] == newp:
        print('logged in')
    else: 
        print('user name or password incorrect')

while True:
    menu = input('1. new user \n 2. login \n ..:')
    if menu == '1':
        loginpage()
    else:
        pass
