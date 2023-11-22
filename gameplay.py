# create a Jerry class with self.hunger, self.happiness, self.cleanliness
# game begins with self.hunger = 3, self.happiness = 3, self.cleanliness = 3
# player wins when self.hunger = 3, self.happiness = 3, self.cleanliness = 3
class Jerry:
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
- 2 bars of play (cat don’t like being washed)

"""
def feed(catClass):
    catClass.hunger += 1
    return catClass

def play(catClass):
    catClass.happiness += 2
    catClass.hunger -= 2
    return catClass

def groom(catClass):
    catClass.cleanliness += 3
    catClass.hunger -= 2
    catClass.happiness -= 2
    return catClass

# player's input



# define functions for if self.hunger/self.happiness/self.cleanliness = 1 or 0
"""
If an interaction drops to 1 bar, Jerry will notify the player with a text bubble. 
Jerry will also have a sad face.
Feed: “I’m hungry meow”
Play: “I’m really sad meow”
Groom: “I need a shower meow”
If any of the interactions drops to 0 bars, game over screen.
"""
def stat_drop_1(catClass):
    if catClass.hunger == 1:
        print("Jerry: I'm hungry meow :(")
    if catClass.happiness == 1:
        print("Jerry: I'm really sad meow :(")
    if catClass.cleanliness == 1:
        print("Jerry: I need a shower meow :(")


def stat_drop_0(catClass):
    stat_bool = True
    if catClass.hunger == 0:
        print("Jerry was too hungry and ran away to find a better owner. "
              "Better luck next time!")
        stat_bool = False
    if catClass.happiness == 0:
        print("Jerry was too sad and ran away to find a better owner. "
              "Better luck next time!")
        stat_bool = False
    if catClass.cleanliness == 0:
        print("Jerry got too dirty and ran away to find a better owner. "
              "Better luck next time!")
        stat_bool = False
    return stat_bool

# nya nya
