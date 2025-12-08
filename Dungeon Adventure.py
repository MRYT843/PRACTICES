import random

# Player stats
player_hp = 20
inventory = []
monsters_defeated = 0

# Game intro
def intro():
    print("Welcome to Dungeon Adventure!")
    print("Commands: move, status, inventory, quit")
    print("Explore the dungeon, fight monsters, and collect items!\n")

# Encounter a monster
def encounter():
    monsters = ['Goblin', 'Skeleton', 'Orc', 'Slime']
    monster = random.choice(monsters)
    monster_hp = random.randint(5, 15)
    print(f"You encountered a {monster} with {monster_hp} HP!")
    return monster, monster_hp

# Battle system
def battle(player_hp, monster, monster_hp):
    global monsters_defeated
    while monster_hp > 0 and player_hp > 0:
        action = input("Do you want to 'attack' or 'run'? ").lower()
        if action == 'attack':
            damage = random.randint(1, 6)
            monster_hp -= damage
            print(f"You hit the {monster} for {damage} damage!")
            if monster_hp <= 0:
                print(f"You defeated the {monster}!\n")
                monsters_defeated += 1
                # Chance to get an item
                if random.random() < 0.5:
                    item = random.choice(['Potion', 'Gold', 'Sword'])
                    inventory.append(item)
                    print(f"You found a {item}!\n")
                return player_hp
            monster_damage = random.randint(1, 5)
            player_hp -= monster_damage
            print(f"The {monster} hits you for {monster_damage} damage! Your HP: {player_hp}")
        elif action == 'run':
            if random.random() < 0.5:
                print("You successfully escaped!\n")
                return player_hp
            else:
                print("You failed to escape!")
                monster_damage = random.randint(1, 5)
                player_hp -= monster_damage
                print(f"The {monster} hits you for {monster_damage} damage! Your HP: {player_hp}")
        else:
            print("Invalid action!")
    return player_hp

# Main game loop
def main():
    global player_hp
    intro()
    while True:
        command = input("Enter command: ").lower()
        if command == 'move':
            monster, monster_hp = encounter()
            player_hp = battle(player_hp, monster, monster_hp)
            if player_hp <= 0:
                print("You have been defeated. Game Over!")
                break
        elif command == 'status':
            print(f"HP: {player_hp}")
            print(f"Monsters defeated: {monsters_defeated}")
        elif command == 'inventory':
            if inventory:
                print("Inventory:", ', '.join(inventory))
            else:
                print("Your inventory is empty.")
        elif command == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
