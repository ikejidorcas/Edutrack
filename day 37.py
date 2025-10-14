print('\033[95m    WELCOME TO MY BIO COMBO', end= '\033[0m  💙💖')
print()
first = input('enter first name: ').strip().lower()
second = input('enter last name: ').strip().lower()
colour = input('enter favourite colour: ').strip().lower()
city = input('enter city name: ').strip().lower()
val1= f'{first[:3]}{second[:2]}{colour[:2]}{city[:3]}'
print(f'YOUR BIO COMBO IS 😍😎 \n {val1}')