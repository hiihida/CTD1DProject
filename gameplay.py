# create a Jerry class with self.hunger, self.happiness, self.cleanliness
# game begins with self.hunger = 3, self.happiness = 3, self.cleanliness = 3
# player wins when self.hunger = 3, self.happiness = 3, self.cleanliness = 3

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