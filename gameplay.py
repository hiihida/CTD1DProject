# create a Jerry class with self.hunger, self.happiness, self.cleanliness
# game begins with self.hunger = 3, self.happiness = 3, self.cleanliness = 3
# player wins when self.hunger = 3, self.happiness = 3, self.cleanliness = 3
class Jerry:
    def __init__(self, hunger, happiness, cleanliness):
        print("init is called")
        self.hunger = hunger
        self.happiness = happiness
        self.cleanliness = cleanliness


cat = Jerry(3, 3, 3)
print("Hunger bar: " + str(cat.hunger) + "\nHappiness bar: " + str(cat.happiness) + "\nCleanliness bar: " + str(cat.cleanliness))
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

def play():
    pass

def groom():
    pass

# player's input
print("[1] Feed \n[2] Play \n[3] Groom")
action = input("Please select: ")

if action == "1":
    feed(cat)
    print("Jerry's hunger bar is now " +str(cat.hunger))
elif action == "2":
    play(cat)
elif action == "3":
    groom(cat)


# define functions for if self.hunger/self.happiness/self.cleanliness = 1 or 0
"""
If an interaction drops to 1 bar, Jerry will notify the player with a text bubble. 
Jerry will also have a sad face.
Feed: “I’m hungry meow”
Play: “I’m really sad meow”
Groom: “I feel dirty meow”
If any of the interactions drops to 0 bars, game over screen.
"""

# nya nya
