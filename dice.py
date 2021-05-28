import random

#Dice Rolls
def d20(num_dice):
    d20_roll = 0
    for i in range(num_dice):
        d20_roll +=  random.randint(1, 20)
    return d20_roll


def d4(num_dice):
    d4_roll = 0
    for i in range(num_dice):
        d4_roll += random.randint(1, 4)
    return d4_roll


def d6(num_dice):
    d6_roll = 0
    for i in range(num_dice):
        d6_roll += random.randint(1, 6)
    return d6_roll      


def d8(num_dice):
    d8_roll = 0
    for i in range(num_dice):
        d8_roll += random.randint(1, 8)
    return d8_roll      


def d10(num_dice):
    d10_roll = 0
    for i in range(num_dice):
        d10_roll += random.randint(1, 10)
    return d10_roll 


def d12(num_dice):
    d12_roll = 0
    for i in range(num_dice):
        d12_roll += random.randint(1, 12)
    return d12_roll 