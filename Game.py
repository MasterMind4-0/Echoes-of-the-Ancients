# This code is made by MasterMind4-0
# Hello!


import time
import sys
import random

Name = "You don't have a name ￣へ￣"
tsquestS = False
outsideF = False
questfailed = False
lockedopen = False
doctors = False
gavecoin = False
Villagename = False
devtools = False
visit_rec = False
free = False
health = 20
damagemod = 0
greetings = ["Hello!", "How do you do?", "Hi", "What?"]
btgreetings = ["What is it today?", "Take your pick.", "Welcome.", "Anything your willing to drink?", "What would you like this fine evening?"]
inventory = []
coinbag = 0
weapons = ["Fists - 2 Damage", ]
achievements = []
c1 = "\033[3mSophia: \033[0m"
c2 = "man"
c3 = "\033[3mThor the Blacksmith: \033[0m"
c4 = "\033[3mTheo the Merchant: \033[0m"
bt = "\033[3mBartender: \033[0m"
bs = "\033[3mBlacksmith: \033[0m"
un = "\033[3mUnknown: \033[0m"
dr = "\033[3mDoctor: \033[0m"
mc = "\033[3mMerchant: \033[0m"
drunk1 = 5
drunk2 = 5
drunk3 = 5
drunk = "\033[3mDrunk\033[0m"

def character_customization():
    Name = input("Hello, what would you like your name to be?: ")
    Choice = input(f"Great! So your name is {Name}? (Y/N)\n")

    if Choice.upper() == "Y":
        print("Great! Now let's continue...")
    elif Choice.lower() == "dev":
        global devtools
        devtools = True
        print("DevTools enabled!")
        character_customization()
    else:
        T = input("Oh. Ok, so would you like to restart? (Y/N)\n")
        if T.lower() == "y":
            print("Ok! Here:")
            return character_customization()
        elif T.lower() == "n":
            print("Um, ok? I'll quit for you.")
            time.sleep(2)
            sys.exit()
        else:
            print('Invalid, ending game. :)')
            sys.exit()

    return Name

def wait():
        sys.stdout.write('.\n')
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('..\n')
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('...\n')
        sys.stdout.flush()
        time.sleep(1)
    
def CC1():
    print("As you get up, you nearly fall, you look at yourself. You have bandaged wounds all over.")
    time.sleep(2)
    T = input("Once you stabilize yourself, you go to the door. Opening it reveals two ways, left, or right.\n")

    if T.lower() == 'right':
        print('\033[3m"Right"\033[0m you think to yourself.')
        MainHos()

    elif T.lower() == 'left':
        print('\033[3m"Ok, definitely left,"\033[0m you think to yourself as you start heading left.')

    else:
        print('Invalid, ending game. :)')
        sys.exit()

def CC1V():
    T = input("You go to the door. Opening it reveals two ways, left, or right.\n")

    if T.lower() == 'right':
        print('\033[3m"Right"\033[0m you think to yourself.')
        time.sleep(2)
        MainHos()

    if T.lower() == 'left':
        print('\033[3m"Ok, definitely left,"\033[0m you think to yourself as you start heading left.')
        time.sleep(2)
        LockedDoor()

def CC2():
    print("You decide to wait for Sophia and the doctor.")
    time.sleep(2)
    wait()
    print("After some time, Sophia enters with a tall, dark-haired man, who you assume is the doctor.")
    doctor()

def CC3():
    global coinbag
    coinbag = coinbag + 1
    print('\033[3m"I will dig through the dresser!"\033[0m')
    time.sleep(2)
    print('You look through the dresser,')
    time.sleep(2)
    print('besides doctor stuff, you find a singular coin.')
    time.sleep(2)
    print('###--- You have found \033[3mCoin\033[0m! ---###')

def RoomHos():
    global doctors, gavecoin, coinbag
    wait()
    print("You enter the room you started in...")
    time.sleep(2)

    if visit_rec and doctors == False:
        doctors = True
        print("As you enter, you see Sophia back where she was sitting, with a tall, dark-haired man.")
        doctor()

    if 1 > coinbag and doctors == False and gavecoin:
        Choice51 = input("Walk out of the room or wait for Sophia (1 or 2?): \n")

        if Choice51 == "1":
            CC1V()
        elif Choice51 == "2":
            CC2()
        else:
            print('Invalid, ending game. :)')
            sys.exit()
    elif 1 > coinbag and doctors == False and gavecoin == False:
        Choice51 = input("Walk out of the room, wait for Sophia, or search the dresser? (1, 2, or 3?): \n")

        if Choice51 == "1":
            CC1V()
        elif Choice51 == "2":
            CC2()
        elif Choice51 == "3":
            CC3()
            time.sleep(2)
            RoomHos()
        else:
            print('Invalid, ending game. :)')
            sys.exit()
    if 1 > coinbag and doctors and gavecoin:
        Choice51 = input("Walk out of the room? (1?): \n")

        if Choice51 == "1":
            CC1V()

        else:
            print('Invalid, ending game. :)')
            sys.exit()
    elif 1 > coinbag and doctors and gavecoin == False:
        Choice51 = input("Walk out of the room or search the dresser? (1 or 2?): \n")

        if Choice51 == "1":
            CC1V()

        elif Choice51 == "2":
            CC3()
            time.sleep(2)
            RoomHos()       
        else:
            print('Invalid, ending game. :)')
            sys.exit() 
    if 1 <= coinbag and doctors == False and gavecoin:
        Choice51 = input("Walk out of the room or wait for Sophia? (1 or 2?): \n")

        if Choice51 == "1":
            CC1V()
        elif Choice51 == "2":
            CC2()
        else:
            print('Invalid, ending game. :)')
            sys.exit()
    elif 1 <= coinbag and doctors == False and gavecoin == False:
        Choice51 = input("Walk out of the room or wait for Sophia, (1 or 2?): \n")

        if Choice51 == "1":
            CC1V()
        elif Choice51 == "2":
            CC2()
        else:
            print('Invalid, ending game. :)')
            sys.exit()
    if 1 <= coinbag and doctors and gavecoin:
        Choice51 = input("Walk out of the room (1?): \n")

        if Choice51 == "1":
            CC1V()
        else:
            print('Invalid, ending game. :)')
            sys.exit()

    elif 1 <= coinbag and doctors and gavecoin == False:
        Choice51 = input("Walk out of the room (1?): \n")

        if Choice51 == "1":
            CC1V()
        else:
            print('Invalid, ending game. :)')
            sys.exit()

def MainHos():
    wait()
    global visit_rec, free, gavecoin, coinbag
    if 1 < coinbag and free == False:
        print("You walk into the house's main room. There is a desk with a person sitting there. He notices you looking at him.")
        print(f"{un}Hey! You're not supposed to be here! Go to your room please.")
        RoomHos()
    elif 1 >= coinbag and free == False:
        print("You walk into the house's main room. There is a desk with a person sitting there. He notices you looking at him.")
        choice3 = input("He eyes the coin you're holding. Then he looks directly at you. (Give or not?)\n")
        if choice3.lower() == "give":
            gavecoin = True
            visit_rec = True
            free = True
            coinbag = coinbag-1
            print("You toss the coin at him, he catches it.")
            time.sleep(2)
            print(f"{un} You're free to go.\nHe smiles.")
            time.sleep(2)
            print('###--- You have lost \033[3mCoin\033[0m! ---###')
            MainHosV()
        elif choice3.lower() == "not":
            visit_rec = True
            free = False
            print("He glares at you,")
            time.sleep(2)
            RoomHos()
        else:
            print('You had one job')
            sys.exit()
    elif free is True:
        print("You walk into the house's main room. There is a desk with a person sitting there. He notices you looking at him.")
        time.sleep(2)
        print("He smiles at you.")
        MainHosV()

def MainHosV():
    T = input("You can: go outside or go back to your room. (Outside or room?)\n")
    
    if T.lower() == "outside":
        print('You decided to go outside.')
        outside()
    
    elif T.lower() == "room":
        print('\033[3m"I think I like the comfort of my room."\033[0m')
        time.sleep(2)
        MainHosV2()

def MainHosV2():
    global coinbag
    print("Before you even think of going back to your room,")
    time.sleep(2)
    print("The man suddenly gasps,")
    time.sleep(2)
    print(f"{un}Oh darn it! I forgot to put out the fire in my house!")
    time.sleep(2)
    print('He then runs right outside, out of sight. Screaming, "PLEASE NO!!!!!"')
    time.sleep(2)
    T = input('His desk is free to snoop around, should you? Or should you go to the room? (Snoop or room?)\n')

    if T.lower() == "snoop":
        print('\033[3m"No harm in simply looking..."\033[0m')
        time.sleep(2)
        if gavecoin == True:
            print("You open the drawers, you find a key and your coin.")
        
        elif gavecoin == False:
            print('You open the drawers to find a key.')
    
        T = input('\033[3m"Should I take it...?\033[0m (Y/N?)\n')

        if T.lower() == "y" and gavecoin == True:
            coinbag = coinbag+1
            inventory.append('Key')
            print('###--- You have found \033[3mCoin\033[0m! ---###')
            print('###--- You have found \033[3mKey\033[0m! ---###')
            print('\033[3m"I should head to my room with this stuff..."\033[0m')
            RoomHos()

        if T.lower() == "y" and gavecoin == False:
            inventory.append("Key")
            print('###--- You have found \033[3mKey\033[0m! ---###')
            print('\033[3m"I should head to my room with this..."\033[0m')
            RoomHos()

        if T.lower() == "n":
            print('\033[3m"I should not."\033[0m')
            time.sleep(2)
            print('\033[3mYou decide to go back to your room...\033[0m')
            RoomHos()

    elif T.lower == "room":
        print('\033[3m"I think I like the comfort of my room."\033[0m')
        time.sleep(2)
        RoomHos()

def LockedDoor():
    global lockedopen
    wait()
    Choice50 = input("You come to a dead end, the only thing that's there is a door. (Open or not?)\n")

    if Choice50.lower() == "open" and "Key" not in inventory and lockedopen == False:
        print("You try to open the door, but it is locked.")
        time.sleep(2)
        print('\033[3m"Guess I will head the other way,"\033[0m you turn around and walk forward.')
        MainHos()
    elif Choice50.lower() == "open" and "Key" in inventory and lockedopen == False:
        lockedopen = True
        inventory.remove('Key')
        print("You open the door.")
        print('###--- You have lost \033[3mKey\033[0m! ---###')
        office()
    elif Choice50.lower() == "open" and lockedopen:
        print('You open the door.')
        office()
    elif Choice50.lower() == "not":
        print('\033[3m"I do not think so,"\033[0m you turn around and walk forward.')
        MainHos()
    else:
        print('Invalid, ending game. :)')
        sys.exit()

def office():
    global coinbag
    wait()
    print("You find yourself in a damp room. There is one single torch lighting the room.")
    time.sleep(2)
    T = input("You see a desk, bookshelf, and table holding various doctor tools. (1, 2, or 3?)\n")

    if T == '1':
        coinbag = coinbag+1
        print("You walk to the desk, there are papers on it, with a fitting bottle of ink and quill. As well as a coin.")
        time.sleep(2)
        print('###--- you have found \033[3mCoin\033[0m! ---###')
        time.sleep(2)
        T = input('Do you look at the papers? (Y/N?)\n')

        if T.lower() == "y":
            print('\033[3m"I wonder what is on these things..."\033[0m')
            time.sleep(2)
            print("\033[3mYou read...\033[0m")
            time.sleep(2)
            print(f"\033[3mMy patient {Name} is doing well, {Name} held up pretty well to the wounds. They're partner, Sophia, oddly does not want to tell how they get their wounds. I understand the hardship, but her telling me would greatly help me recover him. Either way I do what I must...\033[0m")
            time.sleep(5)
            print('\033[3m"The rest is just doctor notes, this information is interesting regardless..."\033[0m')

   
        elif T.lower() == "n":
            print('\033[3m"I' + "ain't" + 'reading all that.\033[0m')

        else:
            print('Invalid, ending game. :)')
            sys.exit()

    elif T == "2":
        print('\033[3m"There has to be a secret door here..."\033[0m')
        time.sleep(2)
        print('You then spend hours checking each and every book...')
        wait()
        print("...To find out, that there is nothing.")

    elif T == "3":
        print('\033[3m"I wonder what is on that table..."\033[0m')
        time.sleep(2)
        print('The table holds:\nWounded man charts, anesthetics, bloodletting tools, arrow pullers and other strange, odd machinery.')
        time.sleep(3)

    else:
        print('Invalid, ending game. :)')
        sys.exit()

    T = input('\033[3m"Should I leave or continue?"\033[0m (Leave or continue?)\n')

    if T.lower() == "leave":
        RoomHos()
    elif T.lower() == "continue":
        office()
    else:
        print('Invalid, ending game. :)')
        sys.exit()

def RoomHosF():
    if 1 > coinbag:
        Choice51 = input("Get up and walk out of the room, wait for Sophia, or search the dresser? (1, 2, or 3?): \n")

    elif 1 <= coinbag:
        Choice51 = input("Get up and walk out of the room or wait for Sophia (1 or 2?): \n")

    if Choice51 == "1":
        CC1V()
    elif Choice51 == "2":
        CC2()
    elif Choice51 == "3" and 1 > coinbag:
        CC3()
        time.sleep(2)
        RoomHos()
    else:
        print('Invalid, ending game. :)')
        sys.exit()

def doctor():
    doctors = True
    print(f"{dr}Well, you look...")
    time.sleep(2)
    print("\033[3mHe studies you\033[0m.")
    time.sleep(2)
    print(f"{dr}In pretty fine condition. I think they're ready to leave don't you think Sophia?")
    time.sleep(3)
    print("Sophia looks at you, and then turns to the doctor.")
    time.sleep(2)

    Choice = input(f"{c1}I think they're ready doctor. You feel fine right {Name}? (Y/N?)\n")

    if Choice.lower() == 'y':
        global free
        free = True
        print(f"{Name}: I think I'm fine doctor.")
        time.sleep(2)
        print(f"{dr}That is simply wonderful to hear, you're welcome to leave at anytime.")
        time.sleep(3)
        print(f"{dr}Let me take you to our entrance.")
        MainHos()
    elif Choice.lower() == 'n':
        print(f"{Name}: No, I think I'm dying. \n You say weakly.")
        time.sleep(2)
        print('Suddenly you collapse to the ground and start coughing.')
        time.sleep(2)
        print("Blood in your hand is the last thing you see...")
        time.sleep(2)
        print('YOU DIED')
        sys.exit()
    else:
        print('Invalid, ending game. :)')
        sys.exit()

def outsideF():
    wait()


    time.sleep(2)
    T = input("You can head to the Drunken Kraken Tavern, the blacksmith, or the town square. (1, 2, or 3?)\n")

    if T == "1":
        DKtavernF()

    elif T == "2":
        blacksmith()

    elif T == "3":
        towns()

    else:
        print('Invalid, ending game. :)')
        sys.exit()

def outside():
    global outsideF
    wait()
    if outsideF == False:
        print("You walk outside, the light blinds you.")
        time.sleep(2)

        if Villagename == True:
            print("You find yourself in the Tishun Village.")
            time.sleep(2)
            print("You look at the sign pointing in various directions.")

        elif Villagename == False:
            print("You find yourself in a village.")
            time.sleep(2)
            print("You look at the sign pointing in various directions.")

            print("You look at the sign pointing in various directions.")
            time.sleep(2)
            T = input("You can head to the Drunken Kraken Tavern, the blacksmith, or the town square. (1, 2, or 3?)\n")

            if T == "1":
                DKtavern()

            elif T == "2":
                blacksmith()

            elif T == "3":
                towns()

            else:
                print('Invalid, ending game. :)')
                sys.exit()
    elif outsideF:
        # MM
        print("You look at the sign pointing in various directions.")
        time.sleep(2)
        T = input("You can head to the Drunken Kraken Tavern, the blacksmith, or the town square. (1, 2, or 3?)\n")

        if T == "1":
            DKtavern()

        elif T == "2":
            blacksmith()

        elif T == "3":
            towns()

        else:
            print('Invalid, ending game. :)')
            sys.exit()

def barfight():
    global health, drunk, drunk1, drunk2, drunk3, s1, c2, damagemod, coinbag
    wait()
    if health <= 0:
        print('YOU DIED')
        sys.exit()
    if drunk1 <= 0 and drunk2 <= 0 and drunk3 <= 0:
        health = 20
        drunk1 = 5
        drunk2 = 5
        drunk3 = 5
        inventory.append('Beer')
        coinbag = coinbag+1
        print('You won the fight!')
        print("###--- You have found \033[3mCoin\033[0m! ---###")
        print('###--- You have found \033[3mBeer\033[0m! ---###')
        outside()
    print('Prepare for battle...')
    print("Some foes approach you.")
    if drunk1 > 0 and drunk2 > 0 and drunk3 > 0:
        T = input(f"Who do you pick to fight? {drunk}1, {drunk}2, or {drunk}3? (1, 2, or 3?)\n")
    elif drunk1 <=0 and drunk2 > 0 and drunk3 > 0:
        T = input(f"Who do you pick to fight? {drunk}2 or {drunk}3? (2 or 3?)\n")
    elif drunk1 <=0 and drunk2 <=0 and drunk3 > 0:
        T = input(f"Who do you pick to fight? {drunk}3? (3?)\n")
    elif drunk1 > 0 and drunk2 <=0 and drunk3 > 0:
        T = input(f"Who do you pick to fight? {drunk}1 or {drunk}3? (1 or 3?)\n")
    elif drunk1 > 0 and drunk2 <= 0 and drunk3 <= 0:
        T = input(f"Who do you pick to fight? {drunk}1? (1?)\n")
    elif drunk1 <= 0 and drunk2 > 0 and drunk3 <= 0:
        T = input(f"Who do you pick to fight? {drunk}2? (2?)\n")

    if T == "1":
        print(f'You pick {drunk}1!')
        time.sleep(2)
        print('Remember, you can only use your fists...')
        time.sleep(2)
        T = "fists"
        if T.lower() == "fists":
            print('You picked Fists!')
            time.sleep(2)
            T = random.randint(0, 10)
            if T >= drunk1:
                drunk1 = drunk1-2
                drunk1 = drunk1-damagemod
                print(f'You hit and dealt {2+damagemod} damage!')
                barfight()

            elif T < drunk1:
                health = health-2
                print(f'You missed and gave the {drunk}1 an opportunity to hit!')
                time.sleep(1)
                print('You take 2 damage!')
                barfight()
        else:
            print('Invalid, ending game. Enter fists next time :)')
            sys.exit()

    elif T == "2":
        print(f'You pick {drunk}2!')
        time.sleep(2)
        print('Remember, you can only use your fists...')
        time.sleep(2)
        print('Pick your weapon...')
        time.sleep(2)
        T = "fists"
        if T.lower() == "fists":
            print('You picked Fists!')
            time.sleep(2)
            T = random.randint(0, 10)
            if T >= drunk2:
                drunk2 = drunk2-2
                drunk2 = drunk2-damagemod
                print(f'You hit and dealt {2+damagemod} damage!')
                barfight()

            elif T < drunk2:
                health = health-2
                print(f'You missed and gave the {drunk}2 an opportunity to hit!')
                time.sleep(1)
                print('You take 2 damage!')
                barfight()
        else:
            print('Invalid, ending game. Enter fists next time :)')
            sys.exit()

    elif T == "3":
        print(f'You pick {drunk}3!')
        time.sleep(2)
        print('Remember, you can only use your fists...')
        time.sleep(2)
        print('Pick your weapon...')
        time.sleep(2)
        T = "fists"
        if T.lower() == "fists":
            print('You picked Fists!')
            time.sleep(2)
            T = random.randint(0, 10)
            if T >= drunk3:
                drunk3 = drunk3-2
                drunk3 = drunk3-damagemod
                print(f'You hit and dealt {2+damagemod} damage!')
                barfight()

            elif T < drunk3:
                health = health-2
                print(f'You missed and gave the {drunk}3 an opportunity to hit!')
                time.sleep(1)
                print('You take 2 damage!')
                barfight()
        else:
            print('Invalid, ending game. Enter fists next time :)')
            sys.exit()

    else:
        print('Invalid, ending game. :)')
        sys.exit()

def DKtavernF():
    print('\033[3m"A tavern sounds good."\033[0m You rub your belly.')
    time.sleep(2)
    wait()
    print('As you enter the tavern, you quickly duck down. You watch in terror as a chair flies above you seemingly in slow motion.')
    time.sleep(3)
    print('You recover yourself and look into the tavern. You see a full on brawl, people bashing glasses into others and others smashing people with their fists!')
    barfight()

def DKtavern():
    wait()
    print('You enter the tavern.')
    time.sleep(2)
    print('The aroma of beer and food insteatly hits your nose.')
    time.sleep(2)
    print('Both making you sick and hungry.')
    time.sleep(2)
    DKtavern1()

def DKtavern1():
        global c2
        T = random.randint(1, 40)

        if T < 10:
            barfight()
    
        elif T >= 10:
            Choice = input('Walk to the bartender, talk to some folk, or leave? (1, 2 ,or 3?)\n')

        if Choice == '1':
            print('\033[3m"Let me see what the bartender offers."\033[0m')
            bartender()
    
        elif Choice == "2":
            T = random.randint(1, 10)
            if T < 5:
                c2 = "man"
            elif T > 5:
                c2 = "woman"
            print(f"{Name}: Hey! You there!")
            time.sleep(2)
            print(f'A {c2} looks at you.')
            time.sleep(2)
            print(f'{un}What do you want?')
            bartalk()

        elif Choice == "3":
            print('\033[3m"Nope, not today."\033[0m')
            time.sleep(2)
            print('You turn around and walk straight out.')
            outside()

        else:
            print('Invalid, ending game. :)')
            sys.exit()

def bartalk():
    global s1, c2
    T = random.randint(1, 5)
    wait()
    print(f'\033[3mYou sit next to the {c2}\033[0m.')
    if T == "1":
        s1 = print(f'{un}So, what brings you here?')
    elif T == '2':
        s1 = print(f'{un}Hi?')
    elif T == "3":
        s1 = print(f'{un}So, why me?')
    elif T == "4":
        s1 = print(f'{un}So, why are you talking to me?')
    elif T == "5":
        s1 = print(f'The {c2} grumbles.')
    time.sleep(2)
    print(s1)
    time.sleep(2)
    bartalk2()

def bartalk2():
    global c2
    T = "\033[3mUnknown\033[0m"
    y1 = input('Where am I, who are you, what do they sell, or leave? (1, 2, 3, or 4?)\n')

    if y1 == "1":
        print(f"{T}: Welcome to \033[3mTishun Village\033[0m.")
        time.sleep(2)
        print(f'{T}: I guess it is pretty cool...')
        bartalk(2)
    elif y1 == "2":
        if c2.lower() == "man":
            names = ["Bouldermore", "Kourayue", "Firestarter", "Musk", "Picking"]

        elif c2.lower() == "woman":
            names = ["Shara", "Locus", "Sophia", "Picking", "Acadia"]
        T = random.choice(names)
        print(f"{T}: The name is {T}.")
        if T.lower() == "sophia":
            print(f"{Name}: Hey I know someone as Sophia!")
            time.sleep(2)
            print(f'{T}: Cool?')
            bartalk2()

    elif y1 == "3":
        print(f"The {c2} looks at you dead in the eyes.")
        time.sleep(2)
        print(f"{T}: BEER")
        time.sleep(2)
        print(f"{T}: ...And some food.")
        time.sleep(2)
        print(f"{T}: I heard he is even looking for a hire.")
        bartalk2()
    
    elif y1 == "4":
        print(f'{Name} Thanks for the talk. \nYou say as you leave.')
        time.sleep(2)
        DKtavern1()

    else:
        print('Invalid, ending game. :)')
        sys.exit()

def bartender():
    T = random.choice(btgreetings)
    wait()
    print('\033[3mYou walk toward the bartender...\033[0m')
    time.sleep(2)
    print(bt + T)
    bartenderdrinks()

def bartenderdrinks():
    global coinbag
    wait()
    T = input(f'''
TAVERN

Beer - 1 Coin
Stewed Mushrooms - 2 Coins

If you want to leave, type L
              
Your inventory: {inventory}
Your pouch: {coinbag}\n
 ''')
    if T.lower() == "beer":
        if 1 <= coinbag:
            inventory.append('Beer')
            coinbag = coinbag-1
            print("You've purchased beer!")
            print('###--- You have found \033[3mBeer\033[0m! ---###')
            bartenderdrinks()

        elif 1 > coinbag:
            print("You don't have enough coins!")
            bartenderdrinks()
        
    elif T.lower() == "stewed mushrooms":
        if 2 <= coinbag:
            inventory.append('Stewed Mushrooms')
            coinbag = coinbag-2
            print('You purchased Stewed Mushrooms!')
            print('###--- You have found \033[3mStewed Mushrooms\033[0m! ---###')
            bartenderdrinks()
        elif 2 > coinbag:
            print("You don't have enough coins!")
            bartenderdrinks()

    elif T.lower() == "l" or "leave":
        print(f"{Name}: I'm ok.")
        time.sleep(2)
        print("\033[3mYou walk out of the bar...\033[0m")
        outside()

    else:
        print('Invalid, ending game. :)')
        sys.exit()

def blacksmith():
    print('\033[3mlet us see what the blacksmith holds."\033[0m')
    blacksmithint()

def blacksmithint():
    global coinbag
    wait()
    print('\033[3mYou enter the blacksmith...\033[0m')
    time.sleep(2)
    print(f'{un}Hey there!')
    time.sleep(2)
    print('\033[3mYou look up, seeing a man with a black apron. He wipes the sweat of his forehead before continuing what he was saying.\033[0m')
    time.sleep(3)
    print(f"{bs}Sorry,")
    time.sleep(2)
    print('He pauses,')
    time.sleep(2)
    print(f"{bs}What would you like?")
    T = input('Shop or leave?')
    if T.lower() == 'shop':
        print(f"{bs}Great to hear!")
        blacksmithitems()
    elif T.lower() == 'leave' or 'l':
        print(f'{bs}Well, comoe back if you require anything!')
        time.sleep(2)
        print('He yells as you leave...')
        outside()
    else:
        print('Invalid, ending game. :)')
        sys.exit()

def blacksmithitems():
    global health, inventory, weapons, coinbag
    wait()
    T = input(f'''
BLACKSMITH

Dagger - 4 Damage - 5 Coin
Shield - +5 Health - 5 Coin
Armor - +10 Health - 10 Coins

If you want to leave, type L
              
Your inventory: {inventory}
Your pouch: {coinbag}
Your weapons: {weapons}
Your health: {health}\n
 ''')
    if T.lower() == "dagger":
        if 5 <= coinbag:
            weapons.append('Dagger - 4 Damage')
            coinbag = coinbag-5
            print("You've purchased Dagger!")
            print('###--- You have found \033[3mDagger\033[0m! ---###')
            blacksmithitems()
        elif 5 > coinbag:
            print("You don't have enough coins!")
            blacksmithitems()
        
    elif T.lower() == "shield":
        if 5 <= coinbag:
            weapons.append('Shield')
            coinbag = coinbag-5
            health = health+5
            print('You purchased Shield!')
            print('###--- You have found \033[3mShield\033[0m! ---###')
            blacksmithitems()
        elif 5 > coinbag:
            print("You don't have enough coins!")
            blacksmithitems()

    elif T.lower() == "armor":
        if 10 <= coinbag:
            weapons.append('Armor')
            coinbag = coinbag-10
            health = health+10
            print('You purchased Armor!')
            print('###--- You have found \033[3mArmor\033[0m! ---###')
            blacksmithitems()
        elif 10 > coinbag:
            print("You don't have enough coins!")
            blacksmithitems()

    elif T.lower() == "l" or "leave":
        print(f"{Name}: I'm ok.")
        time.sleep(2)
        print("\033[3mYou walk out of the blacksmith...\033[0m")
        outside()

    else:
        print('Invalid, ending game. :)')
        sys.exit()

def towns():
    global questfailed, tsquestS, coinbag
    print('\033[3mYou enter the town square.\033[0m')
    time.sleep(2)
    if questfailed:
        print('The place is filled with markets stands and people.')
        townsn()
    elif questfailed == False:
        tsquestS = True
        print('The place is filled with market stands and people. One of the owners of a stands calls out to you...')
        time.sleep(2)
        print('\033[3m"He seems familiar..."\033[0m')
        wait()
        questmark()
    elif tsquestS:
        print('As you enter Theo runs toward you.')
        time.sleep(2)
        print(f'{c4}{Name}! {Name}!')
        time.sleep(2)
        print('You stop and face him.')
        time.sleep(2)
        print(f'{c4}Thank goodness I caught up to you partner.')
        time.sleep(2)
        print('He finally catches his breath.')
        time.sleep(2)
        print(f'{c4}I need a favor. A small one oh please!')
        T = input("I should probably help him, or should I? (Help or not?)\n")
        if T.lower() == 'help':
            print(f'{c4}THANK YOU!')
            time.sleep(1)
            print('He practically screams,')
            time.sleep(2)
            print(f"{c4}I need you to head to the blacksmith, he has some \033[3mWonderful\033[0m items that I must replenish at my stand!")
            T = input(f'{c4}Do you think you can do that? (Y/N?)\n')
            if T.lower() == 'y':
                coinbag = coinbag+30
                print(f'{c4}Thank you! Thank you! Thank you! THANK YOU!')
                time.sleep(1)
                print('He shakes your hand vigorously.')
                time.sleep(2)
                print(f'Here is some money that you can use to buy the items.')
                time.sleep(2)
                print('He fills your hands with coins.')
                time.sleep(2)
                print(f'{c4}That should be enough.')
                time.sleep(1)
                print('###--- You have found \033[3m30 Coins\033[0m! ---###')
                time.sleep(2)
                print(f'{c4}See me when you have gotten those \033[3marmor\033[0m pieces!')
                time.sleep(2)
                print('Quest: Buy three armor sets from the blacksmith')
                outside()
            elif T.lower() == "n":
                questfailed = True
                print(f'{c4}Oh... Ok.')
                time.sleep(2)
                print('Theo sighs and returns to his stand.')
                time.sleep(2)
                print('\033[3m"I do not think I will see him again..."\033[0m')
                outside()
            else:
                print('You had one job')
                sys.exit()
        elif T.lower() == "n":
            questfailed = True
            print(f'{c4}Oh... Ok.')
            time.sleep(2)
            print('Theo sighs and returns to his stand.')
            time.sleep(2)
            print('\033[3m"I do not think I will see him again..."\033[0m')
            outside()
        else:
            print('You had one job...')
            sys.exit()
    elif tsquestS and "Armor" *3 in inventory:
        inventory.append('Armor')
        inventory.append('Armor')
        inventory.append('Armor')
        print('Theo runs toward you.')
        time.sleep(2)
        print(f'{c4}My armor!')
        time.sleep(1)
        print(f'{c4}Thank you! Thank you!')
        time.sleep(2)
        print(f'{c4}Ok, follow me-')
        time.sleep(1)
        print('He guides you to his stand,')
        time.sleep(2)
        print(f'{c4}Ok, thank you!')
        time.sleep(1)
        print(f'{c4}Yes! Wonderful! Ok, ok.')
        T = input(f'{c4}Ah! How about you keep one of these armor sets? (Y/N?)\n')
        if T.lower() == "y":
            inventory.append("Armor")
            print(f'{c4}Well, thank you for your assistance!')
            print('###--- You have found \033[3mArmor\033[0m! ---###')
            outside()
        elif T.lower() == 'n':
            print('He looks at you.')
            if "Armor" in inventory:
                print(f'{c4}Ah, I see your wearing one. Well, um, good luck then!')
                outside()
            elif "Armor" not in inventory:
                print(f'{c4}Well, ok. Best of luck!')
                outside()
        else:
            print('You had one job')
            sys.exit()

def townsn():
    wait()

def questmark():
    global mc, Name, questfailed, health, damagemod, inventory, achievements
    time.sleep(2)
    print(f'{mc}Hello! How you doing pal?!')
    T = input('"Who are you?"' + 'or' + '"Good" (1 or 2?)\n')
    if T == "1":
        questfailed = True
        print(f"{Name}: Who are you?")
        time.sleep(2)
        print(f"{mc}That is gre-")
        time.sleep(1)
        print('He pauses seemingly out of disbelief.')
        time.sleep(2)
        print(f"{mc}You don't... remember me?")
        time.sleep(2)
        print('His voice cracks with sadness.')
        time.sleep(2)
        print('He walks from behind the counter.')
        time.sleep(2)
        print('He places his hands on your shoulders.')
        time.sleep(2)
        print('\033[3m"What is happenening."\033[0m')
        time.sleep(2)
        print(f'{mc}What has made you fallen so hard?')
        time.sleep(2)
        print(f'{Name}: What..?')
        time.sleep(1)
        print('The merchant pats your back.')
        time.sleep(2)
        print(f'{mc}Good luck to you.')
        print('He says in a sorrow tone.')
        time.sleep(2)
        print('You leave out of both embarrassment and confusement.')
        outside()
    elif T == '2':
        print(f'{Name}: Good?')
        time.sleep(1)
        print(f'He smiles.')
        print(f'{mc}Wonderful my partner wonderful! I am doing quite good myself now.')
        time.sleep(2)
        print(f'{Name}: Great...')
        time.sleep(2)
        print('The merchant smiles.')
        time.sleep(2)
        print(f'{mc}Great to see you in good condition.')
        time.sleep(2)
        print('You smile awkwardly.')
        time.sleep(2)
        print(f'{mc}Your clothing...')
        time.sleep(2)
        print('He breathes through his teeth.')
        time.sleep(2)
        print(f"{mc}...I wouldn't say the same.")
        time.sleep(2)
        print(f"{mc}Well, nothing a wardrobe change can't fix!")
        print('He says with with a single finger raised as if he had thought of a ingenius idea.')
        time.sleep(4)
        print('He runs deeper into his stand... ...And then comes back with a few cloths.')
        time.sleep(2)
        print(f'{mc}Take your pick')
        print('He waves the cloths, revealing three separate clothes of numinous qualities.')
        T = input(f'''
CLOTHS

Iron-Claw Cloth
- +2 Damage
- +2 Health

Iron-Plate Cloth
- +4 Health

Vanity-Thimble Cloth
- Nothing (But you get to look cool, and who knows, it might get you some special reactions ¯\_( ͡° ͜ʖ ͡°)_/¯)

Your inventory: {inventory}\n
''')
        if T.lower() == 'iron-claw cloth':
            health = health+2
            damagemod = damagemod+2
            inventory.append('Iron-Claw Cloth')
            print('###--- You have found \033[3mIron-Claw Cloth\033[0m!')
        elif T.lower() == "iron-plate cloth":
            health = health+4
            inventory.append('Iron-Plate Cloth')
            print('###--- You have found \033[3mIron-Plate Cloth\033[0m!')
        elif T.lower() == 'vanity-thimble cloth':
            inventory.append('Vanity-Thimble Cloth')
            achievements.append("I'm cool now Mom!")
            print('###--- You have found \033[3mVanity-Thimble Cloth\033[0m!')
            print('###--- Achievement Unlocked!' + "\033[3mI'm cool now Mom\033[0m! ---###")
        else:
            print("You had one job...")
            sys.exit()

        print(f'{mc} Now \033[3mthat\033[0m is a good pick.')
        time.sleep(2)
        print(f'{Name}: Thanks!')
        time.sleep(2)
        print(f'{c4} Anytime friend! You can always come to me, \033[3mTheo\033[0m the Great for supplies!')
        print('\033[3mTheo says to come back anytime.\033[0m')
        outside()

Name = character_customization()
# Program Starts Here

wait()
print("You awake in a bed, the soft covers keeping you warm. You're in a room, fitted with a dresser and cobblestone walls.")
time.sleep(3)
print("Before you are able to do anything, you hear someone.")
time.sleep(2)
print(un + "Oh! Finally, you're awake!")
time.sleep(1)
T = input('"Where am I?" or "Who are you?" (1 or 2): ')

if T.lower() == "1":
    Villagename = True
    print(Name + ": Where am I?")
    time.sleep(2)
    print(un + "You don't remember do you? Well, welcome to \033[3mTishun Village\033[0m!")
    time.sleep(3)
    print('\033[3m"The name oddly rings a bell..."\033[0m')
    time.sleep(2)
elif T.lower() == "2":
    print(Name + ": Who are you?")
    time.sleep(2)
else:
    print('YOU HAD ONE JOB.')
    sys.exit()

print(c1 + "Oh! I'm \033[3mSophia\033[0m.")
time.sleep(2)
print('\033[3m"Sophia..."\033[0m')
time.sleep(2)
print("You nod understandingly.")
time.sleep(2)
print(c1 + "Ok, well, you'll be fine to leave soon. I just need to tell the doctor.")
time.sleep(3)
print("\033[3mSophia walks away...\033[0m")
time.sleep(1)
print("You look around to see what you're able to do.")
time.sleep(1)
RoomHosF()