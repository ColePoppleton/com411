import random
import time
import os
import progressbar

game_Locations = ["forest", "mountains", "village", "desert"]
game_Events = ["You are being attacked", "You are hungry", "You ran out of manna", "You need to sleep"]
game_Npc = ["mage", "knight", "dog", "pig"]
character_name = input("Enter your name")


def game_loop():
    index = random.randrange(0, 3)
    print(f"You are {character_name}, you are traveling through a {game_Locations[index]} with your {game_Npc[index]}")
    print(f"{game_Events[index]}, what do you do?")
    match game_Events[index]:
        case "You are being attacked":
            combat_loop()
        case "You are hungry":
            care_loop()
        case "You ran out of manna":
            rest_loop()
        case "You need to sleep":
            rest_loop()


def combat_loop():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    enemy_alive = True
    while enemy_alive:
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1) Attack\n2)Heal\n3)Run")
        action = int(input("Enter your choice: "))
        match action:
            case 1:
                print("You killed the enemy")
                enemy_alive = False
            case 2:
                print("You regained health")
            case 3:
                print("You failed to escape")
    game_loop()


def animated_marker(text):
    widgets = [text + ': ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(50):
        time.sleep(0.1)
        bar.update(i)


def care_loop():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    animated_marker("Eating")
    game_loop()


def rest_loop():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    animated_marker("Resting")
    game_loop()


game_loop()
