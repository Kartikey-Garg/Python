print("**********************************")
print("             WELCOME")
print("    THE DICE ROLLING SIMULATOR")
print("**********************************")
import random
def usr():
   return random.randint(1,6)
print("Die Number:", usr())
x=True
while x:
    usr()
    n = input("Do you want to quit ? (Y/N)\n")
    if n in ['Y', 'y']:
        print("Bye!!")
        x=False
    elif n in ['N', 'n']:
        print("Die Number:", usr())
    else:
        print("Invalid Input")
        x=False
