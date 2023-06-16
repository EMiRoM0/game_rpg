#Cristobal Emilio Romo Calvillo 3Dual
#Python game
import random

# An initial menu with 2 options for the game
def show_InitialMenu():
    print("Welcome to FinalPythonsy!\n")
    print("1. Start Game")
    print("2. Exit\n")
    option = input("Enter your option:\n")
    return option

# A message displayed when the player selects exit
def goodbye_Message():
    print("Thanks for playing. See ya!")

# Displays the menu to select a character
def show_CharacterMenu():
    print("✩----------------------✩")
    print("Select your character:")
    print("1. Knight")
    print("2. Wizard")
    print("3. Paladin")
    print("4. Alchemist")
    option = input("Enter your option: ")
    print("✩----------------------✩")
    return option

# Displays the fight menu and handles the battle logic
def show_FightMenu(character, enemy):
    # Initialize life points, initial life points, damage, and damage modifiers for each character
    life = {
        "Knight": 50,
        "Wizard": 40,
        "Paladin": 60,
        "Alchemist": 45
    }
    initial_Life = {
        "Knight": 50,
        "Wizard": 40,
        "Paladin": 60,
        "Alchemist": 45
    }
    damage = {
        "Knight": 8,
        "Wizard": 7,
        "Paladin": 10,
        "Alchemist": 9
    }
    damage_modifier = {
        "Knight": {"Wizard": 3, "Paladin": -3},
        "Wizard": {"Alchemist": 3, "Knight": -2},
        "Paladin": {"Knight": 2, "Alchemist": -3},
        "Alchemist": {"Paladin": 4, "Wizard": -2}
    }

    turns = 0

    # Show the selected character and the enemy
    print(f"You have selected... {character}!")
    print(f"You will fight against... {enemy}!")

    while True:
        print("✩----------------------✩")
        print("Status:")
        print(f"Your life points: {life[character]}")
        print(f"{enemy}'s life points: {life[enemy]}")
        print("✩----------------------✩")
        print("What will you do?")
        print("1. Attack")
        print("2. Heal")
        print("3. Exit Game")
        option = input("Select an option: ")

        if option == "1":
            # Attack logic
            modified_damage = damage[character] + damage_modifier[character].get(enemy, 0)
            life[enemy] -= modified_damage
            print("✩----------------------✩")
            print(f"You have attacked {enemy} and dealt {modified_damage} damage points!")

            if life[enemy] <= 0:
                print("✩----------------------✩")
                print(f"You have defeated {enemy}!")
                break

            # Enemy attack logic
            modified_damage = damage[enemy] + damage_modifier[enemy].get(character, 0)
            life[character] -= modified_damage
            print(f"{enemy} attacks you and deals {modified_damage} damage points.")

            if life[character] <= 0:
                print("✩----------------------✩")
                print("You have been defeated!")
                break

        elif option == "2":
            # Player's healing
            life[character] += 15
            if life[character] > initial_Life[character]:
                life[character] = initial_Life[character]
            print("✩----------------------✩")
            print(f"You have healed. Your current health is {life[character]}")

            # Enemy attack logic
            modified_damage = damage[enemy] + damage_modifier[enemy].get(character, 0)
            life[character] -= modified_damage
            print(f"{enemy} attacks you and deals {modified_damage} damage points.")

            if life[character] <= 0:
                print("✩----------------------✩")
                print("You have been defeated!")
                break

        elif option == "3":
            goodbye_Message()
            break

        else:
            print("✩----------------------✩")
            print("Invalid option. Please try again.")

        turns += 1

        # There is a probability for the enemy to heal itself
        if turns % random.randint(2, 3) == 0:
            # Enemy's healing
            life[enemy] += 15
            if life[enemy] > initial_Life[enemy]:
                life[enemy] = initial_Life[enemy]
            print("✩----------------------✩")
            print(f"{enemy} has healed and recovered 15 life points.")

# Show the initial menu and handle user input
option = show_InitialMenu()

if option == "1":
    character_option = show_CharacterMenu()

    if character_option == "1":
        show_FightMenu("Knight", random.choice(["Wizard", "Paladin", "Alchemist"]))
    elif character_option == "2":
        show_FightMenu("Wizard", random.choice(["Knight", "Paladin", "Alchemist"]))
    elif character_option == "3":
        show_FightMenu("Paladin", random.choice(["Knight", "Wizard", "Alchemist"]))
    elif character_option == "4":
        show_FightMenu("Alchemist", random.choice(["Knight", "Wizard", "Paladin"]))
    else:
        print("✩----------------------✩")
        print("Invalid option. Please try again.")

elif option == "2":
    goodbye_Message()

else:
    print("✩----------------------✩")
    print("Invalid option. Please try again.")
