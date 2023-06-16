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
