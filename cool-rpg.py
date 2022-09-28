#!/usr/bin/python3

'''The modified version of terminal RPG game'''

# random to generate a random riddle
# crayons to display color in terminal
import random
import crayons


# function to print a main menu and the commands
def showInstructions():
    print(f'''
{crayons.red("RPG Game", bold=True)}
{crayons.yellow("========")}
{crayons.red("Commands:")}
  {crayons.cyan("go [direction]")}
  {crayons.cyan("acquire [item, curio]")}
  {crayons.cyan("don [suit]")}
  {crayons.cyan("solve [riddle]")}
''')


def showStatus():
    # print the player's current status
    print(f'{crayons.blue("---------------------------")}')
    print(f'You are in the {crayons.green(currentRoom)}')
    # print the current inventory
    print(f'Inventory : {crayons.green(str(inventory))}')
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print(f"You see a {crayons.green(rooms[currentRoom]['item'])}")
    # print curio if there is one
    if "curio" in rooms[currentRoom]:
        print(f"You see a {crayons.green(rooms[currentRoom]['curio'])}")
    # ask player to play riddle
    if "riddle" in rooms[currentRoom]:
        print(f"You can also attempt to solve the {crayons.green(rooms[currentRoom]['riddle'])} while you are here!")
    print(f'{crayons.blue("---------------------------")}')


# function to play the riddle
def playMonsterRiddle():
    # inventory needs to be updated in this function, so making inventory global
    global inventory
    # dict of riddles
    mon_riddle = {"What do you call a monster with a high IQ?": "Frank-Einstein",
                  "Where do you go if you want to buy a zombie?": "Mon-Store",
                  "What monster plays the most April Fool's jokes?": "Prankenstein",
                  "There was a monster under your bed you looked under and saw nothing. there was a monster in your closet you looked in and saw nothing. there was a monster in your toy chest you looked in there and saw nothing. What was the monsters name?": "Nothing",
                  "The next answer that should escape your lips, should be the creature, wrapped in cloth strips; What am I?": "Mummy",
                  "Which is monster's favorite game?": "Hide and seak",
                  "What room do ghosts avoid?": "The living room",
                  "Which part of a road do Ghosts love to travel the most?": "The Dead End",
                  "What is a ghost's favorite dessert?": "Ice Scream",
                  "What do you get when you cross a snowman with a vampire?": "Frostbite"
                  }
    # convert riddle dictionary to list
    mon_riddle_list = list(mon_riddle.items())
    # ask a random riddle from the list
    random_riddle = random.choice(mon_riddle_list)
    # get the question and set it to variable question
    question = random_riddle[0]
    # assign answer variable to answer of the riddle
    answer = random_riddle[1]
    # counter for number of attempts
    attempts = 0
    # loops until 2 attempts unless player guessed it correct the first time
    while attempts < 2:
        print(
            f"Solve the following riddle to keep going. You have 2 attempts to get it right. {crayons.cyan(question)}")
        user_ans = input()
        # normalize user input
        user_ans = user_ans.lower().strip()
        attempts += 1
        # if input is correct, put it in inventory and break out of it
        if user_ans == answer.lower():
            print(f"{crayons.green('Awesome! You are a monster genius!')}")
            inventory += [move[1]]
            break
        # if player cannot guess in 2 attempts, display the message and provide the answer
        elif attempts == 2:
            print(f"Sorry, not quite. The correct answer was {crayons.cyan(answer)}")
            break
        else:
            print(f"{crayons.red('Try again!')}")


# an inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Restroom',
        'item': 'spooky pic',
    },
    'Kitchen': {
        'north': 'Hall',
        'down': 'Basement',
        'item': 'coffee',
    },
    'Basement': {
        'up': 'Kitchen',
        'item': 'fire extinguisher',
    },
    'Restroom': {
        'west': 'Hall',
        'east': 'Dining Room',
        'item': 'mammoth spray',
        'up': 'Bedroom'
    },
    'Bedroom': {
        'down': 'Restroom',
        'east': 'Media Room',
        'curio': 'avengers suit',
    },
    'Media Room': {
        'west': 'Bedroom',
        'item': 'potion',
        'riddle': 'monster riddle'
    },
    'Dining Room': {
        'west': 'Restroom',
        'south': 'Barn',
        'north': 'Pantry',
        'item': 'monster',
    },
    'Garden': {
        'east': 'Barn',
        'item': 'anti-monster hose',
    },
    'Barn': {
        'west': 'Garden',
        'item': 'magic wand',
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'energy drink',
    },

}

# start the player in the Hall
currentRoom = 'Hall'

# instructions so player knows what to do
showInstructions()

# loop forever
while True:

    showStatus()

    # acquire the player's next 'move'
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an item to have a space on them
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print(f"{crayons.blue('''You can't go that way!''')}")

    # if they type 'acquire' first
    if move[0] == 'acquire':
        # if the room contains an item, and the item is the one they want to acquire
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(f"{crayons.yellow(move[1])} {crayons.yellow('acquired!')}")
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to acquire
        else:
            # tell them they can't acquire it
            print(f'Can\'t acquire {crayons.red(move[1])}!')

    if move[0] == 'don':
        # if the room contains the suit, and the suit is the one they want to don
        if "curio" in rooms[currentRoom] and move[1] in rooms[currentRoom]['curio']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(f"You wore the {crayons.yellow(move[1])}, more power to you!")
            # delete the item from the room
            del rooms[currentRoom]['curio']
        # otherwise, if the item isn't there to acquire
        else:
            # tell them they can't don the suit
            print(f'Can\'t don {crayons.red(move[1])}!')

    if move[0] == 'solve':
        if "riddle" in rooms[currentRoom] and move[1] in rooms[currentRoom]['riddle']:
            playMonsterRiddle()
            del rooms[currentRoom]['riddle']

    # Define how a player can win
    if currentRoom == 'Garden' and 'magic wand' in inventory and 'potion' in inventory and 'avengers suit' in inventory:
        print(
            f'{crayons.magenta("You solved the riddle, have the avengers suit on and you escaped the house with the magic wand and potion...")} {crayons.green("YOU WIN", bold=True)}')
        break

    # If a player enters a room with a monster
    # define how player can escape the monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        required_inventory = ["spooky pic", "fire extinguisher", "mammoth spray", "avengers suit", "potion", "riddle"]
        if all(elem in inventory for elem in required_inventory):
            print(f"{crayons.yellow('''Phew...you survived the monster. What's your next move?''')}")
            continue
        else:
            print(
                f'''{crayons.red("You did not gather enough items to defeat the monster, it has got you... GAME OVER!", bold=True)}''')
        break
