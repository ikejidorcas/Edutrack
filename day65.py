class character:
    name = None
    health = None
    magic_point= None
    def __init__(self, name,health,magic_point):
        self.name= name
        self.health = health
        self.magic_point= magic_point
    def outcome(self):
        print('\033[94m == PLAYER1 INFO 🔥 ==', end='\033[0m')
        print()
        q1 = '| name'
        q2 = '| health'
        q3 = '| magicpoint'
        print(f'{q1:<10} {q2:^10} {q3:>10}')
        print(f'{self.name:<10} {self.health:^10} {self.magic_point:>10}')
class player(character):
    def __init__(self, name, health, magic_point, check):

        self.name= name
        self.health = health
        self.magic_point= magic_point
        self.check = check
    def outcome(self,):
        print('\033[94m == PLAYER2 INFO 🔥 ==', end='\033[0m')
        print()
        q1 = '| name'
        q2 = '| health'
        q3 = '| magicpoint'
        q4 = '| player state'
        print(f'{q1:<10} {q2:^10} {q3:>10} {q4:>10}')
        print(f'{self.name:<10} {self.health:^10} {self.magic_point:>10} {self.check:>10}')
class enemy(character):
    def __init__(self, name, health, magic_point,type, strenght):
        self.name= name
        self.health = health
        self.magic_point= magic_point
        self.type = type
        self.strenght =strenght
        
    def outcome(self,):
        print('\033[94m == PLAYER3 INFO 🔥 ==', end='\033[0m')
        print()
        q1 = '| name'
        q2 = '| health'
        q3 = '| magicpoint'
        q4 = '| player state'
        q5 = '| player type'
        q6 =' |player strenght'
        print(f'{q1:<10} {q2:^10} {q3:>10} {q5:>10} {q6:>10}')
        print(f'{self.name:<10} {self.health:^10} {self.magic_point:>10} {self.type:>15} {self.strenght:>10}')
       
olc = character('olc', 'good', '9')
olc.outcome()
me = player('vampire', 'good', '4', 'alive' )
me.outcome()
we = enemy('bat','good', '3','fire beast', '34hp' )
we.outcome()
        
        
