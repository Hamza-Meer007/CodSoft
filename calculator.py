

import math
from os import system,name
from time import sleep
import subprocess

def menu():
    print("\t\t\t\t-------------------------------------------------")
    print("\t\t\t\t|\tPress 1: For Addition\t\t\t|")
    print("\t\t\t\t|\tPress 2: For Subracion\t\t\t|")
    print("\t\t\t\t|\tPress 3: For Multiplication\t\t|")
    print("\t\t\t\t|\tPress 4: For Division\t\t\t|")
    print("\t\t\t\t|\tPress 5: For Modulus\t\t\t|")
    print("\t\t\t\t|\tPress 6: For Square root\t\t|")
    print("\t\t\t\t|\tPress 7: For Cube root\t\t\t|")
    print("\t\t\t\t|\tPress 8: For Factorial\t\t\t|")
    print("\t\t\t\t|\tPress 9: For Combination\t\t|")
    print("\t\t\t\t|\tPress 10: For Greatest common multiple\t|")
    print("\t\t\t\t|\tPress 11: For Least common multiple\t|")
    print("\t\t\t\t|\tPress 12: For Permutation\t\t|")
    print("\t\t\t\t|\tPress 13: For Square\t\t\t|")
    print("\t\t\t\t|\tPress 14: For Cube\t\t\t|")
    print("\t\t\t\t|\tPress 15: For Copy Sign\t\t\t|")
    print("\t\t\t\t|\tPress 0: To Exit: \t\t\t|")
    print("\t\t\t\t-------------------------------------------------")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')


print("\t\t\t\t\t\t==>--------------------------------------<==\t\t\t\t\t")
print("\t\t\t\t\t\t==>            CALCULATOR                <==\t\t\t\t\t")
print("\t\t\t\t\t\t==>--------------------------------------<==\t\t\t\t\t")
try:
    i =1
    while i>0:

        menu()

        choice =int(input("Enter Your Choice :"))

        i=i+1
        clear()
        if choice==1:

            x = input("Enter 1st Number: ")
            y = input("Enter 2nd Number: ")

            add = int(x) + int(y)
            print(f'The Addition is: {add}')


        elif choice==2:

            x = input("Enter 1st Number: ")
            y = input("Enter 2nd Number: ")

            sub = int(x) - int(y)
            print(f'The Subtraction is: {sub}')

        elif choice==3:

            x = input("Enter 1st Number: ")
            y = input("Enter 2nd Number: ")

            mul = int(x) * int(y)
            print(f'The Multiplition is: {mul}')

        elif choice==4:

            x = input("Enter 1st Number: ")
            y = input("Enter 2nd Number: ")

            div = int(x) / int(y)
            print(f'The Division is: {div}')

        elif choice==5:

            x = input("Enter 1st Number: ")
            y = input("Enter 2nd Number: ")

            mod = int(x) % int(y)
            print(f'The Modulus is: {mod}')

        elif choice==6:
            x = int(input("Enter Number: "))
            print(f'The Square root is: {math.isqrt(x)}')

        elif choice==7:
            x = int(input("Enter Number: "))


            print(f'The Cube root is: {math.cbrt(x)}')

        elif choice==8:
            y = int (input("Enter Number: "))

            print(f'The Factorial is: {math.factorial(y)}')

        elif choice==9:
            x = int(input("Enter 1st Number: "))
            y = int(input("Enter 2nd Number: "))


            print(f'The Combination is: {math.comb(x,y)}')
        elif choice==10:
            x = int(input("Enter 1st Number: "))
            y = int(input("Enter 2nd Number: "))
            print(f'The Greatest Common Factor is: {math.gcd(x,y)}')

        elif choice==11:
            x = int(input("Enter 1st Number: "))
            y = int(input("Enter 2nd Number: "))
            print(f'The Least Common Multiple is: {math.lcm(x,y)}')

        elif choice==12:
            x = int(input("Enter 1st Number: "))
            y = int(input("Enter 2nd Number: "))
            print(f'The Permutation is: {math.perm(x,y)}')

        elif choice==13:
            x = int(input("Enter Number: "))

            print(f'The Square is: {x*x}')

        elif choice==14:
            x = int(input("Enter 1st Number: "))

            print(f'The Cube is: {x*x*x}')

        elif choice==15:
            x = int(input("Enter 1st Number: "))
            y = int(input("Enter 2nd Number: "))

            print(f'The Copy sign is: {math.copysign(y,x)}')
        elif choice==0:
            print("Exiting.......")
            break

        else:
            print("Invalid Integer")
except ValueError:
    print("Invalid :")
except ZeroDivisionError:
    print("Denominator is not  0")