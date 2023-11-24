# Main Menu
# Jerry the Game!
def main_menu():

    while True:
        print("Jerry the Game!")
        print("[1] New Game")
        print("[2] Continue")
        print("[3] Credits")
        print("[4] Exit")

        while True:
            option = input("Please select: ")
            validated_option = input_validation(option)
            if validated_option != False:
                break

        if validated_option == 1: # new game
            new_level()
            break
        elif validated_option == 2: # continue from previous progress
            pass
            break
        elif validated_option == 3: # credits
            pass
        elif validated_option == 4: # exit
            print("Goodbye!")
        break

def input_validation(player_input):

    if player_input.isnumeric() == False:
        print("Invalid input.")
        return False
    else:
        player_input = int(player_input.strip())

        if player_input not in range(4):
            print("Invalid option.")
            return False
        return player_input



# Gameplay
import gameplay as game # import gameplay.py

def new_level():

    #global petName = input("Please enter your pet's name: ")
    pet = game.Pet(3, 3, 3)
    print("Hunger bar: " + str(pet.hunger) + "\nHappiness bar: " + str(pet.happiness) +
          "\nCleanliness bar: " + str(pet.cleanliness))

    while True:
        print("[1] Feed \n[2] Play \n[3] Groom")
        action = input("Please select: ")

        if action == "1": # if feed
            game.feed(pet)
        elif action == "2": # if play
            game.play(pet)
        elif action == "3": # if groom
            game.groom(pet)

        # keep the max stat to 4
        if pet.hunger > 4:
            pet.hunger = 4
        elif pet.happiness > 4:
            pet.happiness = 4
        elif pet.cleanliness > 4:
            pet.cleanliness = 4

        # keep the min stat to 0
        if pet.hunger < 0:
            pet.hunger = 0
        elif pet.happiness < 0:
            pet.happiness = 0
        elif pet.cleanliness < 0:
            pet.cleanliness = 0

        print("Hunger bar: " + str(pet.hunger) + "\nHappiness bar: " + str(pet.happiness) +
              "\nCleanliness bar: " + str(pet.cleanliness))

        game.stat_drop_1(pet)
        game_state = game.stat_drop_0(pet)
        if game_state is False:
            print("Game Over!")
            break

main_menu()
# TEST, print your name
"""
print("Jaf")
print("sus")
print("jaf test")
print("xinping")
print("ihy")
print("lydia")
print("shar")
print("edit")
"""