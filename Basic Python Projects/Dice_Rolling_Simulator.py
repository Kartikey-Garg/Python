print("**********************************")
print("             WELCOME")
print("    THE DICE ROLLING SIMULATOR")
print("**********************************")
import random
import sys
def usr():
   return random.randint(1,6)
print("Die Number:", usr())
while True:
    usr()
    n = input("Do you want to quit ? (Y/N)\n")
    if n in ['Y', 'y']:
        print("Bye!!")
        sys.exit()
    elif n in ['N', 'n']:
        print("Die Number:", usr())
    else:
        print("Invalid Input")
        sys.exit()
