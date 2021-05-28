import time

def choose_char():
    playable_characters = {
        'cleric': {
            'name': '',
            'hp': 11,
            'ac': 18,
            'speed': 25,
            'race': 'hill dwarf',
            'background': 'soldier',
            'alignment': 'neutral good',
            'initiative': -1, 
            'lvl': 1,
            'xp': 0,
            'xp_to_level': 300,
            'class': 'cleric',
            'char_type': 'pc'
        },
        'rogue': {
            'name': '',
            'hp': 9,
            'ac': 14,
            'speed': 25,
            'race': 'lightfoot halfling',
            'background': 'criminal',
            'alignment': 'neutral',
            'initiative': 3, 
            'lvl': 1,
            'xp': 0,
            'xp_to_level': 300,
            'class': 'rogue',
            'char_type': 'pc'
        },
        'fighter': {
            'name': '',
            'hp': 12,
            'ac': 17,
            'speed': 30,
            'race': 'human',
            'background': 'noble',
            'alignment': 'lawful neutral',
            'initiative': -1, 
            'lvl': 1,
            'xp': 0,
            'xp_to_level': 300,
            'class': 'fighter',
            'char_type': 'pc'
        },
        'wizard': {
            'name': '',
            'hp': 8,
            'ac': 12,
            'speed': 30,
            'race': 'high elf',
            'background': 'acolyte',
            'alignment': 'chaotic good',
            'initiative': 2, 
            'lvl': 1,
            'xp': 0,
            'xp_to_level': 300,
            'class': 'wizard',
            'char_type': 'pc'
        }
    }
    print('Please choose your character from the list below: \n')
    time.sleep(1.5)
    chars = playable_characters

    for char in playable_characters:
        print('A', chars[char]['race'], char.upper(), 'with a', 
            chars[char]['background'], 'background.')
        time.sleep(1.5)

    choice = input('\nPlease enter the class you want to choose: ')

    while choice not in chars:
        choice = input('Invalid selection, please choose again. ')
    return playable_characters[choice]

