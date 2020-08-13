print("**********************************")
print("WELCOME")
print("THE DICE ROLLING SIMULATOR")
print("**********************************")
import random
import sys
Yes = ['Y', 'y']
No = ['N', 'n']
def usr():
    x = random.randint(1,6)
    return x
while True:
    usr()
    n = input("Do you want to quit ? (Y/N)\n")
    if n in Yes:
        print("Bye!!")
        sys.exit()
    elif n in No:
        print("Die Number:", usr())
    else:
        print("Invalid Input")
        sys.exit()
