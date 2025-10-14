#SECRETES🔥🔥
import os
from dotenv import load_dotenv
load_dotenv('nbv.env')

user1 = os.getenv("USER_NAME1")
password1 = os.getenv("PASSWORD1")
password1= hash(password1)

user2 = os.getenv('USER_NAME2')
password2 = os.getenv("PASSWORD2")

q1 = input('enter user name: ')
q2 = input('enter password: ')
if q1== user1 and q2 == password1:
    print(f'USER_NAME: {user1} and PASSWORD: {password1} \n verified🥰 you are welcome  director.')

elif q1== user2 and q2 == password2:
    print(f'USER_NAME: {user1} and PASSWORD: {password2} \n verified🥰 you are welcome  student.')
else:
    print('invalid input')
