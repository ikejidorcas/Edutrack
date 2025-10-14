import random, os, time

box = ['gabble', 'cabalist', 'denary', 'fearful', 'huambo', 'juarez', 'rebate', 'recent', 'thesaurus', 'kelpy']
box1 = random.choice(box)
box2 = []
chances = 6
while True:
    time.sleep(1)
    os.system('cls')
    q1 = input('guess a letter in the magic word 🙂😛: ').lower()
    if q1 in box2:
        print('oops you already guessed this letter 😂')
        continue
    box2.append(q1)
    if q1 in box1:
        print('congratulations you found a letter 😍😘🤍')
    else:
        print('oops letter not in magic word 💚')
        chances-= 1
        print()
    letters = True
    for i in box2:
        if i in box2:
            print(i, end = ' ')
        else:
            print('_', end= ' ')
            letters = False
        print()
    if letters == False:
        print('-----------------+')
        print('                 |')
        print('                 |')
        print('                 |')
        print('                 |')
        print('                 |')
        print('                 |')
        print('             =====')
    else:
        print('-+----------------+')
        print(' o                |')
        print('/|\               |')
        print(' |                |')
        print(' |                |')
        print('/ \               |')
        print('                  |')
        print('             ======')

    if chances <=0:
        print('you ran out of chances 😁')
    else:
        print(f' you have {chances} left')
        
    



      

   
    





            
            
                

