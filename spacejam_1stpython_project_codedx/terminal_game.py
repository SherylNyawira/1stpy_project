import random

def explore_galaxy():
    print("Welcome to the Unknown Galaxy!")
    print("You are the captain of a spaceship and your mission is to explore this uncharted territory.")
    print("You have two options:")
    print("1. Explore a nearby planet")
    print("2. Investigate a strange anomaly")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        explore_planet()
    elif choice == "2":
        investigate_anomaly()
    else:
        print("Invalid choice. Please try again.")
        explore_galaxy()

def explore_planet():
    print("You land on a planet and discover a hidden civilization.")
    print("You have two options:")
    print("1. Make peaceful contact with the civilization")
    print("2. Conquer the planet and claim its resources")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        make_contact()
    elif choice == "2":
        conquer_planet()
    else:
        print("Invalid choice. Please try again.")
        explore_planet()

def investigate_anomaly():
    print("You approach the strange anomaly and find a wormhole.")
    print("You have two options:")
    print("1. Enter the wormhole and see where it leads")
    print("2. Stay away from the anomaly and continue exploring")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        enter_wormhole()
    elif choice == "2":
        continue_exploring()
    else:
        print("Invalid choice. Please try again.")
        investigate_anomaly()

def make_contact():
    print("You establish peaceful contact with the civilization.")
    print("They share their knowledge and resources with you.")
    print("Congratulations! You have successfully completed your mission.")

def conquer_planet():
    print("You attack the civilization and conquer the planet.")
    print("However, your actions have consequences and the galaxy unites against you.")
    print("Your spaceship is destroyed and your mission ends in failure.")

def enter_wormhole():
    print("You enter the wormhole and find yourself in a parallel universe.")
    print("You encounter a hostile alien race.")
    print("You have two options:")
    print("1. Engage in a space battle")
    print("2. Try to negotiate a peace treaty")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        engage_in_battle()
    elif choice == "2":
        negotiate_peace()
    else:
        print("Invalid choice. Please try again.")
        enter_wormhole()

def continue_exploring():
    print("You decide to stay away from the anomaly and continue exploring the galaxy.")
    print("You encounter a friendly alien race and establish diplomatic relations.")
    print("Congratulations! You have successfully completed your mission.")

def engage_in_battle():
    print("You engage in a space battle with the hostile alien race.")
    print("Unfortunately, your spaceship is no match for their advanced technology.")
    print("Your mission ends in failure.")

def negotiate_peace():
    print("You successfully negotiate a peace treaty with the hostile alien race.")
    print("They become your allies and help you in your mission.")
    print("Congratulations! You have successfully completed your mission.")

explore_galaxy()