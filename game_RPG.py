import random

def show_InitialMenu():
    print("Welcome to FinalPythonsy!\n")
    print("1. Start Game")
    print("2. Exit\n")
    option = input("Enter your option:\n")
    return option

def goodbye_Message():
    print("Thanks for playing. See ya!")

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

def show_FightMenu(character, enemy):
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
            # Attack
            modified_damage = damage[character] + damage_modifier[character].get(enemy, 0)
            life[enemy] -= modified_damage
            print("✩----------------------✩")
            print(f"You have attacked {enemy} and dealt {modified_damage} damage points!")

