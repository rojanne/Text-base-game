import time

def introScene():
    print("""
    You woke up from comatose after 3 months.
    You are in a hospital.
    You looked up at the clock and saw that it was 5 pm and nearly dark.
    You heard strange noises outside your room. 
    You opened the door and saw WALKING DEADS - ZOMBIES around.
    You have no choice but to go outside your room.
    There are three ways for you.
    Are you going straight, left or right?""")
    time.sleep(2)

    directions = ["left", "straight", "right"]
    choice = ""
    while choice not in directions:
        choice = input("\nstraight, left or right: ").lower()
        time.sleep(2)
        if choice == "straight":
            straightHall()
        elif choice == "right":
            rightHall()
        elif choice == "left":
            leftHall()
        else:
            print("\nWrong input. You are automatically dead.")
            gameOver()

def straightHall():
    print("""
    You found the exit way going to the parking lot.
    You checked each car for keys and gas until you found a toyota corolla ready for use.
    Where will you go?
    Are you going back home or look for help at a police station?""") 
    time.sleep(2)
    hol = input("\nHome or Police: ").lower()
    time.sleep(2)
    if hol == "home":
        myHome()
    elif hol == "police":
        police()
    else:
        print("\nWrong input. You are automatically dead.")
        gameOver()

def leftHall():
    print("""
        You walked quietly in the dark for about 3 minutes until you found yourself at a dead end.
        A swarm of zombies followed you.
        You looked so scared knowing that you can't do anything.
        The zombies took your life..... (T.T)""")
    gameOver()

def rightHall():
    print("""
    You run quietly until you finally see a room full of food and medicinal supplies.
    You found a backpack and filled it with supplies, but you heard someone and saw that it was a man in his twenties, alive.
    What will you do to him, will you take him or leave him there?""")
    time.sleep(2)
    tol = input("\nTake or Leave: ").lower()
    time.sleep(2)
    if tol == "take":
        takeHim()
    elif tol == "leave":
        leaveHim()
    else:
        print("\nWrong input. You are automatically dead.")
        gameOver()

def myHome():
    print("""
    You entered your house only to find it empty.
    You called for your family but no one was home.
    You felt helpless.
    You think for a long time.
    Will you stay at home or find your family?""")
    time.sleep(2)
    sog = input("\nStay or Go: ").lower()
    time.sleep(2)
    if sog == "stay":
        stayHome()
    elif sog == "go":
        findFamily()
    else:
        print("\nWrong input. You are automatically dead.")
        gameOver()

def police():
    print("""
    You entered the police station, no one was around.
    You took a lot of weapons and decided to go.
    As you were leaving, you saw group of zombies.
    Will you kill them first or leave immediately and find your family?""")
    time.sleep(2)
    kol = input("\nKill or Leave: ").lower()
    time.sleep(2)
    if kol == "kill":
        killZombies()
    elif kol == "leave":
        runAway()
    else:
        print("\nWrong input. You are automatically dead.")
        gameOver()

def stayHome():
    print("""
    You feel so sad and tired.
    You ran out of supplies.....
    You died from hunger and dehydration. 
    (T.T)""")
    gameOver()

def findFamily():
    print("""
    You took all the supplies in your house and kept on driving.
    Where will you go?
    CITY or COUNTRY SIDE?""")
    time.sleep(2)
    coc = input("\nCity or Country: ").lower()
    time.sleep(2)
    if coc == "city":
        city()
    elif coc == "country":
        country()
    else:
        print("\nWrong input. You are automatically dead.")
        gameOver()

def city():
    print("""
    You arrived in the city.
    As you are looking around, a huge group of zombies saw you and run after you.
    One zombie bites you and you turned into a zombie......
    (O.O)""")
    gameOver()

def country():
    print("""
    You are running out of fuel when you saw a smoke at a near forest.
    With all your strength left, you walked to that direction.
    You finally reach the source of the smoke, it is a fire pit made by people.
    You look around and see groups of people alive and well.
    They welcomed you with warm hugs until you hear a very familiar voice.
    It was your mother, behind her was all your family.
    THEY ARE ALIVE!""")
    winner()

def killZombies():
    print("""
    You are overwhelmed with so much zombies.
    You died horribly trying to be an action star..... HAHAHA""")
    gameOver()

def runAway():
    print("""
    You leave immediately to look for your family.
    Where will you go?
    City or Country side?""")
    time.sleep(2)
    corc = input("\nCity or Country: ").lower()
    time.sleep(2)
    if corc == "city":
        city()
    elif corc == "country":
        country()
    else:
        print("\nWrong input. You are automatically dead.")
        gameOver()

def takeHim():
    print("""
    You agreed to travel together and help one another to find your families or anyone alive.
    You found a car and now you are arguing whether to go to your own house or his house?""")
    time.sleep(2)
    yoh = input("\nYours or His: ").lower()
    time.sleep(2)
    if yoh == "yours":
        myHome()
    
def hisHome():
    print("""
    You entered his house only to find that all his family members turned into zombies.
    The door behind you gets jammed and you are trapped inside.
    You died together fighting side by side..... (T.T)""")
    gameOver()

def leaveHim():
    print("""
    You tell him that he can't come with you.
    As you are walking away, he stabbed you and you died on the spot. 
    The taste of KARMA he said.""")
    gameOver()

def gameOver():
    time.sleep(4)
    print(f"\nYou lost your life, {player}.\nCongratulations on reaching this far.\nPlease play again sometime.")
    time.sleep(2)
    print("""
            
        G A M E   O V E R !
            
            """)
    time.sleep(2)
    playAgain()

def winner():
    time.sleep(5)
    print(f"\n\nCongratulations, {player}!!!\n\nYou finally found your family.\nYou stayed together and waited for help and for everything to go back to normal.\nYou lived happily and see the future together. :)")
    time.sleep(3)
    print("""
            
         -----E N D  OF  W A L K I N G  D E A D-----
            
        """)
    time.sleep(2)
    print("Please stay tuned........ for more thrilling and exciting games.")

def playAgain():
    print("\nDo you want to play again?")
    answer = input(f"yes or no: ").lower()
    if answer == "yes":
        return introScene()
    if answer == "no":
        time.sleep(1)
        print("\nOkay. Come again if you want to play!")



#main program
print("""
HALLOWEEN GAME

--------------

W A L K I N G   D E A D

""")
time.sleep(2)

print("\nThis game is for 13 years old and above. Some scenes are not suitable for children.")
time.sleep(2)

player = input("\nWelcome to HALLOWEEN GAME: WALKING DEAD!\n\nPlease Enter your Name: ")
time.sleep(2)

print(f"\nAre you ready to play the WALKING DEAD, {player}?")
answer = input("yes or no: ").lower()
time.sleep(2)

if answer == "yes":
    print(f"\nLet's start! Best of luck to you {player}!!!")
    time.sleep(1)
    print("Remember, if you type a wrong choice it will cost your life in the game.\nChoose wisely :)")
    time.sleep(4)

    introScene()

elif answer == "no":
    time.sleep(1)
    print("\nOkay. Come again if you want to play!")
