
from os import system,name

import random
import time

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')


count = 1
flag = 1
while count <= 3 and flag <= 3:
    print("\t------------------------------------------")
    print("\t==>       Stone Paper Scissors  \t<==")

    print("\t------------------------------------------\n\n")
    
    print("Enter 1 for Stone \nEnter 2 for Paper\nEnter 3 for Scissors ")
    user = int(input("Enter Your Choice: "))
    if user <= 3:
        if user == 1:
            print("You entered stone")
        elif user == 2:
            print("You entered Paper")
        else:
            print("You entered scissors:")

        comp = random.randint(1, 3)
        if comp == 1:
            print("Computer entered stone")
        elif comp == 2:
            print("Computer entered Paper")
        else:
            print("Computer entered scissors:")
        time.sleep(2)
        if user == comp:
            print("Draw ")
        elif user == 1 and comp == 2:
            print("You lose:")
            flag += 1
        elif user == 1 and comp == 3:
            print("You Won:")
            count += 1
        elif user == 2 and comp == 1:
            print("You Won:")
            count += 1
        elif user == 2 and comp == 3:
            print("You lose:")
            flag += 1
        elif user == 3 and comp == 1:
            print("You lose:")
            flag += 1
        elif user == 3 and comp == 2:
            print("You Won:")
            count += 1
        
        clear()  # Clear the screen after each iteration
    else:
        print("Try again")

if count == 4:
    print("\t\t\t\tCongratulations!!!........You Won: \t\t\t\t")
else:
    print("\t\t\t\tYou Lose:...........Thanks for Playing!!!\t\t\t\t")
