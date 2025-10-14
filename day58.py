import random, os, time
total=0
def game():
    attempts =0
    while True:
        number = random.randint(1, 100)
        guess = int(input('pick a number between 1 and 100: '))
        if guess > number:
            print('too high')
            attempts+=1
        elif guess < number:
            print('too low')
            attempts+=1
        else:
            print('just right')
            print(f'{attempts} attempts this round')
            return attempts
while True:
    menue = input('1.Number of attemts \n2.Guess the random number \n3. exit \n...')
    if menue == '2':
        total+=game()
    elif menue =='1':
        print(f'total attempts is {total}')
    else:
        break
    