# create a Jerry class with self.hunger, self.happiness, self.cleanliness
# game begins with self.hunger = 3, self.happiness = 3, self.cleanliness = 3
# player wins when self.hunger = 6, self.happiness = 6 self.cleanliness = 6

# retrieve pet name from main.py
# from main import petName
import random
import ascii_art


class Pet:
    def __init__(self, name, petType, hunger, happiness, cleanliness, sick):
        self.name = name
        self.petType = petType
        self.hunger = hunger
        self.happiness = happiness
        self.cleanliness = cleanliness
        self.sick = sick

    def display_stats(self):
        hunger = '■' * self.hunger + '□' * (6 - self.hunger)
        happiness = '■' * self.happiness + '□' * (6 - self.happiness)
        cleanliness = '■' * self.cleanliness + '□' * (6 - self.cleanliness)

        print(f"Hunger bar: {self.hunger}/6 " + hunger + f"\nHappiness bar: {self.happiness}/6 " + happiness +
              f"\nCleanliness bar: {self.cleanliness}/6 " + cleanliness)

    def limit_stats(self):

        # keep the stat in range 0-6
        self.hunger = max(0, min(self.hunger, 6))
        self.happiness = max(0, min(self.happiness, 6))
        self.cleanliness = max(0, min(self.cleanliness, 6))

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

    def input_validation(self, player_input, inventory):
        if not player_input.isnumeric():  # if player input is not numeric
            print("Invalid input.")
            return False
        else:
            player_input = int(player_input.strip())

            if player_input not in range(1, len(inventory['items']) + 1):
                print("Invalid option.")
                return False
            else:
                return player_input

    def feed(self, action_number, inventory):
        if len(inventory['items']) > 0:
            for i in range(1, len(inventory['items']) + 1):
                print(str(i) + ": " + inventory['items'][i - 1])
            # user select what item to feed jerry
            while True:
                selected_item = input("Please select what item to feed your pet: ")
                validated_item = self.input_validation(selected_item, inventory)
                if validated_item is not False:
                    break

            item = inventory['items'][validated_item - 1]
            if item == 'Normal Pet Food':
                self.hunger += 1
            elif item == 'Fancy Pet Food':
                self.hunger += 2
            elif item == 'Exquisite Pet Food':
                self.hunger += 3
            elif item == 'Medicine':
                self.sick = False
                print("Jerry is now cured! ^w^")
            else:
                print("Invalid item.")

            inventory['items'].remove(item)
            print(f"Successfully fed {item} to {self.name}! ^w^")
            action_number += 1
            # print("You fed Jerry", item, "^w^")
            # print(ascii_art.cat_ascii('feed'))
            ascii_art.ascii(self.petType, 'feed')

            self.limit_stats()
            self.display_stats()
            print()
            return self, action_number
        else:
            print(f"You don't have any food to feed {self.name}.")

    def play(self, action_number):
        if self.petType == 'cat':
            self.happiness += 2
            self.hunger -= 1
            # print(ascii_art.cat_ascii('play'))
        elif self.petType == 'dog':
            self.happiness += 2
            self.hunger -= 2
            # print(ascii_art.dog_ascii('play'))
        elif self.petType == 'bird':
            self.happiness += 2
            self.hunger -= 1
            self.cleanliness -= 2
            # print(ascii_art.bird_ascii('play'))
        action_number += 1
        print(f"You played with {self.name} ^w^")
        ascii_art.ascii(self.petType, 'play')

        self.limit_stats()
        self.display_stats()
        print()
        return self, action_number

    def groom(self, action_number):
        if self.petType == 'cat':
            self.cleanliness += 2
            self.hunger -= 1
            # print(ascii_art.cat_ascii('groom'))
        elif self.petType == 'dog':
            self.cleanliness += 1
            self.hunger -= 1
            # print(ascii_art.dog_ascii('groom'))
        elif self.petType == 'bird':
            self.cleanliness += 2
            self.hunger -= 1
            # print(ascii_art.bird_ascii('groom'))
        action_number += 1
        print(f"You groomed {self.name} =D")
        ascii_art.ascii(self.petType, 'groom')

        self.limit_stats()
        self.display_stats()
        print()
        return self, action_number

    def day(self, day, action_number, coin_system):

        if action_number == 3:
            day += 1
            action_number = 0
            coins = coin_system.collect_coins()
            return day, action_number, coins

    # https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
    def generate_sick_probability(self, probability):
        # from day 4 onwards, pet has a chance of getting sick
        # chance increases by 0.1 each day
        # after getting sick, medicine has to be given
        # after recovery, pet has 3 days until there is a chance of getting sick again
        sickBool = random.choices(
            population=[True, False],
            weights=[probability, 1 - probability])[0]
        if sickBool is True:
            print(
                f"{self.name} is sick :( For each day that your pet is sick, its stats will decrease by 2. Feeding medicine to your pet will cure it!")
            ascii_art.ascii(self.petType, 'sick')
            self.sick = True
            probability = 0.2  # reset to 0.2
        else:
            probability += 0.1
            probability = min(probability, 1.0)
        return probability

    def health(self, days, probability):
        # if pet is healthy, check for probability of falling sick
        if self.sick is False:
            if days >= 2:  # day 2 onwards
                probability = self.generate_sick_probability(probability)
            print(probability, self.sick)

        # if pet is sick, decrease all stats by 2
        if self.sick is True:
            self.hunger -= 2
            self.happiness -= 2
            self.cleanliness -= 2
        return probability

    # define functions for if self.hunger/self.happiness/self.cleanliness = 1 or 0
    """
    If all interactions fill up to 6 bars, the game is won!
  
    If an interaction drops to 1 bar, the pet will notify the player with a text bubble. 
    The pet will also have a sad face.
    Feed: “I’m hungry”
    Play: “I’m really sad”
    Groom: “I need a shower”
  
    If any of the interactions drops to 0 bars, game over screen.
    """

    def stat_up_6(self):
        if self.hunger == 6 and self.happiness == 6 and self.cleanliness == 6:  # add win condition pet is healthy
            print("You won!")
            ascii_art.ascii(self.petType, 'champion')
            # self.pet_ascii(self, 'champion')

            return True

    def stat_drop_1(self):
        stat_bool = False
        if self.hunger == 1:
            print(f"{self.name}: I'm hungry :(")
            stat_bool = True
        if self.happiness == 1:
            print(f"{self.name}: I'm really sad :(")
            stat_bool = True
        if self.cleanliness == 1:
            print(f"{self.name}: I need a shower :(")
            stat_bool = True

        if stat_bool is True:
            ascii_art.ascii(self.petType, 'sad')
        return stat_bool

    def stat_drop_0(self):
        stat_bool = True
        if self.hunger == 0:
            print(f"{self.name} was too hungry and ran away to find a better owner. "
                  "Better luck next time!")
            stat_bool = False
        if self.happiness == 0:
            print(f"{self.name} was too sad and ran away to find a better owner. "
                  "Better luck next time!")
            stat_bool = False
        if self.cleanliness == 0:
            print(f"{self.name} got too dirty and ran away to find a better owner. "
                  "Better luck next time!")
            stat_bool = False

        if stat_bool is False:
            ascii_art.ascii(self.petType, 'run_away')
        return stat_bool

    def check_game_lose(self):
        # stat_up_6(self)
        self.stat_drop_1()
        game_state = self.stat_drop_0()
        if game_state is False:
            print("Game Over!")
            return game_state


"""
def display_stats(petClass):
  hunger = '■'*petClass.hunger + '□'*(6-petClass.hunger)
  happiness = '■'*petClass.happiness + '□'*(6-petClass.happiness)
  cleanliness = '■'*petClass.cleanliness + '□'*(6-petClass.cleanliness)

  print(f"Hunger bar: {petClass.hunger}/6 " + hunger + f"\nHappiness bar: {petClass.happiness}/6 " + happiness +
    f"\nCleanliness bar: {petClass.cleanliness}/6 " + cleanliness)
# define functions for Feed, Play, Groom
"""
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
"""
def feed(petClass, action_number, inventory):
  if len(inventory['items']) > 0:
    for i in range(1, len(inventory['items'])+1):
      print(str(i) + ": " + inventory['items'][i-1])
    # user select what item to feed jerry
    item = int(input("Please select what item to feed your pet: "))
    item = inventory['items'][item-1]
    if item == 'Normal Pet Food':
      petClass.hunger += 1
    elif item == 'Fancy Pet Food':
      petClass.hunger += 2
    elif item == 'Exquisite Pet Food':
      petClass.hunger += 3
    elif item == 'Medicine':
      petClass.sick = False
      print("Jerry is now cured! ^w^")
    else:
      print("Invalid item.")

    inventory['items'].remove(item)
    print(f"Successfully fed {item} to Jerry! ^w^")
    action_number += 1
    #print("You fed Jerry", item, "^w^")
    print(ascii_art.cat_ascii('feed'))

    limit_stats(petClass)
    display_stats(petClass)
    print()
    return petClass, action_number
  else:
    print("You don't have any food to feed Jerry.")

def play(petClass, action_number):
  petClass.happiness += 2
  petClass.hunger -= 1
  #petClass.cleanliness -= 1
  action_number += 1
  print("You played with Jerry ^w^")
  print(ascii_art.cat_ascii('play'))

  limit_stats(petClass)
  display_stats(petClass)
  print()
  return petClass, action_number

def groom(petClass, action_number):
  petClass.cleanliness += 2
  petClass.hunger -= 1
  #petClass.happiness -= 2
  action_number += 1
  print("You groomed Jerry =D")
  print(ascii_art.cat_ascii('groom'))

  limit_stats(petClass)
  display_stats(petClass)
  print()
  return petClass, action_number

def limit_stats(petClass):

  # keep the stat in range 0-6
  petClass.hunger = max(0, min(petClass.hunger, 6))
  petClass.happiness = max(0, min(petClass.happiness, 6))
  petClass.cleanliness = max(0, min(petClass.cleanliness, 6))

def day(day, action_number, coin_system):

  if action_number == 3:
    day += 1
    action_number = 0
    coins = coin_system.collect_coins()
    return day, action_number, coins


# Generating a random probability
def total_days(day, recovery_days):
  probability = 0
  if recovery_days != 0:
    for day in range(1,11):
      #restricts probability between 0 to 1
      probability += random.random()
  else:
    recovery_days -= 1
  return probability

# https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
def generate_sick_probability(petClass, probability):
  # from day 4 onwards, pet has a chance of getting sick
  # chance increases by 0.1 each day
  # after getting sick, medicine has to be given
  # after recovery, pet has 3 days until there is a chance of getting sick again
  sickBool = random.choices(
    population = [True, False], 
    weights = [probability, 1 - probability])[0]
  if sickBool is True:
    print("Jerry is sick :( gib medicine pls")
    print(ascii_art.cat_ascii('sick_cat'))
    petClass.sick = True
    probability = 0.2 # reset to 0.2
  else:
    probability += 0.1
    probability = min(probability, 1.0)
  return probability

def health(petClass, days, probability):
  # if jerry is healthy, check for probability of falling sick
  if petClass.sick is False: 
    if days >= 2: # day 2 onwards
      probability = generate_sick_probability(petClass, probability)
    print(probability, petClass.sick)

  # if jerry is sick, decrease all stats by 2
  if petClass.sick is True:
    petClass.hunger -= 2
    petClass.happiness -= 2
    petClass.cleanliness -= 2
  return probability
"""
"""
def recover(petClass, probability):
  # if cat is fed medicine, recover
  petClass.sick = False
  probability = 0.2
  return probability

def sickness(petClass, probability):
  if probability >= 0.75:
    print('Jerry is sick :(')
    petClass.sick = True
    #print(ascii_art.cat_ascii('sick'))
    for i in range(0,11,2):
      petClass.cleanliness -= 2
      petClass.hunger -= 2
      petClass.happiness -= 2

recovery_days = 0
def taking_medicine(inventory):
  del inventory['items']['medicine']
  print('Jerry is all okay! He will be recovering for 2 more days!')
  recovery_days = 2

"""

# define functions for if self.hunger/self.happiness/self.cleanliness = 1 or 0
"""
If all interactions fill up to 6 bars, the game is won!

If an interaction drops to 1 bar, the pet will notify the player with a text bubble. 
The pet will also have a sad face.
Feed: “I’m hungry”
Play: “I’m really sad”
Groom: “I need a shower”

If any of the interactions drops to 0 bars, game over screen.
"""
"""
def stat_up_6(petClass):
  if petClass.hunger == 6 and petClass.happiness == 6 and petClass.cleanliness == 6: # add win condition jerry is healthy
    print("You won!")
    print(ascii_art.cat_ascii('champion_cat'))
    #print("insert happy cat ascii here :3")
    return True

def stat_drop_1(petClass):
  stat_bool = False
  if petClass.hunger == 1:
    print("Jerry: I'm hungry meow :(")
    stat_bool = True
  if petClass.happiness == 1:
    print("Jerry: I'm really sad meow :(")
    stat_bool = True
  if petClass.cleanliness == 1:
    print("Jerry: I need a shower meow :(")
    stat_bool = True

  if stat_bool is True:
    print(ascii_art.cat_ascii('sad'))
  return stat_bool


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

  if stat_bool is False:
    ascii_art.cat_running_away()
  return stat_bool

def check_game_lose(petClass):
  #stat_up_6(petClass)
  stat_drop_1(petClass)
  game_state = stat_drop_0(petClass)
  if game_state is False:
    print("Game Over!")
    return game_state
"""