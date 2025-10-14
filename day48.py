import os, time
while True:
    s = open('didi. list', '+a')
    q3 = 'High score board'
    q1 = input('enter three letter initials of your choice: ')
    q2 = input('enter score: ')
    print(q3)
    s.write(f'{q1}:  {q2} \n')
    time.sleep(1)
    os.system('cls')
    s.close()