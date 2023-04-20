Character_attributes = {
    'Name': '',
    'Cool': 0,
    'Charm': 0,
    'Tough': 0,
    'Sharp': 0,
    'Weird': 0,
    'Health': 7,
    'Starting_Armor': 0,
    'Armor': 0
}
Monster_Ghoul = {
    'Health': 8,
    'Tough': 2,
    'Armor': 0
}
Character_attributes['Name'] = input('''
Enter your characters name: ''')
while True:
    Choice = input(f'''
Choose to give or take points away from an attribute. All attributes are currently set to 0. You can have as low  as  -3
and up to 3 in a single attribute, and the sum of all attributes must add up to 3.  
The attributes are:
Cool: How cool does {Character_attributes['Name']} stay under pressure.
Charm: How well do they interact with others. 
Tough: How well do they take, and how well do they give damage. 
Sharp: How well they can pick up on things around them. 
Weird: How weird are they. 

What would you like to do?
1: Add points to an attribute
2: Take points from an attribute
3: Finalize your character

Enter Your choice: ''')
    if Choice == '1':
        choice = input('''
Which attribute would you like to add to?
1: Cool
2: Charm
3: Tough
4: Sharp
5: Weird
6: Back

Enter choice: ''')
        if choice == '1':
            if Character_attributes['Cool'] >= 3:
                print('You have the maximum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to add to cool?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Cool'] += at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '2':
            if Character_attributes['Charm'] >= 3:
                print('You have the maximum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to add to charm?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Charm'] += at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '3':
            if Character_attributes['Tough'] >= 3:
                print('You have the maximum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to add to tough?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Tough'] += at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '4':
            if Character_attributes['Sharp'] >= 3:
                print('You have the maximum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to add to sharp?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Sharp'] += at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '5':
            if Character_attributes['Weird'] >= 3:
                print('You have the maximum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to add to weird?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Weird'] += at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '6':
            True
    if Choice == '2':
        choice = input('''
Which attribute would you like to take from?
1: Cool
2: Charm
3: Tough
4: Sharp
5: Weird
6: Back
    
Enter choice: ''')
        if choice == '1':
            if Character_attributes['Cool'] <= -3:
                print('You have the minimum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to take from cool?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Cool'] -= at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '2':
            if Character_attributes['Charm'] <= -3:
                print('You have the minimum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to take from charm?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Charm'] -= at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '3':
            if Character_attributes['Tough'] <= -3:
                print('You have the minimum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to take from tough?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Tough'] -= at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '4':
            if Character_attributes['Sharp'] <= -3:
                print('You have the minimum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to take from sharp?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Sharp'] -= at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '5':
            if Character_attributes['Weird'] <= -3:
                print('You have the minimum amount, allocate points elsewhere.')
            else:
                at_input = int(input('''
How many would you like to take from weird?
Enter amount: '''))
            if at_input > 3:
                print(" You entered an unallowed amount")
            Character_attributes['Weird'] -= at_input
            print(f'''
Current stats:
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}''')
        at_input = 0
        if choice == '6':
            True
    if Choice == '3':
        ch_score = Character_attributes['Cool'] + Character_attributes['Charm'] + Character_attributes['Tough'] + \
                   Character_attributes['Sharp'] + Character_attributes['Weird']
        print(f'''
Cool: {Character_attributes['Cool']}
Charm: {Character_attributes['Charm']}
Tough: {Character_attributes['Tough']}
Sharp: {Character_attributes['Sharp']}
Weird: {Character_attributes['Weird']}

        ''')
        if ch_score < 3:
            print('''
Your total is less than 4, please balance your character attributes so that the sum is 3.''')
        if ch_score > 3:
            print('''
Your total is more than 4, please balance your character attributes so that the sum is 3.''')
        if ch_score == 3:
            finalization = input('''
Your attribute total is fine, are you sure you wish to continue?
1: Yes
2: No
 
Enter Choice: ''')
            if finalization == '1':
                break
            if finalization == '2':
                True
print('''
Enter anything if you'd rather not say: ''')
gender = input('''
What's your characters gender?
M/F/NA: ''').lower()
if gender == 'm':
    gender = 'fella'
elif gender == 'f':
    gender = 'lady'
elif gender == 'na':
    gender = 'person'
else:
    gender = 'person'
    input('''
We won't press you to say your gender.
Press enter to opt out of saying: ''')

player_health = Character_attributes['Health']
monster_health = Monster_Ghoul['Health']
player_tough = Character_attributes['Tough']
monster_tough = Character_attributes['Tough']
player_armor = Character_attributes['Armor']
monster_armor = Monster_Ghoul['Armor']
chance = 0
plus_sharp = 0

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


def defence():
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


article_read = False
n = 0
print(f'''
    {Character_attributes['Name']} is a low level agent in the Bureau of  Monster  Removal.  After  years  of  classroom 
lectures you are finally able to take on your first solo mission. You've been waiting patiently  for  your  turn  to  be
called up to the directors office so he can personally give out your assignment.
    Currently  sitting in your room, you see that you have been letting your chores  slip. Clothes  lay  everywhere  and 
open books scatter your desk. You have been bored for days and are itching to get things done.
    ''')
print('''
In areas like this you can choose to move to a different room by entering you numeric choice, or use the  command  words
like search, use, or inspect to get more information about the object that you want to perform the action on. If it is a
relevant command there will display the results of that action.
Try out by typing "Inspect books"''')

while n < 1:
    open_choice = input('''
1: Exit room
Or enter command.
Enter Command: ''').lower()
    if open_choice == 'inspect books':
        plus_sharp = sharp_roll()
        if plus_sharp < 6:
            print(f'''
            \nSharp roll: {plus_sharp}
You look at the books but you've gone over it too much in the past week. The first words are enough for  you  to  cringe
and the pain of boredom will be crippling. Hopefully the director calls you soon.
    ''')
        elif 6 <= plus_sharp < 9:
            print(f'''
            \nSharp roll: {plus_sharp} 
    You fan through the pages. The boredom has you just enjoying doing something tactile with your hands. You  stop   on  
the journal article titled "Magic, Monkeys, and Science. The binding of the mystical, the physical and the intellectual"
by Dr. Lawrence Beech. You remember vaguely reading it and dismissing it, it  really  was  two  bit  stuff  compared  to  
the other stuff you had to read from Dr. Johannsen or Dr. Price. Beech came off as the  fanatical. But  that's  all  you
really remember. 
   ''')
            n = n + 1
        elif 9 <= plus_sharp:
            article_read = True
            print(f'''
            \nSharp roll: {plus_sharp} 
            \nArticle_Read: {article_read}
    You fan through the pages. The boredom has you just enjoying doing something tactile with your hands. You  stop   on  
the journal article titled "Magic, Monkeys, and Science. The binding of the mystical, the physical and the intellectual"
by Dr. Lawrence Beech. You remember vaguely reading it and dismissing it, it  really  was  two  bit  stuff  compared  to  
the other stuff you had to read from Dr. Johannsen or Dr. Price. But you're bored enough to give it  another  read,  you           
get through it. 
    It was better on the second read. You get the basic idea that is purposed  by  Dr.  Beech. Using  magic  to  enhance 
technological abilities would be a break through not only in the cybernetic market, but can lead to machines  that  make 
more power than they need to operate. You put the article down feeling refreshed having worked out mentally.
''')
    if open_choice == '1':
        print('''
    Your irritated and can't sit still. So you leave your barrack and go exercise. Coming back you see  that  you  still  
haven't been notified.
''')
        n = n + 1
while n == 1:
    print('''
    After another hour of boredom you finally get called up to the directors office. You hop  to  your  feet,  and  walk
briskly to his office door. 
''')
    input(''' ''')