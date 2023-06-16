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
