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
print("Hunger bar: " + str(cat.hunger) + "\nHappiness bar: " + str(cat.happiness) + "\nCleanliness bar: " + str(cat.cleanliness))

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

    game.stat_drop_1(cat)
    game_state = game.stat_drop_0(cat)
    if game_state is False:
        break

    print("Jerry's hunger bar is now " + str(cat.hunger))
    print("Jerry's happiness bar is now " + str(cat.happiness))
    print("Jerry's cleanliness bar is now " + str(cat.cleanliness))

# Game Over

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