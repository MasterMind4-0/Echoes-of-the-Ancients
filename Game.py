# This code is made by MasterMind4-0
# Hello!


import time
import sys
import random

Name = "You don't have a name ￣へ￣"
CheckedDraw = False
nextlevel = False
questf = False
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
snooped = False
snoopedD = False
DKtaverne = False
barhelp = False
health = 20
damagemod = 0
weaponsL = {
    'Dagger - 4 Damage': {'Damage': 4},
    "Fist - 2 Damage": {'Damage': 2},
    'Bow - 5 Damage': {'Damage': 5}
}
greetings = ["Hello!", "How do you do?", "Hi", "What?"]
btgreetings = ["What is it today?", "Take your pick.", "Welcome.", "Anything your willing to drink?", "What would you like this fine evening?"]
inventory = []
coinbag = 0
weapons = ["Fists - 2 Damage"]
achievements = []
names = []
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
goblin1 = 5
goblin2 = 5
goblin3 = 5
goblin4 = 5
drunk = "\033[3mDrunk\033[0m"
gob = "\033[3mGoblin\033[0m"

def character_customization():
    global devtools, coinbag, Name
    leave = False
    Name = input("Hello, what would you like your name to be?: ")
    Choice = input(f"Great! So your name is {Name}? (Y/N)\n")

    if Choice.upper() == "Y":
        print("Great! Now let's continue...")
    elif Choice.lower() == "dev":
        devtools = True
        print("DevTools enabled!")
        while leave == False:
            T = input('Enter code or l to leave:\n')
            if T.lower() == 'l':
                print('Leaving...')
                break
            elif T.lower() == 'money':
                coinbag = 10000
                print(f'Coinbag has {coinbag} coins.')
            elif T.lower() == 'out':
                outside()
            elif T.lower() == 'barfight':
                barfight()
            elif T.lower() == 'a new world':
                anewworld()
            elif T.lower() == 'wagon':
                wagon()
            else:
                print('Invaild')
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
        time.sleep(2)
        LockedDoor()

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
    global coinbag, CheckedDraw
    CheckedDraw = True
    coinbag = coinbag + 1
    print('\033[3m"I will dig through the dresser!"\033[0m')
    time.sleep(2)
    print('You look through the dresser,')
    time.sleep(2)
    print('besides doctor stuff, you find a singular coin.')
    time.sleep(2)
    print('###--- You have found \033[3mCoin\033[0m! ---###')

def RoomHos():
    global doctors, coinbag, CheckedDraw
    if CheckedDraw:
        wait()
    elif CheckedDraw == False:
        wait()
        print("You enter the room you started in...")
        time.sleep(2)

    if visit_rec and doctors == False:
        doctors = True
        print("As you enter, you see Sophia back where she was sitting, with a tall, dark-haired man.")
        doctor()

    if CheckedDraw and doctors == False and gavecoin:
        Choice51 = input("Walk out of the room or wait for Sophia (1 or 2?): \n")

        if Choice51 == "1":
            CC1V()
        elif Choice51 == "2":
            CC2()
        else:
            print('Invalid, ending game. :)')
            sys.exit()
    elif CheckedDraw == False and doctors == False and gavecoin == False:
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
    if CheckedDraw and doctors and gavecoin:
        Choice51 = input("Walk out of the room? (1?): \n")

        if Choice51 == "1":
            CC1V()

        else:
            print('Invalid, ending game. :)')
            sys.exit()
    elif CheckedDraw == False and doctors:
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
    if CheckedDraw and doctors == False:
        Choice51 = input("Walk out of the room or wait for Sophia? (1 or 2?): \n")

        if Choice51 == "1":
            CC1V()
        elif Choice51 == "2":
            CC2()
        else:
            print('Invalid, ending game. :)')
            sys.exit()
    elif CheckedDraw and doctors == False:
        Choice51 = input("Walk out of the room or wait for Sophia, (1 or 2?): \n")

        if Choice51 == "1":
            CC1V()
        elif Choice51 == "2":
            CC2()
        else:
            print('Invalid, ending game. :)')
            sys.exit()
    if CheckedDraw and doctors:
        Choice51 = input("Walk out of the room (1?): \n")

        if Choice51 == "1":
            CC1V()
        else:
            print('Invalid, ending game. :)')
            sys.exit()

    elif CheckedDraw and doctors:
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
    global coinbag, snooped
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
        if gavecoin and snooped:
            print('There is nothing here in the drawer.')
        elif gavecoin and snooped == False:
            snooped = True
            print("You open the drawers, you find a key and your coin.")
        elif gavecoin == False and snooped:
            print('There is nothing here in the drawer.')
        elif gavecoin == False and snooped == False:
            snooped = True
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
    global coinbag, snoopedD
    wait()
    print("You find yourself in a damp room. There is one single torch lighting the room.")
    time.sleep(2)
    T = input("You see a desk, bookshelf, and table holding various doctor tools. (1, 2, or 3?)\n")

    if T == '1':
        if snoopedD:
            coinbag = coinbag+1
            print("You walk to the desk, there are papers on it, with a fitting bottle of ink and quill. As well as a coin.")
            time.sleep(2)
            print('###--- you have found \033[3mCoin\033[0m! ---###')
            time.sleep(2)
            T = input('Do you look at the papers? (Y/N?)\n')
        elif snoopedD == False:
            snoopedD = True
            print("You walk to the desk, there are papers on it, with a fitting bottle of ink and quill. As well as a coin.")
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
            print('\033[3m"I ' + "ain't " + 'reading all that."\033[0m')

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

    if T.lower() == "leave" or T.lower() == "l":
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

def outside():
    global outsideF, DKtaverne
    wait()
    if outsideF:
        outsideF = False
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
    elif outsideF == False:
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
    global coinbag, drunk1, drunk2, drunk3, health, damagemod, inventory
    wait()
    while drunk1 > 0 or drunk2 > 0 or drunk3 > 0:
        if health <= 0:
            print('YOU DIED')
            sys.exit()
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
            time.sleep(.5)
            T = random.randint(0, 10)
            if T >= drunk1:
                drunk1 = drunk1-2
                drunk1 = drunk1-damagemod
                print(f'You hit and dealt {2+damagemod} damage!')
                time.sleep(.5)

            elif T < drunk1:
                health = health-2
                print(f'You missed and gave the {drunk}1 an opportunity to hit!')
                time.sleep(.5)
                print('You take 2 damage!')
                time.sleep(.5)

        elif T == "2":
            print(f'You pick {drunk}2!')
            time.sleep(.5)
            T = random.randint(0, 10)
            if T >= drunk2:
                drunk2 = drunk2-2
                drunk2 = drunk2-damagemod
                print(f'You hit and dealt {2+damagemod} damage!')
                time.sleep(.5)

            elif T < drunk2:
                health = health-2
                print(f'You missed and gave the {drunk}2 an opportunity to hit!')
                time.sleep(.5)
                print('You take 2 damage!')
                time.sleep(.5)

        elif T == "3":
            print(f'You pick {drunk}3!')
            time.sleep(.5)
            T = random.randint(0, 10)
            if T >= drunk3:
                drunk3 = drunk3-2
                drunk3 = drunk3-damagemod
                print(f'You hit and dealt {2+damagemod} damage!')
                time.sleep(.5)

            elif T < drunk3:
                health = health-2
                print(f'You missed and gave the {drunk}3 an opportunity to hit!')
                time.sleep(.5)
                print('You take 2 damage!')
                time.sleep(.5)

        else:
            print('Invalid, ending game. :)')
            sys.exit()
    
    health = 20
    drunk1 = 5
    drunk2 = 5
    drunk3 = 5
    inventory.append('Beer')
    coinbag = coinbag+1
    print('You won the fight!')
    print("###--- You have found \033[3mCoin\033[0m! ---###")
    print('###--- You have found \033[3mBeer\033[0m! ---###')
    bartender()
    
def DKtavernF():
    print('Suddenly, a chair flies above you seemingly in slow motion, you barely manange to quickly duck down.')
    time.sleep(3)
    print('You recover yourself and look into the tavern. You see a full on brawl, people bashing glasses into others and others smashing people with their fists!')
    barfight()

def DKtavern():
    global DKtaverne
    wait()
    if DKtaverne:
        print('You enter the tavern.')
        time.sleep(2)
        print('The aroma of beer and food insteatly hits your nose.')
        time.sleep(2)
        print('Both making you sick and hungry.')
        time.sleep(2)
        DKtavern1()
    else:
        DKtaverne = True
        DKtavernF()

def DKtavern1():
        global c2
        T = random.randint(1, 60)

        if T < 10:
            print('But soon you realize you walked yourself straight into a barfight.')
            barfight()
    
        elif T >= 10:
                Choice = input('Walk to the bartender, talk to some folk, or sit with a beer? (1, 2, or 3? L for leave.)\n')

        if Choice == '1':
            print('\033[3m"Let me see what the bartender offers."\033[0m')
            bartender()
    
        elif Choice == "2":
            c2 = random.randint(1, 2)
            if c2 == '1':
                c2 = 'man'
            else:
                c2 = 'woman'
            print(f"{Name}: Hey! You there!")
            time.sleep(2)
            print(f'A {c2} looks at you.')
            time.sleep(2)
            print(f'{un}What do you want?')
            bartalk()
        
        elif Choice == '3':
            DKtaverntable()
            
        elif Choice.lower() == "l":
            print('\033[3m"Nope, not today."\033[0m')
            time.sleep(2)
            print('You turn around and walk straight out.')
            outside()

        else:
            print('Invalid, ending game. :)')
            sys.exit()

def DKtaverntable():
    global coinbag, inventory, health
    print("\033[3mYou walk to a table...\033[0m")
    time.sleep(2)
    print('\033[3mAs you sit, a waitress walks over,\033[0m')
    time.sleep(2)
    if 'Beer' not in inventory:
        print('\033[3mWaitress\033[0m: Would you like a beer?')
        time.sleep(.5)
        print('She smiles,')
        time.sleep(2)
        T = input(f'''
TAVERN

Beer - 1 Coin #1
Stewed Mushrooms - 2 Coins #2

If you want to leave, type L
              
Your pouch: {coinbag}\n
''')
        if T.lower() == 'beer' or T == '1':
            if 1 <= coinbag:
                coinbag -= 1
                print("You've purchased beer!")
                print('You consume the beer.')
                bartenderdrinks()
            elif 1 > coinbag:
                print("\033[3mI don't have enough coins!\033[0m")
                time.sleep(2)
                print(f"\033[3m{Name}\033[0m: I'm afraid I don't have enough coins,")
                wait()
                print('\033[3mYou were kicked out...\033[0m')
                outside()
                

        elif T.lower() == "stewed mushrooms" or T == '2':
            if 2 <= coinbag:
                health = 20
                coinbag -= 2
                inventory.append('Stewed_Mushrooms')
                print('You purchased Stewed Mushrooms!')
                bartenderdrinks()
            elif 2 > coinbag:
                print("\033[3mI don't have enough coins!\033[0m")
                time.sleep(2)
                print(f"\033[3m{Name}\033[0m: I'm afraid I don't have enough coins,")
                wait()
                print('\033[3mYou were kicked out...\033[0m')
                outside()
            
        else:
            print(f"\033[3m{Name}\033[0m: I'm fine thank you.")
            time.sleep(2)
            print(f"\033[3mYou get up to leave the tavern.\033[0m")
            outside()
    
    elif 'Beer' in inventory:
        print("\033[3mWaitress\033[0m: Oh! Looks like you've already got a beer. Well, enjoy yourself.")
        time.sleep(2)
        print('You smile,')
        time.sleep(2)
        print('She leaves, leaving you and your beer.')
        time.sleep(2)
        while True:
            ABeer = inventory.count('Beer')
            if ABeer == 0:
                print('You are out of beer, you leave your table.')
                break
            elif ABeer > 0:
                T = input(f'You have {ABeer} in your inventory, would you like to consume one? (Y/N?)\n')
                if T.lower() == 'y':
                    inventory.remove('Beer')
                    ABeer = inventory.count('Beer')
                    print('You consume one beer from your inventory.')
                    time.sleep(2)
                    print(f'You have {ABeer} left...')
                    time.sleep(2)
                else:
                    print('\033[3mI think that is enough for now.\033[0m')
                    break
        time.sleep(2)
        print('You walk out of the tavern.')
        outside()

def bartalk():
    T = random.randint(1, 5)
    wait()
    print(f'You sit next to the {c2}.')
    if T == 1:
        s1 = print(f'{un}So, what brings you here?')
    elif T == 2:
        s1 = print(f'{un}Hi?')
    elif T == 3:
        s1 = print(f'{un}So, why me?')
    elif T == 4:
        s1 = print(f'{un}So, why are you talking to me?')
    elif T == 5:
        s1 = print(f'The {c2} grumbles.')
    time.sleep(2)
    s1
    time.sleep(2)
    bartalk2()

def bartalk2():
    nameKN = False
    while True:
        y1 = input('Where am I, who are you, what do they sell, or leave? (1, 2, 3, or 4?)\n')

        if y1 == "1":
            if nameKN == False:
                print(f"{un}Welcome to \033[3mTishun Village\033[0m.")
                time.sleep(2)
                print(f'{un}I guess it is pretty cool...')
            else:
                print(f"\033[3m{name__c}\033[0m: Welcome to \033[3mTishun Village\033[0m.")
                time.sleep(2)
                print(f'\033[3m{name__c}\033[0m: I guess it is pretty cool...')

        elif y1 == "2":
            nameKN = True
            if c2.lower() == "man":
                names = ["Bouldermore", "Kourayue", "Firestarter", "Musk", "Picking"]
            elif c2.lower() == "woman":
                names = ["Shara", "Locus", "Sophia", "Picking", "Acadia"]
            name__c = random.choice(names)
            print(f"\033[3m{name__c}\033[0m: The name is \033[3m{name__c}\033[0m.")
            if name__c.lower() == "sophia":
                print(f"\033[3m{Name}\033[0m: Hey I know someone as Sophia!")
                time.sleep(2)
                print(f'\033[3m{name__c}\033[0m: Cool?')

        elif y1 == "3":
            if nameKN == False:
                print(f"The {c2} looks you dead in the eyes.")
                time.sleep(2)
                print(f"{un}BEER")
                time.sleep(2)
                print(f"{un}...And some food.")
                time.sleep(2)
                print(f"{un}I heard he is even looking for a hire.")
            else:
                print(f"\033[3m{name__c}\033[0m looks you dead in the eyes.")
                time.sleep(2)
                print(f"\033[3m{name__c}\033[0m: BEER")
                time.sleep(2)
                print(f"\033[3m{name__c}\033[0m: ...And some food.")
                time.sleep(2)
                print(f"\033[3m{name__c}\033[0m: I heard he is even looking for a hire.")
    
        elif y1 == "4":
            print(f'\033[3m{Name}\033[0m: Thanks for the talk.\nYou say as you leave.')
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
    global coinbag, health, inventory, barhelp
    wait()
    if barhelp == False:
        T = input(f'''
TAVERN

Beer - 1 Coin #1
Stewed Mushrooms - 2 Coins #2
              
Help the bartender - type help

If you want to leave, type L
              
Your pouch: {coinbag}\n
''')
        if T.lower() == "beer" or T == '1':
            if 1 <= coinbag:
                coinbag = coinbag-1
                inventory.append('Beer')
                print("You've purchased beer!")
                bartenderdrinks()

            elif 1 > coinbag:
                print("\033[3mI don't have enough coins!\033[0m")
                bartenderdrinks()
        
        elif T.lower() == "stewed mushrooms" or T == '2':
            if 2 <= coinbag:
                health = 20
                coinbag = coinbag-2
                inventory.append('Stewed_Mushrooms')
                print('You purchased Stewed Mushrooms!')
                bartenderdrinks()
            elif 2 > coinbag:
                print("\033[3mI don't have enough coins!\033[0m")
                bartenderdrinks()

        elif T.lower() == "l" or T.lower() == "leave":
            print(f"{Name}: I'm ok.")
            time.sleep(2)
            DKtavern1()
        
    
        elif T.lower() == 'help':
            print(f'{bt}Thank goodness, I really needed some help.')
            time.sleep(2)
            barmini()

        else:
            print('Invalid, ending game. :)')
            sys.exit()
    
    else:
        barhelp = False
        T = input(f'''
TAVERN

Beer - 1 Coin #1
Stewed Mushrooms - 2 Coins #2

If you want to leave, type L
              
Your pouch: {coinbag}\n
''')
        if T.lower() == "beer" or T == '1':
            if 1 <= coinbag:
                coinbag = coinbag-1
                inventory.append('Beer')
                print("You've purchased beer!")
                bartenderdrinks()

            elif 1 > coinbag:
                print("\033[3mI don't have enough coins!\033[0m")
                bartenderdrinks()
        
        elif T.lower() == "stewed mushrooms" or T == '2':
            if 2 <= coinbag:
                health = 20
                coinbag = coinbag-2
                inventory.append('Stewed_Mushrooms')
                print('You purchased Stewed Mushrooms!')
                bartenderdrinks()
            elif 2 > coinbag:
                print("\033[3mI don't have enough coins!\033[0m")
                bartenderdrinks()

        elif T.lower() == "l" or T.lower() == "leave":
            print(f"{Name}: I'm ok.")
            DKtaverntable()

def barmini():
    global coinbag, barhelp
    barminig = ['412', '567', '125671834070461456108936458', '1', '51', '1255', '164', '231', '176', '424365', '752', '79', '44']
    print('Let us begin!')
    print('Just a reminder, you have to type back the number shown to win!')
    correct_answers = 0
    for i in range(4):
        for correct_answers in range(4):
            T = random.choice(barminig)
            C = input(T + "\n")
            if C == T:
                correct_answers += 1
            else:
                print('You failed!')
                bartenderdrinks()
    
        barhelp = True
        coinbag = coinbag+4
        print('###--- You have found \033[3m4 Coins\033[0m! ---###')
        time.sleep(2)
        print(f'{bt} Thanks for the help!')
        bartenderdrinks()

def blacksmith():
    if nextlevel:
        print(f'{c3}Your back! Good, Timo was about to leave eh.')
        wagon()
    elif nextlevel == False:
        print('\033[3m"let us see what the blacksmith holds."\033[0m')
        blacksmithint()

def blacksmithinfo():
    global nextlevel
    wait()
    print(f'{c3}The names Thor, so, your interested ye?')
    time.sleep(1)
    T = input('\033[3m"What did I get myself into? I should probably say something..."\033[0m (Y/N)\n')
    if T.lower() == 'y':
        nextlevel = True
        print(f'{Name}: Definitely.')
        time.sleep(2)
        print(f'{c3}Wonderful! Ok, so the job is simple.')
        time.sleep(1)
        print('\033[3m"The job..?"\033[0m')
        time.sleep(1)
        print(f'{c3}All your going to do is go with my mate, Timo. Real softy, anyhow. You go with him and simply guard the wagon.')
        time.sleep(2)
        print('You nod.')
        time.sleep(1)
        print(f'{c3}Great! Were done. See me when your ready.')
        time.sleep(1)
        print('\033[3mThor takes you outside\033[0m')
        outside()
    elif T.lower() == 'n':
        print(f"{bs}That's a shame, now, I'll let you go. Just, don't tell anyone.")
        time.sleep(2)
        print('\033[3mFear strikes your heart.\033[0m')
        time.sleep(1)
        print('\033[3m"What did I just do..?"\033[0m')
        outside()

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
    T = input('Shop or information?\n')
    if T.lower() == 'shop':
        print(f"{bs}Great to hear!")
        blacksmithitems()
    elif T.lower() == 'info' or T.lower() == 'information':
        print(f'{bs}Well, well! Ok, well, follow me.')
        time.sleep(2)
        print('He guides you to a back room filled with armor, weapons, and tools.')
        blacksmithinfo()
    else:
        print('Invalid, ending game. :)')
        sys.exit()

def blacksmithitems():
    global health, inventory, weapons, coinbag
    wait()
    T = input(f'''
BLACKSMITH

Dagger - 4 Damage - 5 Coin #1
Shield - +5 Health - 5 Coin #2
Armor - +10 Health - 10 Coins #3

If you want to leave, type L
              
Your inventory: {inventory}
Your pouch: {coinbag}
Your weapons: {weapons}
Your health: {health}\n
''')
    if T.lower() == "dagger" or T == '1':
        if 5 <= coinbag:
            weapons.append('Dagger - 4 Damage')
            coinbag = coinbag-5
            print("You've purchased Dagger!")
            print('###--- You have found \033[3mDagger\033[0m! ---###')
            blacksmithitems()
        elif 5 > coinbag:
            print("\033[3mI don't have enough coins!\033[0m")
            blacksmithitems()
        
    elif T.lower() == "shield" or T == "2":
        if 5 <= coinbag:
            inventory.append('Shield')
            coinbag = coinbag-5
            health = health+5
            print('You purchased Shield!')
            print('###--- You have found \033[3mShield\033[0m! ---###')
            blacksmithitems()
        elif 5 > coinbag:
            print("\033[3mI don't have enough coins!\033[0m")
            blacksmithitems()

    elif T.lower() == "armor" or T == '3':
        if 10 <= coinbag:
            inventory.append('Armor')
            coinbag = coinbag-10
            health = health+10
            print('You purchased Armor!')
            print('###--- You have found \033[3mArmor\033[0m! ---###')
            blacksmithitems()
        elif 10 > coinbag:
            print("\033[3mI don't have enough coins!\033[0m")
            blacksmithitems()

    elif T.lower() == "l" or T.lower() == "leave":
        print(f"{Name}: I'm ok.")
        time.sleep(2)
        print("\033[3mYou walk out of the blacksmith...\033[0m")
        outside()

    else:
        print('Invalid, ending game. :)')
        sys.exit()

def towns():
    global questfailed, tsquestS, coinbag, questf
    print('\033[3mYou enter the town square.\033[0m')
    time.sleep(2)
    if questfailed:
        print('The place is filled with markets stands and people.')
        townsn()
    elif questfailed == False and tsquestS == False and questf == False:
        tsquestS = True
        print('The place is filled with market stands and people. One of the owners of a stands calls out to you...')
        time.sleep(2)
        print('\033[3m"He seems familiar..."\033[0m')
        wait()
        questmark()
    elif tsquestS and questf == False:
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
    elif tsquestS and inventory.count('Armor') == 3:
        tsquestS = False
        questf = True
        inventory.remove('Armor')
        inventory.remove('Armor')
        inventory.remove('Armor')
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
    T = input('"Who are you? "' + 'or' + '" Good" (1 or 2?)\n')
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

Iron-Claw Cloth #1
- +2 Damage
- +2 Health

Iron-Plate Cloth #2 
- +4 Health

Vanity-Thimble Cloth #3
- Nothing (But you get to look cool, and who knows, it might get you some special reactions ¯\_( ͡° ͜ʖ ͡°)_/¯)

Your inventory: {inventory}\n
''')
        if T.lower() == 'iron-claw cloth' or T == '1':
            health = health+2
            damagemod = damagemod+2
            inventory.append('Iron-Claw Cloth')
            print('###--- You have found \033[3mIron-Claw Cloth\033[0m!')
        elif T.lower() == "iron-plate cloth" or T == '2':
            health = health+4
            inventory.append('Iron-Plate Cloth')
            print('###--- You have found \033[3mIron-Plate Cloth\033[0m!')
        elif T.lower() == 'vanity-thimble cloth' or T == '3':
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

def wagon():
    wait()
    print('\033[3mYou hop on to the wagon. Timo is sitting holding the reins. He is a large male, one of his eyes is covered by a eye patch.\033[0m')
    time.sleep(2)
    print(f'{c3}Here,')
    print('Thor is holding a bow in this grasp.')
    print(f'{c3}you can take this bow.')
    time.sleep(2)
    T = input('Do you take the bow? Bow - 5 Damage (Y/N)\n')
    if T.lower() == "y":
        weapons.append('Bow - 5 Damage')
        print('You grab the bow.')
        print('###--- You have found \033[3mBow\033[0m! ---###')
    elif T.lower() == 'n':
        print(f'{c3}Suit yourself.')
    time.sleep(2)
    print("\033[3mAfter taking off you and Timo find yourselves in the woods, Timo doesn't talk much, so you mostly kept to yourself.")
    wait()
    print('While in the woods, suddenly, you hit a large bump. Nearly knocking you and your belongings off the wagon.')
    time.sleep(2)
    print('\033[3mTimo\033[0m: You, go check.')
    print('Timo says in a course voice.')
    time.sleep(2)
    print('You, both freightened by Timo and the bump, hop off nerviously.')
    time.sleep(2)
    print('You look to see what you hit, and it seems to be a large green bump.')
    T = input('Check it out? (Y/N)\n')
    if T.lower() == 'y':
        print('You crouch down to see the problem, but suddenly the world goes dark as you get bagged.')
        time.sleep(2)
        print('You can hear Timo screaming at the creature that took you. But he never comes.')
        time.sleep(2)
        print('You thrown on to another wagon, you assume, and are taken to some unknown place.')
        anewworld()
    elif T.lower() == 'n':
        T = random.randint(1, 6)
        print('\033[3m"Heck no."\033[0m')
        time.sleep(1)
        print(f'{Name}: Hey! We hit something strange!')
        time.sleep(1)
        print('You hop on the wagon, Timo is glaring behind you.')
        time.sleep(2)
        print('You mouth the words, "What?"')
        time.sleep(2)
        print('Timo continues to stare.')
        time.sleep(2)
        if T <= 3:
            print("You look behind you, you don't see a thing.")
            time.sleep(2)
            print('But suddenly, a small goblin jumps out screaming.')
            time.sleep(1)
            battle()
        elif T > 3:
            print('You look behind you, into the bushes. You see a small goblin hiding in there.')
            T = input('Use your bow? (Y/N)\n')
            if T.lower() == "y":
                T = random.randint(1, 6)
                print('You lift your bow to the goblin')
                print('You pull the string back.')
                time.sleep(2)
                print('\033[3mFling!\033[0m')
                if T > 3:
                    print('The arrow hits the goblin in the skull.')
                    time.sleep(1)
                    print('Instantly killing it. Soon, other goblins begin popping up...')
                    battle()
                elif T <= 3:
                    print('You miss the goblin completely...')
                    print('Temo: Pathetic.')
                    time.sleep(2)
                    T = input('"Shut up" or say nothing. (1 or 2?)\n')
                    if T.lower() == "1":
                        print(f'{Name}: Shut up.')
                        time.sleep(1)
                        print('Surprisingly, Timo does shut up.')
                    elif T.lower() == "2":
                        print('You scoff.')
                    else:
                        print('You had one job')
                        sys.exit()
                    print('The goblin houls, summoning other goblins to aid it.')
                    battle()
                else:
                    print('you had one job')
                    sys.exit()

def battle():
    global health, goblin1, goblin2, goblin3, goblin4, c2, damagemod, coinbag, inventory, weapons
    wait()
    while goblin1 > 0 or goblin2 > 0 or goblin3 > 0 or goblin4 > 0:

        if health <= 0:
            time.sleep(2)
            print("You're shoved off the wagon by Timo. He disappears.")
            time.sleep(2)
            print('Suddenly the world goes dark as you get bagged.')
            time.sleep(2)
            print('You thrown on to another wagon, you assume, and are taken to some unknown place.')
            anewworld()
            health = 20
            goblin1 = 5
            goblin2 = 5
            goblin3 = 5
            goblin4 = 5
            weapons.append('Dagger - 4 Damage')
            coinbag = coinbag+5
            print('You won the fight!')
            print("###--- You have found \033[3m5 Coins\033[0m! ---###")
            print('###--- You have found \033[3mDagger\033[0m! ---###')
            outside()

        if goblin1 > 0 and goblin2 > 0 and goblin3 > 0 and goblin4 > 0:
            T = input(f'{gob}1, {gob}2, {gob}3, and {gob}4 (1, 2, 3, or 4?)\n')
        elif goblin1 <= 0 and goblin2 > 0 and goblin3 > 0 and goblin4 > 0:
            T = input(f'{gob}2, {gob}3, and {gob}4 (2, 3, or 4?)\n')
        elif goblin1 <= 0 and goblin2 <= 0 and goblin3 > 0 and goblin4 > 0:
            T = input(f'{gob}3, and {gob}4 (3 or 4?)\n')
        elif goblin1 <= 0 and goblin2 <= 0 and goblin3 <= 0 and goblin4 > 0:
            T = input(f'{gob}4 (4?)\n')
        elif goblin1 <= 0 and goblin2 <= 0 and goblin3 > 0 and goblin4 <= 0:
            T = input(f'{gob}1, {gob}2, {gob}3, and {gob}4 (1, 2, 3, or 4?)\n')
        elif goblin1 > 0 and goblin2 <= 0 and goblin3 > 0 and goblin4 > 0:
            T = input(f'{gob}1, {gob}3, and {gob}4 (1, 3, or 4?)\n')
        elif goblin1 <= 0 and goblin2 > 0 and goblin3 <= 0 and goblin4 > 0:
            T = input(f'{gob}1, {gob}2, and {gob}4 (1, 2, or 4?)\n')
        elif goblin1 <= 0 and goblin2 > 0 and goblin3 > 0 and goblin4 <= 0:
            T = input(f'{gob}1, {gob}2, and {gob}3 (1, 2, or 3?)\n')

    
        if T == "1":
            print(f'You pick {gob}1!')
            time.sleep(2)
            weapon = input(f'Which weapon do you pick?\n{weapons}')
            time.sleep(2)
            if weapon.lower() in weapons:
                print(f'You picked {weapon}!')
                time.sleep(2)
                T = random.randint(0, 20)
                if T >= 15:
                    goblin1 -= weapons[weapon]['Damage']+damagemod
                    print(f'You hit and dealt {weapons[weapon]["Damage"]+damagemod} damage!')

                elif T < 15:
                    health -= 3
                    print(f'You missed and gave the {gob}1 an opportunity to hit!')
                    time.sleep(1)
                    print('You take 3 damage!')
            else:
                print('ERROR')

        elif T == "2":
            print(f'You pick {gob}2!')
            time.sleep(2)
            weapon = input(f'Which weapon do you pick?\n{weapons}')
            time.sleep(2)
            if weapon.lower() in weapons:
                print(f'You picked {weapon}!')
                time.sleep(2)
                T = random.randint(0, 20)
                if T >= 15:
                    goblin1 -= weapons[weapon]['Damage']+damagemod
                    print(f'You hit and dealt {weapons[weapon]["Damage"]+damagemod} damage!')

                elif T < 15:
                    health -= 3
                    print(f'You missed and gave the {gob}2 an opportunity to hit!')
                    time.sleep(1)
                    print('You take 3 damage!')
            else:
                print('ERROR')

        elif T == "3":
            print(f'You pick {gob}3!')
            time.sleep(2)
            weapon = input(f'Which weapon do you pick?\n{weapons}')
            time.sleep(2)
            if weapon.lower() in weapons:
                print(f'You picked {weapon}!')
                time.sleep(2)
                T = random.randint(0, 20)
                if T >= 15:
                    goblin3 -= weapons[weapon]['Damage']+damagemod
                    print(f'You hit and dealt {weapons[weapon]["Damage"]+damagemod} damage!')

                elif T < 15:
                    health -= 3
                    print(f'You missed and gave the {gob}3 an opportunity to hit!')
                    time.sleep(1)
                    print('You take 3 damage!')
            else:
                print('ERROR')

        elif T == "4":
            print(f'You pick {gob}4!')
            time.sleep(2)
            weapon = input(f'Which weapon do you pick?\n{weapons}')
            time.sleep(2)
            if weapon.lower() in weapons:
                print(f'You picked {weapon}!')
                time.sleep(2)
                T = random.randint(0, 20)
                if T >= 15:
                    goblin4 -= weapons[weapon]['Damage']+damagemod
                    print(f'You hit and dealt {weapons[weapon]["Damage"]+damagemod} damage!')

                elif T < 15:
                    health -= 3
                    print(f'You missed and gave the {gob}4 an opportunity to hit!')
                    time.sleep(1)
                    print('You take 3 damage!')
            else:
                print('ERROR')

        else:
            print('Invalid, ending game. :)')
            sys.exit()

def anewworld():
    global inventory, coinbag
    inventory = []
    coinbag = None
    wait()
    print('You awake in a damp, dark room. A torch shining in your face.')
    time.sleep(2)
    print(f'{gob}1: Look! Look! He is wake!')
    time.sleep(1)
    print('As your eyes adjust to the light, you see two other goblins.')
    time.sleep(2)
    print(f'{gob}2: You been kidnapped!')
    time.sleep(1)
    print('The goblins snicker,')
    time.sleep(1)
    print(f'{gob}1: Come, Leader wish us not here.')
    time.sleep(1)
    print('You watch as the goblins mumble to themselves while walking out.')
    time.sleep(2)
    print("Soon it's just you alone, tied up in the corner of the cell.")
    time.sleep(1)
    esc()

def esc():
    global health
    T = input('Do you attempt to rub the rope on the rough walls, try to bite through them, or accept your fate? (1, 2, or 3?)\n')
    if T == '1':
        health = health-2
        print('You decided to use the wall to aid your escape.')
        wait()
        print('After some time, you finally manange to tear through the rope. After facing some burns yourself.')
        time.sleep(2)
    elif T == '2':
        print('\033[3m"Maybe I can tear it with my teeth."\033[0m')
        time.sleep(1)
        print('You start using your mouth to bite down on the rope.')
        wait()
        print("After some time it finally ends up tearing.")
        time.sleep(1)
    elif T == '3':
        print('You lay back into the stone. You accept your fate.')
        sys.exit()
    esc1()

def esc1():
    print('') 

character_customization()

wait()
print("You awake in a bed, the soft covers keeping you warm. You're in a room, fitted with a dresser and cobblestone walls.")
time.sleep(3)
print("Before you are able to do anything, you hear someone.")
time.sleep(2)
print(un + "Oh! Finally, you're awake!")
time.sleep(1)
T = input('"Where am I?" or "Who are you?" (1 or 2)\n')

if T.lower() == "1":
    Villagename = True
    print(Name + ": Where am I?")
    time.sleep(2)
    print(un + "You don't remember do you? Well, welcome to \033[3mTishun Village\033[0m!")
    time.sleep(3)
    print('\033[3m"The name oddly rings a bell..."\033[0m')
    time.sleep(2)
    print(f'{c1}: My name is Sophia by the way.')
elif T.lower() == "2":
    print(Name + ": Who are you?")
    time.sleep(2)
    print(c1 + "Oh! I'm \033[3mSophia\033[0m.")
else:
    print('YOU HAD ONE JOB.')
    sys.exit()

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