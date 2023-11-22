# Main Menu
# Jerry the Game!
print("Jerry the Game!")
print("[1] New Game")
print("[2] Continue")
print("[3] Credits")
print("[4] Exit")

# Gameplay
import gameplay as game # import gameplay.py

cat = game.Jerry(3, 3, 3)
print("Hunger bar: " + str(cat.hunger) + "\nHappiness bar: " + str(cat.happiness) +
      "\nCleanliness bar: " + str(cat.cleanliness))

while True:
    print("[1] Feed \n[2] Play \n[3] Groom")
    action = input("Please select: ")

    if action == "1": # if feed
        game.feed(cat)
    elif action == "2": # if play
        game.play(cat)
    elif action == "3": # if groom
        game.groom(cat)

    # keep the max stat to 4
    if cat.hunger > 4:
        cat.hunger = 4
    elif cat.happiness > 4:
        cat.happiness = 4
    elif cat.cleanliness > 4:
        cat.cleanliness = 4

    # keep the min stat to 0
    if cat.hunger < 0:
        cat.hunger = 0
    elif cat.happiness < 0:
        cat.happiness = 0
    elif cat.cleanliness < 0:
        cat.cleanliness = 0

    print("Hunger bar: " + str(cat.hunger) + "\nHappiness bar: " + str(cat.happiness) +
          "\nCleanliness bar: " + str(cat.cleanliness))

    game.stat_drop_1(cat)
    game_state = game.stat_drop_0(cat)
    if game_state is False:
        print("Game Over!")
        break

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