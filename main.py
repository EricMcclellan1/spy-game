print('''
*******************************************************************************
    0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777
*******************************************************************************
''')

import time #Importing time modeule
print("Welcome to Skull Island 007.")
print("Your mission is to find the treasure... or Die Trying.")

time.sleep(2)
print("Muahhahahah ahahaha")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

time.sleep(2)

choice1 = input ('You\'re at a cross road of the secret base. How would you like to proceed? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input ('You\'ve come to a lake passing by the 2nd base. Type "wait" to wait for boat to sneak on. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input ('You have arrived at the true main base unharmed. There are 3 doors. One red, one yellow and one blue. Which color do you choose? \n').lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over")
      time.sleep(1)
      print('''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
''')

    elif choice3 == "yellow":
      print("You found the treasure agent 007! You win!")
      time.sleep(1)
      print('''
    ******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
''')
    elif choice3 == "blue":
      print("You enter a room of armed soldiers aiming at your head. Game Over.")
      time.sleep(1)
      print('''
               |\                |\                       
    || .---.          || .---.          || .---.          
    ||/_____\         ||/_____\         ||/_____\         
    ||( '.' )         ||( '.' )         ||( '.' )         
    || \_-_/_         || \_-_/_         || \_-_/_         
    :-"`'V'//-.       :-"`'V'//-.       :-"`'V'//-.       
   / ,   |// , `\    / ,   |// , `\    / ,   |// , `\    
  / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |   
 /_/||__//   || |  /_/||__//   || |  /_/||__//   || |  
 \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  
  \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |   
  /\|_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |   
  `--|`^"""^`||_|   `--|`^"""^`||_|   `--|`^"""^`||_|   
     |   |   ||/       |   |   ||/       |   |   ||/      
     |   |   |         |   |   |         |   |   |        
     |   |   |         |   |   |         |   |   |        
     |   |   |         |   |   |         |   |   |         
     L___l___J         L___l___J         L___l___J         
      |_ | _|           |_ | _|           |_ | _|    
''')
    else:
      print("You chose a door that doesn't exist. Game over.")
  else:
    print("You get attacked by angry shark, the one day you forgot shark repllent. Game Over.")
else:
  print("You get spotted by a guard and shot. Game Over.")
  time.sleep(1)
  print('''
     -"           ^""**$$$e.
   ."                   '$$$c
  /                      "4$$b
 d  3                      $$$$
 $  *                   .$$$$$$
.$  ^c           $$$$$e$$$$$$$$.
d$L  4.         4$$$$$$$$$$$$$$b
$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
$$$$P d$$$$F $ $$$$$$$$$- $$$$$$
3$$$F "$$$$b   $"$$$$$$$  $$$$*"
 $$P"  "$$b   .$ $$$$$...e$$
  *c    ..    $$ 3$$$$$$$$$$eF
    %ce""    $$$  $$$$$$$$$$*
     *$e.    *** d$$$$$"L$$
      $$$      4J$$$$$% $$$
     $"'$=e....$*$$**$cz$$"
     $  *=%4.$ L L$ P3$$$F
     $   "%*ebJLzb$e$$$$$b
      %..      4$$$$$$$$$$
       $$$e   z$$$$$$$$$$
        "*$c  "$$$$$$$P"
          """*$$$$$$$"
''')
