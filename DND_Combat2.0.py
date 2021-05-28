import random
import time
import dice
import monsters
import heroes

print(dice.d20(1))


monsters = monsters.monsters()

#Functions List

def main_menu():
    print('Welcome to your next adventure, hero!\n')
    time.sleep(1.5)
    player = heroes.choose_char()
    player['name'] = input('\nPlease enter your character name: ')
    return player



#Program

player = main_menu()
    
print(player)

#monsters = monsters.monsters()

print(monsters)