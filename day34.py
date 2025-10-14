import os, time
students_email = []

def cup():
    os.system('cls')
    count = 1
    print('\033[94m  STUDENTS EMAIL AVAILABLE🥰 \n', end = '\033[0m')
    print()
    for q2 in students_email:
        print(f'{count}: {q2}')
        count+=1
        time.sleep(1)

def spam(max):
    for t in range(0, max):
        print(f' Email{t + 1} \n Dear {students_email[t]} \n It has come to our attention that you dont know princess Bianca \n Who is one of the most popular princess in the whole wild word🥰🥰 \n  If you dont know her we insist you go research about her if you dont do that right away we promise to block your account😌😌 \n Kisses and love😘 \n I am the messangerIII😎 ')
        time.sleep(2)
        os.system('cls')

while True:
    q1 = input('1: Add email💙 \n2: Remove email💖 \n3: View email list💛 \n4: Lets get spamming😌 \n Choose > ')
    if q1 == '1':
        q2 = input('Add email🎁: ')
        students_email.append(q2)
    elif q1 == '3':
        cup()
    elif q1 == '4':
        spam(5)
        q2 = input('remove email👮‍♂️: ')
        if q2 in students_email:
            students_email.remove(q2)
        else:
            print('STUDENT EMAIL UNAVAILABLE💖')

    time.sleep(2)
    os.system('cls')
    

