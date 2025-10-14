class animals:
    name =None
    species = None
    sounds = None
    def __init__(self, name, species, sounds):
        self.name = name
        self.species = species
        self.sounds = sounds
    def talk(self):
        print(f'{self.name} says {self.sounds}')
class bird(animals):
    colour =None
    def __init__(self, colour):
        self.name = 'Bird'
        self.species = 'aves'
        self.sounds = 'tweet'
        self.colour = colour

        
dog = animals('dog', 'German shephard', 'woof')
print(dog.talk())
polly = bird('blue')
polly.talk()
print(polly.colour)
        