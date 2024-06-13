
import string
import random


def password_gen(password):
    check = ''
    user = int(input("Enter the length of password: "))
    i =0
    if user > 0 and user < 50:
        while i<= user:
            
            check +=random.choice(password)
            
            i +=1
        print(f"Your password of desired length and complexity: {check}")
    else:
        print("Enter length between 1 and 49")








print("\t------------------------------------------")
print("\t==>     Welcome to Password Generator\t<==")
print("\t------------------------------------------")
print("Enter password complexity")
user1 = int(input("1. Easy \n2. Normal \n3. Hard\nEnter your choice:"))
if user1 == 3:
    password = string.ascii_letters+string.digits+string.punctuation
    password_gen(password)
    
elif user1 == 1:
    password = string.ascii_letters
    password_gen(password)
    
elif user1==2:
    password=string.ascii_letters+string.digits
    password_gen(password)
    
else:
    print("Invalid......")
    

