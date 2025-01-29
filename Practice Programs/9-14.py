import random
from random import randint

rand = randint(1,6)
print("Random number between 1 - 6: " + str(rand))

class Die:
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_die(self):
        return random.randint(1, self.sides)
        
        
die = Die()
for _ in range(6):
    print(die.roll_die())
    
    
    

