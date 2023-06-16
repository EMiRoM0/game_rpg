import random

#An initial menu with 2 options for the game
def show_InitialMenu():
    print("Welcome to FinalPythonsy!\n")
    print("1. Start Game")
    print("2. Exit\n")
    option = input("Enter your option:\n")
    return option

#A message if we select exit
def goodbye_Message():
    print("Thanks for playing. See ya!")

#Here we show the available characters to choose
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

#Now then we assign the different values of each character like their life points, max life points, damage and the damage modifier
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

#Here shows our selected character and our enemy
    print(f"You have selected... {character}!")
    print(f"You will fight against... {enemy}!")

#Now here are the status of the battle, all type of details and the table of actions.
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

#Now this happen if we attack
        if option == "1":
            # Attack logic
            modified_damage = damage[character] + damage_modifier[character].get(enemy, 0)
            life[enemy] -= modified_damage
            print("✩----------------------✩")
            print(f"You have attacked {enemy} and dealt {modified_damage} damage points!")

#Here it is when our life is zero, we lose
            if life[enemy] <= 0:
                print("✩----------------------✩")
                print(f"You have defeated {enemy}!")
                break

            # Enemy attack logic here
            modified_damage = damage[enemy] + damage_modifier[enemy].get(character, 0)
            life[character] -= modified_damage
            print(f"{enemy} attacks you and deals {modified_damage} damage points.")

#In the case we defeat the enemy this will appear
            if life[character] <= 0:
                print("✩----------------------✩")
                print("You have been defeated!")
                break

#If we choose the action number 2, we can heal us and recover life points
        elif option == "2":
            # Player's healing
            life[character] += 15
            if life[character] > initial_Life[character]:
                life[character] = initial_Life[character]
                print("✩----------------------✩")
            print(f"You have healed. Your current health is {life[character]}")

            # Enemy logic and what happend if the enemy damage us the enough
            modified_damage = damage[enemy] + damage_modifier[enemy].get(character, 0)
            life[character] -= modified_damage
            print(f"{enemy} attacks you and deals {modified_damage} damage points.")

            if life[character] <= 0:
                print("✩----------------------✩")
                print("You have been defeated!")

                break
            #And if we select the action, the game ends
        elif option == "3":
            goodbye_Message()
            break
        #If we put an invalid option, other number, this will appear
        else:
            print("✩----------------------✩")
            print("Invalid option. Please try again.")

            turns += 1
            #There is the probability of the enemy to heal theirselves
        if turns % random.randint(2, 3) == 0:
            # Enemy's healing
            life[enemy] += 15
            if life[enemy] > initial_Life[enemy]:
                life[enemy] = initial_Life[enemy]
                print("✩----------------------✩")
            print(f"{enemy} has healed and recovered 15 life points.")

option = show_InitialMenu()

#When we will choose a character there is a randomizer to assign our enemy
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

#If in the initial menu we put 2, the code ends
elif option == "2":
    goodbye_Message()

else:
    print("✩----------------------✩")
    print("Invalid option. Please try again.")
