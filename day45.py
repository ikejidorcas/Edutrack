import os, time
list= []

def add():
    time.sleep(1)
    os.system('cls')
    name = input('NAME🥰: ')
    date = input('DATE🤍: ')
    priority = input('priority💕: ').capitalize()
    row = [name, date, priority]
    list.append(row)
    print('\033[35m  YOU HAVE SUCESSFULLY ADDED TO THE LIST💛', end='\033[0m')

def view():
    time.sleep(2)
    os.system('cls')
    q2 = input('1: All? \n2: Priority? ')
    if q2 == '1':
        for row in list:
            for item in row:
                print(item, end= '|')
            print()
        print()
    else:
        q3 = input(' \033[94m what Priority? ').capitalize()
        for row in list:
            if q3 in row:
                for item in row:
                    print(item, end= '|')
                print()
            print()

def edit():
    time.sleep(1)
    os.system('cls')
    q4 = input('Enter the name of task to edit💚: ')
    for row in list:
        if q4 not  in row:
            print('ITEM DOES NOT EXIST: ')
        elif q4 in row:
            list.remove(row)

    name = input('NAME🥰: ')
    date = input('DATE🤍: ')
    priority = input('priority💕: ').capitalize()
    row = [name, date, priority]
    list.append(row)
    print('\033[35m  YOU HAVE SUCESSFULLY EDITED THE LIST💛', end='\033[0m')

def remove():
    time.sleep(1)
    os.system('cls')
    q5 = input('enter the item you wish to remove🥰: ')
    for row in list:
        if q5 in row:
            list.remove(row)


while True:
    q1 = input('1: Add:\n2: View:\n3: Edit: \n4: Remove: \n--:')
    if q1 == '1':
        add()
    elif q1 == '2':
        view()
    elif q1 == '3':
        edit()
    else:
        remove()          
    time.sleep(1)
    os.system('cls')