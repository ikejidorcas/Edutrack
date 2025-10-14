import os, time
print('\033[94m','TO - DO LIST', '\033[0m', '🥰💛❤💙')
print()
todo = []
def show():
    print()
    for q1 in todo:
        print()
        print(f' {q1: >16} ')

while True:

    q2 = input('1: add task👩 \n2: reduce task💗 \n 3: view recent task💙 \n4: edit task added💜 \n5: delete to-do list💚 \n what would you like to do today:')
    print( f'\033[32m {q2: ^30}', end = '\033[0m')
    if q2 == '1':
        q1 = input('WHAT WOULD YOU LIKE TO DO TODAY 🥰😊: ')
        print(f'\033[1m  \033[35m  {q1: >16}   ', end = '\033[31m')
        todo.append(q1) 
    elif q2 == '3':
        show()
    elif q2 == '5':
        todo = []
        
    elif q2 == '4':
        q1 = input('WHAT WOULD YOU LIKE TO EDIT TODAY 🥰😊: ')
        q3 = input('what would you like to change it to: ')
        for t in  range(0, len(todo)):
            if todo[t] == q1:
                todo[t] = q3
    elif q2 == '2':
        q1 = input('WOW CONGRATS I BELIEVE YOU ARE DONE WITH THIS TASK 🤗🤩: ')
        confirm = input('are you sure you want to remove this task? ')
        if confirm == 'yes':
            if q1 in todo:
                todo.remove(q1)  
            else:
                print(f'{q1} was never in the list 😀 so that means  you are free from {q1} congratulations 🎉🎊🎈')
                    
    time.sleep(2)
    os.system('cls')