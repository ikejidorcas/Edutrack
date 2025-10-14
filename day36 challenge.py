class_members = []

def class1():
    print()
    print('\033[31m  SS3A CLASS LIST 💙💛💚🤍', end= '\033[0m')
    print()
    for q1 in class_members:
        print(q1)
    print()
while True:
    print('STUDENTS NAMES" 😍🥰🤍❣')
    print()
    val1 = input('ENTER FIRST NAME: ').strip().capitalize()
    val2 = input('ENTER SURNNAME: ').strip().capitalize()
    print()
    q1 =f'{val2} {val1}'
    if q1 not in class_members:
        class_members.append(q1)
    else:
        print('This name is already in the list 🥰')
    class1()

