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
        # from day 2 onwards, pet has a chance of getting sick = 0.2
        # chance increases by 0.1 each day
        # after getting sick, medicine has to be given
        # after recovery, probability reset to 0.2
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
            # uncomment this to show the probability of pet getting sick
            #print(probability, self.sick)

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
            # print(ascii_art.ascii(self.petType, 'champion'))
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
            if self.petType == "cat":
                ascii_art.cat_running_away()
            elif self.petType == "dog":
                ascii_art.dog_running_away()
            elif self.petType == "bird":
                ascii_art.ascii(self.petType, "run_away")
        return stat_bool

    def check_game_lose(self):
        # stat_up_6(self)
        self.stat_drop_1()
        game_state = self.stat_drop_0()
        if game_state is False:
            print("Game Over!")
            return game_state
