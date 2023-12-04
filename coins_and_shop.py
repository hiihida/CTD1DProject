import random
# import main
import ascii_art


class CoinShopSystem:

    def __init__(self):
        self.player_inventory = {'total number of coins': 5, 'items': []}
        self.shop_items = {'Normal Pet Food': 1, 'Fancy Pet Food': 2, 'Exquisite Pet Food': 3, 'Medicine': 5}

    def spin_wheel(self):
        return random.randint(1, 3)

    def collect_coins(self):
        coins_collected = self.spin_wheel()
        self.player_inventory['total number of coins'] += coins_collected
        return coins_collected

    def display_inventory(self):
        print("\nPlayer's Inventory:")
        print(f"Total number of coins: {self.player_inventory['total number of coins']}")
        print(f"Items: {self.player_inventory['items']}")

    def display_shop(self):
        print("\nWelcome to the shop! Here are the items you can buy:")
        n = 1
        a = 0
        ls = ['Fills your pet’s hunger bar by 1 bar', 'Fills your pet’s hunger bar by 2 bars',
              'Fills your pet’s hunger bar by 3 bars', 'Cures your pet from ailments']
        for item, cost in self.shop_items.items():
            if cost == 1:
                print(f"[{n}] {item}: {cost} coin")
            else:
                print(f"[{n}] {item}: {cost} coins")
            print(ls[a])
            n += 1
            a += 1
        print('[5] Back')

    def buy_item(self, item):
        if item in self.shop_items and self.player_inventory[
            'total number of coins'] >= self.shop_items[item]:
            self.player_inventory['total number of coins'] -= self.shop_items[item]
            # print(self.shop_items[item])
            self.player_inventory['items'].append(item)
            print(f"Successfully bought {item}!")
            # retrieve pet type from main
            # petType = main.level_menu()
            # ascii_art.ascii(petType, item)
            return True
        else:
            print("Not enough coins or invalid item.")
            return False


# xp
def input_validation(menu, player_input):
    if not player_input.isnumeric():  # if player input is not numeric
        print("Invalid input.")
        return False
    else:
        player_input = int(player_input.strip())

        if (menu == 'shop_menu' and player_input not in range(1, 6)):
            print("Invalid option.")
            return False
        else:
            return player_input


def main(coin_system):
    # coin_system = CoinShopSystem
    coin_system.display_inventory()

    coin_system.display_shop()
    # player input on what to buy

    while True:
        selected_item = input("\nWhat do you want to buy (or select 5 to go back): ")
        validated_item = input_validation("shop_menu", selected_item)
        if validated_item is not False:
            break

    if validated_item == 1:
        coin_system.buy_item('Normal Pet Food')

    if validated_item == 2:
        coin_system.buy_item('Fancy Pet Food')

    if validated_item == 3:
        coin_system.buy_item('Exquisite Pet Food')

    if validated_item == 4:
        coin_system.buy_item('Medicine')

    if validated_item == 5:
        return False


if __name__ == "__main__":
    main()
