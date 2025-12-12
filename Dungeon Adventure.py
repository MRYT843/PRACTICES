import random

class Player:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.defense = 5            
        self.inventory = []
        self.equipped_armor = None  

    def is_alive(self):
        return self.hp > 0

    def hp_bar(self, bar_length=20):
        ratio = self.hp / self.max_hp
        filled = int(bar_length * ratio)
        empty = bar_length - filled
        return "█" * filled + "░" * empty

    def equip_armor(self, item, defense_bonus):
        if self.equipped_armor:
            print(f"\n🛡 You unequipped {self.equipped_armor}.")
            self.defense -= self.equipped_defense_bonus

        self.equipped_armor = item
        self.equipped_defense_bonus = defense_bonus
        self.defense += defense_bonus
        print(f"\n🛡 You equipped {item}! Defense increased to {self.defense}.")


class Enemy:
    def __init__(self, name, hp, dmg, special_chance=0.3):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.special_chance = special_chance

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        if random.random() < self.special_chance:
            special_dmg = self.dmg + random.randint(5, 15)
            print(f"💥 {self.name} uses a SPECIAL ATTACK for {special_dmg} damage!")
            return special_dmg
        else:
            return random.randint(5, self.dmg)




def show_hp(player):
    print(f"\n❤️ HP: {player.hp}/{player.max_hp}")
    print(f"[{player.hp_bar()}]")  # HP bar



ARMOR_TYPES = {
    "Iron Armor": 10,
    "Steel Armor": 20,
    "Magic Shield": 15,
    "Dragon Scale": 30
}

def fight(player, enemy):
    print(f"\n⚔️ A wild {enemy.name} appears! ({enemy.hp} HP)")

    while enemy.is_alive() and player.is_alive():
        show_hp(player)
        print(f"{enemy.name} HP: {enemy.hp}")

        action = input("Choose action: [A]ttack  [R]un: ").lower()

        if action == "a":
            dmg = random.randint(10, 20)
            enemy.hp -= dmg
            print(f"\nYou hit {enemy.name} for {dmg} damage!")

            if enemy.is_alive():
                enemy_dmg = enemy.attack() - player.defense
                enemy_dmg = max(0, enemy_dmg)
                player.hp -= enemy_dmg
                print(f"{enemy.name} hits you for {enemy_dmg} damage after armor!")

        elif action == "r":
            print("\nYou ran away!")
            return

        else:
            print("\nInvalid action.")

    if not player.is_alive():
        print("\n💀 You have been defeated...")
    else:
        print(f"\n🏆 You defeated the {enemy.name}!")
        loot = random.choice(list(ARMOR_TYPES.keys()) + ["Potion", "Herb"])
        player.inventory.append(loot)
        print(f"You found **{loot}**!")

        # Auto-equip if loot is armor
        if loot in ARMOR_TYPES:
            player.equip_armor(loot, ARMOR_TYPES[loot])


def explore(player):
    show_hp(player)
    print("\nYou move deeper into the dungeon...")

    event = random.choice(["enemy", "item", "nothing"])

    if event == "enemy":
        fight(player, random.choice([
            Enemy("Demogorgon", 40, 20, special_chance=0.3),
            Enemy("Mind Flayer", 60, 25, special_chance=0.4),
            Enemy("Vecna", 80, 30, special_chance=0.5),
        ]))

    elif event == "item":
        loot = random.choice(list(ARMOR_TYPES.keys()) + ["Potion", "Herb"])
        player.inventory.append(loot)
        print(f"🧺 You found a **{loot}**!")

        if loot in ARMOR_TYPES:
            player.equip_armor(loot, ARMOR_TYPES[loot])

    else:
        print("The room is empty.")

def main():
    player = Player()
    print("🏰 Welcome to the Dungeon with Multiple Armor Types & Special Attacks!")

    while player.is_alive():
        show_hp(player)
        print("\n---- Dungeon Menu ----")
        print("[1] Explore")
        print("[2] Inventory")
        print("[3] Quit")

        choice = input("Choose: ")

        if choice == "1":
            explore(player)

        elif choice == "2":
            print("\n📦 Inventory:", player.inventory)
            print(f"🛡 Armor (Defense): {player.defense}")
            if player.equipped_armor:
                print(f"Currently Equipped: {player.equipped_armor} (+{player.equipped_defense_bonus} Defense)")

        elif choice == "3":
            print("\nGoodbye adventurer!")
            break

        else:
            print("\nInvalid option!")

    print("\nGame Over!")

main()
