import os, time
items = []
try:
    w = open('item.rsg', 'r')
    w1 = eval(w.read())
    w.close()
except:
    pass
def additem():
    time.sleep(1)
    os.system('cls')
    print()
    print('\033[95m ITEMS BOX🎁🎁')
    print('============ \033[0m')
    a1 = input('what item would you like to add: ')
    items.append(a1)

    
def removeitem():
    time.sleep(1)
    os.system('cls')
    print()
    print('\033[95m ITEMS BOX🎁🎁')
    print('============ \033[0m')
    a1 = input('what item would you like to remove: ')
    if a1 in items:
        items.remove(a1)

    
def viewitems():
    print()
    print('\033[95m ITEMS BOX🎁🎁')
    print('============ \033[0m')
    q2 = set(items)
    for i in q2:
        print(f'{i}  {items.count(i)}')
        time.sleep(2)
while True:
    time.sleep(1)
    os.system('cls')
    print()
    print('\033[95m ITEMS BOX🎁🎁')
    print('============ \033[0m')
    q1 = input('1:Add? \n2:Remove? \n3:View \n...: ')
    if q1 == '1':
        additem()
    elif q1 == '2':
        removeitem()
    else:
        viewitems()
    
    w = open('item.rsg', 'w')
    w.write(str(items))
    w.close()