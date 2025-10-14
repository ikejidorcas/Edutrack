import os, time
y1 = []
try:
    u = open('to.do','r')
    w1 = eval(u.read())
    u.close()
except:
    print('oops there is a problem')
def add():
    time.sleep(1)
    os.system('cls')
    p2 = input('Customers name: ')
    print()
    p3 = input('PIZA SIZE(s \ m \ l) \n...:').upper()
    while True:
        try:
            p4 = int(input('Quantity of pizza: ')) 
            break
        except: 
            print(' \033[31m Invalid input please input a whole number 🥰')
        cost = 0
        if p3 == 's':
            cost== 5.98
        elif p3 == 'm':
            cost == 9.99
        else:
            cost = 10.46
        price = p4 * cost
        price = round(price, 2)
        row = [p2, p4, price]
        y1.append(row)

def view():
    s1 = 'CUSTOMERS NAME💕'
    s2 = 'PIZZA QUANTITY'
    s3 = 'PRICE OF PIZZA'
    print(f'{s1:^10} |  {s2:^10}| {s3:^10}')
    for row in y1:
        print(f'{row[0]:^10} {row[1]:^10} {row[2]:^10}')
        time.sleep(1)
while True:
    time.sleep(2)
    os.system('cls')
    p1 = input('1. ADD LIST \n2. VIEW\n ...: ')
    if p1 == '1':
        add()
    else:
        view()
    u = open('to.do','w')
    u.write(str(y1))
    u.close