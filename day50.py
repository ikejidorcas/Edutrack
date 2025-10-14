import os, time, random
def add():
    os.system('cls')
    q2 = input('Enter idea: ')
    a = open('dope.list', '+a')
    a.write(f'{q2}\n')
    a.close()
    print('SUCESSFULY ADDED')
    time.sleep(2)
    os.system('cls')

def show():
    a = open('dope.list', 'r')
    q3 = a.read().split('\n')
    q3.remove('')
    q4 = random.choice(q3)
    print(q4)
    a.close()
    time.sleep(1)
    os.system('cls')
    
    
while True:
    q1 = input('1: Add idea \n2: show random ideas \n>..')
    if q1 == '1':
        add()
    else:
        show()