
print("You wake up in a dark room. After a few moments your eyes adjust and you're able to make out the outline of a door.")
def ans1():
    ans1 = input("Would you like to look around the room or leave (type explore or leave):  ").capitalize()
    if ans1 == "Explore":
        print("It seems to be bare.  The is a single chest.")
        ans2 = input("Would you like to open the chest or leave the room (type open or leave):  ").capitalize()
        if ans2 == "Open":
                ans3 = input("There are 15 gold coins in the chest. Would you like to take them? (type yes or no):  ").capitalize()
                if ans3 == "Yes":
                    print("You put the coins in your pocket and leave the room.")
                else:
                    print("With nothing else to do, you leave the room.")
                    
   
    elif ans1 or ans2 == "leave":
        print
ans1()

