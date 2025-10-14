"""val1 = input('who is the most popular princess in the whole wild world🧡❤💜😊: ')
if val1.upper().strip() == 'PRINCESS BIANCA':
    print('\033[94m you are very correct my loyal subject 🥰😘😎')
else:
    print('\033[31m YOU ARE VERY WRONG BOZO 😡😒 NOW LEAVE MY PRESENCE')"""



list = []
def guy():
    print('welcome to my list💙')
    print()
    for r in list:
        print(r)
        print()
while True:
    q1 = input('build list💚: ').strip().capitalize()
    if q1 not in list:
        list.append(q1)
    guy()