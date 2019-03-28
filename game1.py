
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
                    print("You exit into a long hallway.")
                else:
                    print("With nothing else to do, you leave the room.")
                    print("You exit into a long hallway.")
        elif ans2 == "Leave":
            print("You exit into a long hallway.")
    elif ans1 == "Leave":
        print("You exit into a long hallway.")
    else:
        print("Unexpected response.")
ans1()

def ans4():
    ans4 = input("Would you like to go left or right? (type left or right):  ").capitalize
    if ans4 == "Left":
        input("You exit the building into a small courtyard. You continue walking and are off the property. You find yourself on the edge of a forest. Would you like to enter the forest? (Type yes or no):  ")
        

ans4()