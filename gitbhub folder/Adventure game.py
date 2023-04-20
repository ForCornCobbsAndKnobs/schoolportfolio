#Character Creation

ability_scores = [
    [2, -1, 1, -1, 1],
    [-1, 2, 2, 1, 2],
    [1, 1, 1, 2, -1],
    [2, 2, 1, 1, -1],
    [-1, -1, -1, 2, 2]
]

start_choice = input('''
choose between the stat blocks.
1: stat block 1
2: stat block 2
3: stat block 3
4: stat block 4
5: stat block 5

enter choice: ''')

if start_choice == '1':
    charm = ability_scores[0][0]
    cool = ability_scores[1][0]
    sharp = ability_scores[2][0]
    tough = ability_scores[3][0]
    weird = ability_scores[4][0]
    start_choice = 'stat block 1'
elif start_choice == '2':
    charm = ability_scores[0][1]
    cool = ability_scores[1][1]
    sharp = ability_scores[2][1]
    tough = ability_scores[3][1]
    weird = ability_scores[4][1]
    start_choice = 'stat block 2'
elif start_choice == '3':
    charm = ability_scores[0][2]
    cool = ability_scores[1][2]
    sharp = ability_scores[2][2]
    tough = ability_scores[3][2]
    weird = ability_scores[4][2]
    start_choice = 'stat block 3'
elif start_choice == '4':
    charm = ability_scores[0][3]
    cool = ability_scores[1][3]
    sharp = ability_scores[2][3]
    tough = ability_scores[3][3]
    weird = ability_scores[4][3]
    start_choice = 'stat block 4'
elif start_choice == '5':
    charm = ability_scores[0][4]
    cool = ability_scores[1][4]
    sharp = ability_scores[2][4]
    tough = ability_scores[3][4]
    weird = ability_scores[4][4]
    start_choice = 'stat block 5'
print(f'''
You have chosen {start_choice}, your stats are as follows. 
Charm = {charm}
Cool = {cool}
Sharp = {sharp}
Tough = {tough}
Weird = {weird}
Have fun
''')

race_selection = input('''
Select a character Race:
1: Human
    +1 charm
    +1 cool
2: Lycan
    +1 tough
    +1 weird
3: Sphinx:
    +1 sharp
    +1 charm
''')

if race_selection == '1':
    charm = charm + 1
    cool = cool + 1
    race_selection = 'Human'
elif race_selection == '2':
    tough = tough + 1
    weird = weird + 1
    race_selection = 'Lycan'
elif race_selection == '3':
    sharp = sharp + 1
    cool = cool + 1
    race_selection = 'Shpinx'

print(f'''
You have choosen to be a {race_selection}. 
Here is your updated stat block:
Charm = {charm}
Cool = {cool}
Sharp = {sharp}
Tough = {tough}
Weird = {weird}
''')

character_name = input('''
Character Name: ''')

character_gender = input('''
M/F/NA: 
''').lower()

if character_gender == 'm':
    character_gender = 'fella'
elif character_gender == 'f':
    character_gender = 'lady'
elif character_gender == 'na':
    character_gender = 'living'

background = input('''
Choose a background:
1: Vagabond traveling the united states for gold.
2: Discharged military finding work as a gun for higher.
3: Adventurous type trying to see it all before.
''')

if background == '1':
    background_vagabond = True
    background = ' vagabond'
elif background == '2':
    background_military = True
    background = 'gun for hire'
elif background == '3':
    background_adventuros = True
    background = 'adventurer'

print(f'''
You are a {character_gender} {race_selection}. Who's background as a {background} has brought them to the town of
Lonesome in the western frontier.
''')
input('Press Enter to Continue')

#Dice Roller and Stat modification#

import random
def dice_roll():
    return random.randint(1, 20)

attack = dice_roll() + tough
