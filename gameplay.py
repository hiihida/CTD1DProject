# create a Jerry class with self.hunger, self.happiness, self.cleanliness
# game begins with self.hunger = 3, self.happiness = 3, self.cleanliness = 3
# player wins when self.hunger = 6, self.happiness = 6 self.cleanliness = 6

# retrieve pet name from main.py
from main import petName

class Pet:
    def __init__(self, hunger, happiness, cleanliness):
        self.hunger = hunger
        self.happiness = happiness
        self.cleanliness = cleanliness


# define functions for Feed, Play, Groom
"""
Feed (Hunger)
+ 1 bar of feed

Play (Happiness)
+ 2 bars of play
- 2 bars of feed

Groom (Cleanliness)
+ 3 bars of groom
- 2 bars of feed
- 2 bars of play (animal don’t like being washed)

"""
def feed(petClass):
    petClass.hunger += 1
    return petClass

def play(petClass):
    petClass.happiness += 2
    petClass.hunger -= 2
    return petClass

def groom(petClass):
    petClass.cleanliness += 3
    petClass.hunger -= 2
    petClass.happiness -= 2
    return petClass


# define functions for if self.hunger/self.happiness/self.cleanliness = 1 or 0
"""
If an interaction drops to 1 bar, the pet will notify the player with a text bubble. 
The pet will also have a sad face.
Feed: “I’m hungry”
Play: “I’m really sad”
Groom: “I need a shower”
If any of the interactions drops to 0 bars, game over screen.
"""
def stat_drop_1(petClass):
    if petClass.hunger == 1:
        print("Jerry: I'm hungry meow :(")
    if petClass.happiness == 1:
        print("Jerry: I'm really sad meow :(")
    if petClass.cleanliness == 1:
        print("Jerry: I need a shower meow :(")


def stat_drop_0(petClass):
    stat_bool = True
    if petClass.hunger == 0:
        print("Jerry was too hungry and ran away to find a better owner. "
              "Better luck next time!")
        stat_bool = False
    if petClass.happiness == 0:
        print("Jerry was too sad and ran away to find a better owner. "
              "Better luck next time!")
        stat_bool = False
    if petClass.cleanliness == 0:
        print("Jerry got too dirty and ran away to find a better owner. "
              "Better luck next time!")
        stat_bool = False
    return stat_bool

# nya nya
