import os, time
clue = {}
def prettyprint():
    time.sleep(1)
    os.system('cls')
    print()
    for key, value in clue.items():
        print(f'{key}: {value['location']}| {value['weapon']}| {value['energy']}')
    print()
while True : 
    q6 = '\033[1m   \033[31m BEAST INFO 🔥🔥'
    print(f'{q6:>10}')
    
    name = input('\033[94m  beast name😛😮: ')
    location =input('\033[1m beast type🥰: ')
    weapon = input('HP: ')
    energy = input('mp: ')
    clue[name]= {'location': location, 'weapon': weapon, 'energy': energy}
    prettyprint()


"""bianca= {'days complete':46, 'streaks': 12 }
rabbi = {'days complete': 12, 'straeks': 13}
david = {'days complete': 56, 'streaks': 19}
progress ={'bianca': bianca, 'rabbi': rabbi, 'david': david}
print(progress)"""
