import os, time, random
q1 ={}
q1['David'] = {'intelligence': 123, 'speed': 2, 'guile': 89, 'baldness': 87}
q1['Bianca'] = {'intelligence': 321, 'speed': 20, 'guile': 98, 'baldness': 78}
q1['Rabbi'] = {'intelligence': 67, 'speed': 4, 'guile': 34, 'baldness': 64}
q1['Adnan'] = {'intelligence': 76, 'speed': 5, 'guile': 43, 'baldness': 46}
while True:
    q2 = '\033[31m \033[1m TOP TRUMPS CHARACTERS🔥'
    print(f'{q2:>10}')
    for key in q1:
        print(key)
    player = input('player character🥰: ').strip().capitalize()
    comp = random.choice(list(q1.keys()))
    print('COMPUTER PICKED', comp)
    
    print()
    print('\033[94m1:INTELLIGENCE🧠 \n2:SPEED🏃💨 \n3:GUILE👀 \n4:BALDNESS👩‍🦲 ')
    q3 = input('--: ').strip().lower()

    print(f'{player}: {q1[player][q3]}')
    print(f'{comp}: {q1[comp][q3]}')

    if q1[player][q3] > q1[comp][q3]:
        print(player, 'wins🎉✨')
    elif q1[player][q3] < q1[comp][q3]:
        print(comp, 'wins🎉✨')
    else:
        print('it"s a tie 💕👀')
    time.sleep(3)
    os.system('cls')

