import time

coins = 0


print("You wake up in a dark room. After a few moments your eyes adjust and you're able to make out the outline of a door.")
def ans1():
    ans1 = input("Would you like to look around the room or leave (type explore or leave):  ").capitalize()
    if ans1 == "Explore":
        print("It seems to be bare. There is a single chest.")
        ans2 = input("Would you like to open the chest or leave the room (type open or leave):  ").capitalize()
        if ans2 == "Open":
                ans3 = input("There are 15 gold coins in the chest. Would you like to take them? (type yes or no):  ").capitalize()
                if ans3 == "Yes":
                    print("You put the coins in your pocket and leave the room.")
                    coins = 0+15
                    print("You now have", coins, "coins.")
                    print("You enter a sterile looking hallway.")
                else:
                    print("With nothing else to do, you leave the room.")
                    print("You exit into a long hallway.")
        elif ans2 == "Leave":
            print("You exit into a cold, bleak hallway.")
    elif ans1 == "Leave":
        print("You exit into a dark hallway.")
ans1()

def ans4():
    ans4 = input("Would you like to go left or right? (type left or right):  ").capitalize()
    if ans4 == "Left":
        print("You exit the building into a small courtyard.")
        ans5 = input("You continue walking and are off the property. You find yourself on the edge of a lava field. Would you like to enter the field? (Type yes or no):  ").capitalize()
        if ans5 == "Yes":
            print("You feel your foot burning. You instantly regret your choice and can feel your health deteriorating.")
            print("However, in the distance you can see an apparation in the distance.")
            ans6 = input("It might be your imagaination.  Would you like to investigate?  (Type yes or no):  ").capitalize()
            if ans6 == "Yes":
                print("You are beginning to  get woozy. Everything goes dark.")
                time.sleep(2)
                print("You are awoken with a shake.")
                print("The apperation is standing above you.")
                print("In a booming voice they say: I can help you, but only in you pay. Do you have any coins")
                ans7 = input("Did you take the coins from the chest earlier? (type yes or no):  ").capitalize()
                if ans7 == "Yes":
                    coins = 15 - 10
                    print("You now have", coins, "coins")
                    print("You are returned to the edge of the field.  You now must walk around it.")
                if ans7 == "No":
                    print("The spirit disappeared, and you are left for dead in the field.")
                    time.sleep(2)
                    print("GAME OVER")
            if ans6 == "No":
               print("You turn around and exit the field. Your feet have never hurt this much. You take a brief rest but then you feel you need to press on. You set off around the field.")
        if ans5 == "No":
            print("You set off around the field.")
    if ans4 == "Right":
        print("You walk down hallway for what feels like days. At the end you reach a door at the end of the hall.")
        print("You enter and hear the door lock behind you. You feel fear over take you.")
        print("There is nothing in the room except a single lightbulb hanging from the cieling.")
        print("You look around in hopes of finding a window or something.")
        print("You reach your hand into your pocket and realize in horror that there is a hole in it.")
        ans8 = input("What would you like to do? type(shout or sleep):  ").capitalize()
        if ans8 == "Sleep":
            print("You lay down and don't wake up.")
            print("GAME OVER")
        if ans8 == "Shout":
            print("You yell for ages.")
            print("Eventually you hear somebody outside the room.")
        
        
ans4()