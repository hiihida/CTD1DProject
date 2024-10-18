# ASCII art for game
# rmb to give credit
# https://www.asciiart.eu/animals/cats
import time
#import os

"""
pet ascii
- normal
- happy (after being fed/played)
- sad (when any bar is at 1)
- sick
- champion
- running away
"""


# from gameplay import groom

def ascii(pet_type, state):
    if pet_type == "cat":
        print(cat_ascii(state))
    elif pet_type == "dog":
        print(dog_ascii(state))
    elif pet_type == "bird":
        print(bird_ascii(state))


def cat_ascii(state):
    normal_cat = '''
   \\    /\\ 
    )  ( ')
   (  /  )
    \\(__)|
  '''
    # print(normal_cat)
    # art by Joan Stark
    fed_cat = '''
       Yummy!

      /\\_____/\\ 
     /  o   o  \\
    ( ==  v  == )
     )         (
    (           )
   ( (  )   (  ) )
  (__(__)___(__)__)
  '''
    # print(fed_cat)
    # art by Joan Stark
    played_cat = '''
      Meow :3

        /\\_/\\           ___
       = o o =_______    \\ \\
       __ Y      __(  \\.__) )
   (◍)<_____>__(_____)____/
  '''
    # art by Julie Rhodes
    groomed_cat = '''
      Groomed!

     /\\_/-..--.
    / _ _   ,  ;
   `~=`Y'~_<._./
    <`-....__.'
  '''
    # Art by Marcin Glinski
    sad_cat = '''
                 I'm sad :(

                   ______
                 / >     >
                |  _   _|
               / '=__x ◞
             /         |  
          /    \\       ◞   
         |    |    |   |
     /¯¯|     |    |   |
    | (¯ \\  __ \\ __) ___)
    \\ __ )
   '''
    # https://www.pinterest.com/pin/815573813838700047/
    # by SHH
    sick_cat = '''
    )\\._.,--....,'``.
    /x   _.. \\   _\\  (`._ ,.
   `._.-(,_..'--(,_..'`-.;.' 
  '''

    champion_cat = '''
               __..--''``---....___   _..._    __
 /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
///_.-' _..--.'_    \                    `( ) ) // //
/ (_..-' // (< _     ;_..__               ; `' / ///
 / // // //  `-._,_)' // / ``--...____..-' /// / //

  '''

    cat_state = {'normal': normal_cat, 'feed': fed_cat, 'play': played_cat, 'groom': groomed_cat, 'sad': sad_cat,
                 'sick': sick_cat, 'champion': champion_cat}

    return cat_state[state]


# cat running away
def cat_running_away():
    def clear_screen():
        # Function to clear the console screen
        os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII frames of a cat running by chatgpt but modified it
    frames = [
        """


                      (`.-,')
                    .-'     ;
                _.-'   , `,-
          _ _.-'     .'  /._
        .' `  _.-.  /  ,'._;)
       (       .  )-| (
        )`,_ ,'_,'  \\_;)
('_  _,'.'  (___,))
 `-:;.-'
""",
        """


                                          (`.-,')
                                        .-'     ;
                                    _.-'   , `,-
                              _ _.-'     .'  /._
                            .' `  _.-.  /  ,'._;)
                           (       .  )-| (
                            )`,_ ,'_,'  \\_;)
                    ('_  _,'.'  (___,))
                     `-:;.-'
""",
        """


                                                                    (`.-,')
                                                                  .-'     ;
                                                              _.-'   , `,-
                                                        _ _.-'     .'  /._
                                                      .' `  _.-.  /  ,'._;)
                                                     (       .  )-| (
                                                      )`,_ ,'_,'  \\_;)
                                              ('_  _,'.'  (___,))
                                               `-:;.-'
  """,
        """




                                                                     _ _.-'  
                                                                   .' `  _.-.
                                                                  (       .  
                                                                  )`,_ ,'_,' 
                                                          ('_  _,'.'  (___,)
                                                           `-:;.-'
  """,
    ]

    # Number of times to repeat the animation
    num_repeats = 1
    for _ in range(num_repeats):
        for frame in frames:
            # clear_screen()
            print(frame)
            time.sleep(1 / 2)  # Adjust the sleep duration for the desired speed


def dog_ascii(state):
    normal_dog = '''
       __                 
    o-''|\\_____/)
     \\_/|_)     )
        \\  __  /
        (_/ (_/    

    '''
    # Art by Hayley Jane Wakenshaw <3

    fed_dog = '''
      ,    /-.
     ((___/ __>
     /      }
     \ .--.(        ___
     \\\   \\\       /___\\
'''
    # by Joan Stark

    played_dog = '''

         /^-^\\
        / o o \\
       /   Y   \\
       V \ v / V
         / - \\
        /    |
  (    /     |
   ===/___) ||

  '''
    # Art by Hayley Jane Wakenshaw
    groomed_dog = '''
      ___
   __/_  `.  .-"""-.
   \\_,` | \\-'  /   )`-')
    "") `"`    \\  ((`"`
   ___Y  ,    .'7 /|
  (_,___/...-` (_/_/ 

  '''
    # Art by Hayley Jane Wakenshaw
    sick_dog = '''
               /)-_-(\

               (o o) 
       .-----__/\\^/      
      /  __      /       
  \\__/\\ /  \\_\\ |/          
       \\     ||                 
       //     ||       
       |\\     |\\     
  '''
    # unknown creator
    sad_dog = '''
        I'm sad:(
           ___
          /  \\
         / ..|\\
        (_\  |_)
        /  \@' 
       /     \\
  _   /  `   |
  \\\/  \  | _\\
   \   /_ || \\\_
    \____)|_) \_)

  '''
    # art by Hayley Jane Wakenshaw
    champion_dog = '''
  ,-.___,-.
  \_/_ _\_/
    )>_O(
   { (_) }
    `-^-' 

  '''

    # Art by Joan G. Stark

    dog_state = {'normal': normal_dog, 'feed': fed_dog, 'play': played_dog, 'groom': groomed_dog, 'sad': sad_dog,
                 'sick': sick_dog, 'champion': champion_dog}
    return dog_state[state]


def dog_running_away():
    def clear_screen():
        # Function to clear the console screen
        os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII frames of a dog running
    frames = [
        """
                 .--~~,__
    :-....,-------`~~'._.'
     `-,,,  ,_      ;'~~'
      _,-' ,'`-__; '--.
     (_/'~~      ''''(;
    """,
        """                                      .--~~,__
                                :-....,-------`~~'._.'
                                 `-,,,  ,_      ;'~~'
                                  _,-' ,'`-__; '--.
                                 (_/'~~      ''''(;
  
    """,
        """
                                                              :-....,--
                                                               `-,,,  ,
                                                                _,-' ,'
                                                               (_/'~~ 
    """,
    ]

    # Number of times to repeat the animation
    num_repeats = 1
    for _ in range(num_repeats):
        for frame in frames:
            # clear_screen()
            print(frame)
            time.sleep(1 / 2)  # Adjust the sleep duration for the desired speed


def bird_ascii(state):
    normal_bird = '''
                  (@>  
                 {||
                --""--
                  ||
                  ||

  '''
    # unknown creator
    fed_bird = '''
           /'{>
       ____) (____
     //'--;   ;--'\\\\
    ///////\_/\\\\\\\\\\\\\\
'''
    # jgs 6
    played_bird = '''
                              .
                           | \\\/|
   (\\\   _                  ) )|/|
       (/            _----. /.'.'
 .-._________..      .' @ _\\\  .'
 '.._______.   '.   /    (_| .')
   '._____.  /   '-/      | _.'
    '.______ (         ) ) \\
      '..____ '._       )  )
         .' __.--\\\  , ,  // ((
         '.'     | \\\/   (_.'(
                 '   \\\ .'
                  \\\   (
                   \\\   '.
                    \\\ \\\ '.)
                     '-'-'
  '''
    # mrf
    groomed_bird = '''
   /""\\\      ,
   <>^  L____/|
    `) /`   , /
     \\\ `---' /
      `'";\\\)`
      _/_Y 

  '''
    # sk
    sick_bird = '''
         .------._ 
   .-"""`-.<')    `-._ 
  (.--. _   `._       `'---.__.-'
   `   `;'-.-'         '-    ._
     .--'``  '._      - '   .
      `""'-.    `---'    ,
            `\\
              `\\\      .'
                `'. '
                  `'.
  '''
    # jgs
    sad_bird = '''
       _...._
      /      \\
     /  O   O \\
    (     ^    )
    )          (
   (   -  -  -  )
  (             )
   (            )
    [          ]
  ---/l\\\    /l\\\--------
    ----------------
       (  )
      ( __ _)
  '''
    # unknown creator
    champion_bird = '''
        _\\\|      __    
_-  \\\_  _/"->   _/  -_
-_    `-'(   )`-'    _-
`=.__.=-(   )-=.__.='
        |/-\\\|
        Y   Y
'''
    # cjr
    run_away_bird = '''
            _.-'`)     (`'-._
          .' -' / __    \\\ '- '.
         / .-' ( '-,`|   ) '-. \\
       ; ; /.`'.-'(   )'-.'`.\\\ ; ;
       | .-'|\\\//'-/   \\\-'\\\/|'-. |
       |` |; :|'._\\\   /_,'|: ;| `|
       || : |;    `Y-Y`    ;| : ||
       \\\:| :/======"="======\\\| |:/
       /_:-`                 `-;_\\\  
  '''
    # jgs

    # by Joan G. Stark
    bird_state = {'normal': normal_bird, 'feed': fed_bird, 'play': played_bird, 'groom': groomed_bird,
                  'sick': sick_bird, 'sad': sad_bird, 'champion': champion_bird, 'run_away': run_away_bird}
    return bird_state[state]
