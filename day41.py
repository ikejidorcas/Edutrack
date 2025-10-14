"""family = {'mother': 'Ifeoma', 'sister1': 'Miracle', 'sister2': 'Esther', 'brother': 'David', 'Father': 'Augustine'}
for name, value in family.items():
    print(f'{name}: {value}')"""

import os, time
print('LETS KNOW ABOUT YOU🤍💚🤩')


about = {'name': None, 'faculty': None, 'matric number': None, 'department': None, 'level': None}
for name, value in about.items():
    about[name] = input(f'{name}: ')
time.sleep(2)
os.system('cls')
    


print()
print('\033[31m  NOW YOU KNOW ABOUT A GREAT PERSON CONGRATULATIONS TO YOU😁😎🎊', end= '')
print()
for name, value in about.items():
    print(f'\033[35m   {name}: {value}')    
