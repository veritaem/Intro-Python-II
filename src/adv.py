from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons.  A few stalactites and stalagmites dangle from the ceiling and floor", rm_layout = """
          ____  _ ________  ___   _
        VV    VV / _ \\   VV   VVV V
                / / \\ \\
               / /   \\ \\
    ^ ^^^^ ^ /  /     \\ \\^^^^^^
    ^^ ^  ^        x        ^^^^^   ^^^
"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", rm_layout = """
                     | |
        ___/ \\_______| |         __
       |               |        /
        \\       x      |_______/  /
         >_______  _______________/
                 | |
                    
"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", rm_layout = """
                                       ,   _   ,
                                        . (~) .
    _______x____                    ___,___#__ ,
               |                   |
               |                   |
               |                   |
               |                   |
               |                   |
""", items=[Item('lockbox','''a small lockbox lies in the corner of the room, behind a small pillar.
The lockbox is old and made of some unidentifiable metal.''', '''

''')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", rm_layout = """
               | |
               | |
               | |
    __________/  |
    ______x______/
        
"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south. A dusty key lies in the middle 
of the floor, with an ornate handle with a socket, presumably once holding a gem""", rm_layout = """
      __________________
     /                 \\
     |                  |
     |       k          |
     |         x        |
     \\_______  _______/
              ||       

""", items = [Item('ornate key', '''a long-handled key with a socket missing a gem.  
Something was etched here, long ago, but it has long since faded'''), Item('gold piece', '''all that is left of the old treasure...''')] ),

    'path': Room("Pathway", """The pathway has been winding slowly down and around 
for some time, becoming steeper and steeper until it finally terminates here, at 
this small hill.  Above you, you see the hill flatten, and the manor, darkly yawning above it.
A broken sign proved to be the first enemy you felled.""", rm_layout = """
                           .-----.
                         .'       `.
                        :      ^v^  :
                        :           :
                        '           '
         |~        www   `.       .'
        /.\       /#^^\_   `-/\--'
       /#  \     /#%    \   /# \\
      /#%   \   /#%______\ /#%__\\
     /#%     \   |= I I ||  |- |
     ~~|~~~|~~   |_=_-__|'  |[]|
       |[] |_______\__|/_ _ |= |`.
^V^    |-  /= __   __    /-\|= | :;
       |= /- /\/  /\/   /=- \.-' :;
       | /_.=========._/_.-._\  .:'
       |= |-.'.- .'.- |  /|\ |.:'
       \  |=|:|= |:| =| |~|~||'|
        |~|-|:| -|:|  |-|~|~||=|      ^V^
        |=|=|:|- |:|- | |~|~|| |
        | |-_~__=_~__=|_^^^^^|/___
        |-(=-=-=-=-=-(|=====/=_-=/\\
        | |=_-= _=- _=| -_=/=_-_/__\ 
        | |- _ =_-  _-|=_- |]#| I II
        |=|_/ \_-_= - |- = |]#| I II
        | /  _/ \. -_=| =__|]!!!I_II!!
       _|/-'/  ` \_/ \|/' _ ^^^^`.==_^.
     _/  _/`-./`-; `-.\_ / \_'\`. `. ===`.
    / .-'  __/_   `.   _/.' .-' `-. ; ====;\\
   /.   `./    \ `. \ / -  /  .-'.' ====='  >
  /  \  /  .-' `--.  / .' /  `-.' ======.' /
""", items = [Item('Broken Sign', '''A Broken sign.  Its warped board have writing on them.
|   |   |   |   |
BEWARE THE LIGHT
|   |   |   |   |'''), Item('Bloody Note', '''A bloody note with chunks torn out of it.
it must have been dropped here recently, given the wet blood.
It says: 

We lost the key, and now we cant get out.  Thrice-accursed Marwin lost the gem as well, through his fumbling.
The walls seem to be ... shifting...  I dont think we are going to make it out.  If anyone makes it deep
enough to find this note, please deliver it to my family.  They will reward you greatly.  

No name remains on the tattered scrap..''')])
}

# Link rooms together
room['outside'].s_to = room['path']
room['path'].n_to = room['outside']
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

Player_1 = Player('Player 1', char_class ='spelunker', location = room['path'])

# Write a loop that:
# print current room
user_input = str(input('You approach the cavern.. Could the stories of treasure and crime..and worse... be true?? \n[N]orth\n\n')).lower()

while not user_input == 'q':
    if user_input in ['n', 'north']:
        print('You Head North...')
        if Player_1.location.n_to != 'Nowhere to go here!':
            Player_1.move_location(Player_1.location.n_to)
            print(Player_1.location)
        else:
            print('wrong way!')
            print(Player_1.location)
    
    elif user_input in ['s', 'south']:
        print('You head South...')
        if Player_1.location.s_to != 'Nowhere to go here!':
            Player_1.move_location(Player_1.location.s_to)
            print(Player_1.location)
        else:
            print('wrong way!')
            print(Player_1.location)
    
    elif user_input in ['e', 'east']:
        print('You head East...')
        if Player_1.location.e_to != 'Nowhere to go here!':
            Player_1.move_location(Player_1.location.e_to)
            print(Player_1.location)
        else:
            print('wrong way!')
            print(Player_1.location)

    elif user_input in ['w', 'west']:
        print('You head West')
        if Player_1.location.s_to != 'Nowhere to go here!':
            Player_1.move_location(Player_1.location.s_to)
            print(Player_1.location)
        else:
            print('wrong way!')
            print(Player_1.location)
    
    elif user_input in ['x', 'inspect self', 'me']:
        print('------INSPECT SELF------')
        print(Player_1)
    
    elif user_input in ['i', 'inv', 'inventory']:
        print('------INVENTORY------')
        print(f'currently, {Player_1.name} is carrying around...')
        for l in range(len(Player_1.inventory)):
            print(f'\n{Player_1.inventory[l].name}\n{Player_1.inventory[l].description}\n')
        choice = str(input('What do you want to do? [#]drop item#  [R]eturn  [U]se')).lower()
        if choice.isdigit():
            digit = int(choice)-1
            Player_1.location.add_item(Player_1.inventory[digit])
            Player_1.drop_item(Player_1.inventory[digit])
            
        
        elif choice in ['return', 'r']:
            pass

    
    elif user_input in ['l', 'look', 'look at items']:
        print('------INVESTIGATION------')
        print('in this room you find...')
        for l in range(len(Player_1.location.items)):
            print(f'\n{l+1}) {Player_1.location.items[l].name}')
        choice = str(input('What will you do with them? [T]ake all  [#]take item#  [R]eturn')).lower()
        
        if choice in(['t', 'take']):
            items_copy = [item for item in Player_1.location.items]
            for item in items_copy:
                Player_1.add_item(item)
                Player_1.location.pickup_item(item)
            print('taken!')
            for l in range(len(Player_1.inventory)):
                print(f'\n{Player_1.inventory[l].name}')
            for l in range(len(Player_1.location.items)):
                print(f'\n{Player_1.location.items[l].name}')
        
        elif choice.isdigit():
            digit = int(choice)-1
            Player_1.add_item(Player_1.location.items[digit])
            Player_1.location.pickup_item(Player_1.location.items[digit])

        elif choice in ['r', 'return']:
            pass


    else:
        print('...')
        print(Player_1.location)
    user_input = (input('What do you want to do? \n\n GO: [N]orth  [S]outh  [E]ast  [W]est\nDO:[X]amine self  [I]nventory  [L]ook at items [Q]uit\n\n')).lower()

    #quit option
if user_input == 'q':
    raise SystemExit
