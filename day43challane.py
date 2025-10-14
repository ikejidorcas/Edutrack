import random
def bingo():
    game= random.randint(1, 90)
    return game
def gameprint():
    for f in bingo:
        print(f)
game = []
for u in range(8):
    game.append(bingo())
game.sort
bingo = [ [game[0], game[1], game[2]],
         [game[3], game[4],'BINGO!😛😝' ],
         [game[5], game[6], game[7]] 
         ]
gameprint()