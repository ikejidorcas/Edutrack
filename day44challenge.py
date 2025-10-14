import random, os, time
def bingo1():
    game= random.randint(1, 90)
    return game
def gameprint():
    for f in bingo:
        for s in f:
            print(s, end= '\t \t ' )
        print()
        

game = []
for u in range(8):
    q1 = bingo1()
    while q1 in game:
        q1 = bingo1()
    game.append(q1)
game.sort()
bingo = [ [game[0], game[1], game[2]],
        [game[3], game[4],'BG!😛😝' ],
        [game[5], game[6], game[7]] 
        ]
gameprint()

while True:
    time.sleep(1)
    os.system('cls')
    gameprint()
    q1 = int(input('ENTER NUMBER🥰: '))
    for f in range(3):
       for s in range(3):
           if bingo[f][s] == q1:
               bingo[f][s] = '❌'
    count = 0            
    for f in range(3):
        for s in range(3):
            if s == '❌':
                count+=1
    if count ==7:
        os.system('cls')
        gameprint(bingo)
        print('CONGRATULATIONS TASK COMPLETED!🥰🎆🎈')
        break
    time.sleep(1)

    