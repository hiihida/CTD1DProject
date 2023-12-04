# Main Menu
# Jerry the Game!

# XTODO: check if the game is winnable? lmao
# XTODO: fix the sick random event - at 0 bars, game over
# XTODO: add medicine for sick pet
# XTODO: let player choose what food to feed
# XTODO: add levels! reformat cat class
# TODO: ensure user can only go next level when prev level is completed
# TODO: add save/continue system
# XTODO: winning cat ascii (happy/dancing cat) and sick cat ascii
import ascii_art
import coins_and_shop


def main_menu():
    while True:
        print("Jerry the Game!")
        print("[1] New Game")
        print("[2] Continue")
        print("[3] Credits")
        print("[4] Exit")

        while True:
            option = input("Please select: ")
            validated_option = input_validation('main_menu', option)
            if validated_option is not False:
                break

        if validated_option == 1:  # new game
            level_menu()
            break
        elif validated_option == 2:  # continue from previous progress
            pass
            break
        elif validated_option == 3:  # credits
            credits()
        elif validated_option == 4:  # exit
            print("Goodbye!")
            break


def input_validation(menu, player_input):
    if not player_input.isnumeric():  # if player input is not numeric
        print("Invalid input.")
        return False
    else:
        player_input = int(player_input.strip())

        if (menu == 'main_menu' and player_input not in range(1, 5)) or \
                (menu == 'level_menu' and player_input not in range(1, 5)) or \
                (menu == 'game_menu' and player_input not in range(1, 7)):
            print("Invalid option.")
            return False
        else:
            return player_input


def level_menu():
    while True:
        print("\nNew Game!")
        print("\n[1] Level 1 \n[2] Level 2 \n[3] Level 3 \n[4] Back to Main Menu")

        while True:
            option = input("Please chose a level: ")
            validated_option = input_validation('level_menu', option)
            if validated_option is not False:
                break

        if validated_option == 1:  # level 1
            new_level("cat")
            return "cat"
        elif validated_option == 2:  # level 2
            new_level("dog")
            return "dog"
        elif validated_option == 3:  # level 3
            new_level("bird")
            return "bird"
        elif validated_option == 4:  # exit
            main_menu()


# Gameplay
import gameplay as game  # import gameplay.py
import coins_and_shop as coins_shop  # import coins_and_shop.py


def new_level(petType):
    # petName = input("Please enter your pet's name: ")
    # initialize pet
    if petType == "cat":
        pet = game.Pet("Jerry", petType, 3, 3, 3, False)
    elif petType == "dog":
        pet = game.Pet("Dog name", petType, 3, 3, 3, False)
    elif petType == "bird":
        pet = game.Pet("Bird name", petType, 3, 3, 3, False)
    else:
        pet = game.Pet("Jerry", petType, 3, 3, 3, False)  # unbound error

    print("\nNew Game!")
    print("After you perform any three actions (Feed, Play or Groom), the day will end.")
    print(f"You find 5 coins that were lying next to {pet.name}!")

    # initialize coins
    coin_system = coins_shop.CoinShopSystem()
    # print(coin_system)

    # initialize day = 1
    no_of_days = 1
    action_number = 0
    ascii_art.ascii(petType, 'normal')

    # initialize day range that pet is healthy
    # day_range = 1
    # initialize probability of pet getting sick
    probability = 0.2

    while True:
        # set day and coins collected
        dayAction = pet.day(no_of_days, action_number, coin_system)

        # check for a new day
        if dayAction is None:  # if not new day yet
            print(f"\nDay {no_of_days}")
        else:  # if new day
            no_of_days, action_number, coins_collected = dayAction
            print(f"\nDay {no_of_days}")
            if coins_collected == 0:
                print("Daily bonus: Oops, you did not get any coins. Better luck next time!\n")
            elif coins_collected == 1:
                print(f"{pet.name} found {coins_collected} coin for you while hunting!")
            elif coins_collected >= 1:
                print(f"{pet.name} found {coins_collected} coins for you while hunting!")

            # check for pet's health
            probability = pet.health(no_of_days, probability)
            pet.limit_stats()

        # check for number of actions left
        action_number_left = 3 - action_number
        if action_number_left == 1:
            print(f"You have {action_number_left} action left before the day ends.")
        else:
            print(f"You have {action_number_left} actions left before the day ends.")

        coin_system.display_inventory()
        print()

        pet.display_stats()
        game_state = pet.check_game_lose()
        if game_state is False:
            break

        print("[1] Feed \n[2] Play \n[3] Groom \n[4] Shop \n[5] Save \n[6] Exit")

        while True:
            action = input("Please select: ")
            validated_action = input_validation('game_menu', action)
            if validated_action is not False:
                break

        while True:
            if validated_action == 1:  # if feed
                while True:
                    feedBool = pet.feed(action_number, coin_system.player_inventory)
                    if feedBool is not None:
                        action_number += 1
                    break
            elif validated_action == 2:  # if play
                pet.play(action_number)
                action_number += 1
            elif validated_action == 3:  # if groom
                pet.groom(action_number)
                action_number += 1
            elif validated_action == 4:  # shop
                while True:  # keep showing shop menu until player goes back
                    # actionBool = False
                    shopBool = coins_shop.main(coin_system)
                    if shopBool is False:
                        break
            elif validated_action == 5:  # save
                pass
            elif validated_action == 6:  # exit
                print("Goodbye!")
                return False
            break

        # game.limit_stats(pet)

        game_state = pet.stat_up_6()
        if game_state is True:  # won
            break
        game_state = pet.check_game_lose()
        if game_state is False:  # lost
            break


def credits():
    print("\nJerry Fanclub!")
    print("Nurul Hidayah Bte Md Azmi")
    print("Jafira Bte Abdul Nassar")
    print("Robert Rajkumar Lydia Rachel Robert")
    print("Tan See Yen Amanda ")
    print("Wong Xin Ping")
    print("Sharmaine Koh Xin Yi")
    print()


main_menu()