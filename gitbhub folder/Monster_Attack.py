Character_attributes = {
    'Name': '',
    'Cool': 0,
    'Charm': 0,
    'Tough': 0,
    'Sharp': 0,
    'Weird': 0,
    'Health': 9,
    'Starting_Armor': 0,
    'Armor': 0
}
Monster_Ghoul = {
    'Health': 9,
    'Tough': 2,
    'Armor': 0
}
player_health = Character_attributes['Health']
monster_health = Monster_Ghoul['Health']
player_tough = Character_attributes['Tough']
monster_tough = Character_attributes['Tough']
player_armor = Character_attributes['Armor']
monster_armor = Monster_Ghoul['Armor']
chance = 0
import random


def dice_roll():
    return random.randint(1, 12)


def dmg_roll():
    dmg = dice_roll()
    if dmg <= 4:
        dmg = 1
        return dmg
    if 4 < dmg <= 11:
        dmg = 2
        return dmg
    if dmg == 12:
        dmg = 3
        return dmg


def monster_action():
    global player_health
    global monster_tough
    monster_roll = dice_roll()
    dmg = dmg_roll()
    monster_attack = monster_roll + monster_tough

    if monster_attack > 6:
        player_health = player_health - dmg
        return print(f'''
monster roll: {monster_roll}  
monster tough: {monster_tough}
monster result: {monster_roll}  
dmg: {dmg}      
Your health: {player_health}
The monster swings and hits you.
        ''')
    else:
        return print(f'''
monster roll: {monster_roll}  
monster tough: {monster_tough}
monster result: {monster_roll} 
Your health: {player_health}     
The monster swings and misses you
        ''')


def player_action():
    global monster_health
    global player_tough
    player_roll = dice_roll()
    dmg = dmg_roll()

    player_attack = player_roll + player_tough
    if player_attack > 6:
        monster_health = monster_health - dmg
        return print(f'''
Your roll: {player_roll}
your tough: {player_tough}
dmg: {dmg}
your result: {player_attack}
monster health: {monster_health}

You swing on the monster and hit it.''')
    else:
        return print(f'''
Your roll: {player_roll}
your tough: {player_tough}
your result: {player_attack}
monster health: {monster_health}
You swung on the monster and missed."
        ''')


def magic_attack():
    global monster_health
    global monster_armor
    magic_roll = dice_roll() + Character_attributes['Weird']
    if magic_roll <= 4:
        return print('''
You missed the monster.
        ''')
    elif 4 < magic_roll <= 9:
        monster_health = monster_health - 1 + monster_armor
        return print(f'''
You hit the monster. You dmg the monster for 1.
your roll: {magic_roll}
your dmg: 1
monster health: {monster_health}''')
    elif 9 < magic_roll < 11:
        monster_health = monster_health - 2 + monster_armor
        return print(f'''
You hit the monster. You dmg the monster for 2.
your roll: {magic_roll}
your dmg: 2
monster health: {monster_health}
''')
    elif magic_roll > 12:
        monster_health = monster_health - 4 + monster_armor
        return print(f'''
        You hit the monster. You dmg the monster for 4.
        your roll: {magic_roll}
        your dmg: 4
        monster health: {monster_health}
        ''')


def denfense():
    global player_armor
    Def = dice_roll()
    if Def <= 4:
        player_armor = player_armor + 1
        return print(f'''
You defend yourself adding 1 to your armor.
Your armor: {player_armor}
                ''')
    elif 4 < Def <= 11:
        player_armor = player_armor + 2
        return print(f'''
You defend yourself adding 2 to your armor.
Your armor: {player_armor}
                ''')
    elif Def == 12:
        player_armor = player_armor + 3
        return print(f'''
You defend yourself adding 3 to your armor.
Your armor: {player_armor}
        ''')


def sharp_roll():
    global Character_attributes
    plus_sharp = dice_roll() + Character_attributes['Sharp']
    return plus_sharp


def runaway():
    global player_health
    global chance
    chance = sharp_roll()
    if chance <= 4:
        dmg = dmg_roll() + 1
        player_health = player_health - dmg
        return print(f'''
You were not successful in a terrible way. The monster takes the oppurtunity and hits you for dmg.
dmg: {dmg}
your health: {player_health}''')
    if 4 < chance:
        dmg = dmg_roll()
        player_health = player_health - dmg
        print(f'''
You were successful in a terrible way. The monster takes the oppurtunity and hits you for dmg.
dmg: {dmg}
your health: {player_health}
''')
        return chance


# combat
enemy_name = 'Monster 1'

while monster_health > 0 or player_health > 0:
    action = input('''
attack or naw:
1: attack
2: defense
3: use magic
4: run away
Enter action: ''')
    if action == '1':
        player_action()
    if action == '2':
        denfense()
    if action == '3':
        magic_attack()
    if action == '4':
        runaway()
        print(f'chance: {chance}')
        if chance > 4:
            break
    if monster_health > 0:
        monster_action()
        if action == '2':
            player_armor = Character_attributes['Starting_Armor']
            print(f'''
Your armor has been restored to it starting value.
Player armor: {player_armor}
''')
        if player_health <= 0:
            break
    else:
        break
if monster_health <= 0:
    print('you defeated the monster')
elif player_health <= 0:
    print('the monster defeated you')
elif chance > 4:
    print('you got away from the monster')
