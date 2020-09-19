print("**********************************")
print("       Truth Or Dare Game")
print("**********************************")
def Truth():
    #ques = str(input(random.choice(lines)))
    print(random.choice(lines))
    TODG()
    
def Dare():
    #ques = str(input(random.choice(line)))
    print(random.choice(line))
    TODG()
    
def TODG():
    game = input("Completed / Skipping (C/S) ? ")
    if game in 'C':
        choice = input("Great! Lets Continue playing, Type 'OK' to continue :")
        if choice in 'OK':
            base()
        else:
            print("Bye!")
            sys.exit()
    elif game in 'S':
        print("Okay I am leaving on to your friends to ask you something")
        print("Will display next question in 10 secs.")
        time.sleep(10)
        TODG()
    else:
        print("Input Not Recognized")    

def base():
    plyr = random.choice(plyrs_arr)
    ch = input(plyr+ " Truth or Dare (T/D): ")
    if ch is 'T':
       Truth()
    elif ch in 'D':
       Dare()
    else:
        print("Input not recognized, try retrying")
        base()
                
import random
import time
import sys
f =  open('Python_Truth.txt', encoding='utf8')
f1 =  open('Python_Dare.txt', encoding='utf8')
lines = [line for line in f.readlines()]
line = [line for line in f1.readlines()]
f.close()
f1.close()
plyrs = input("Enter the name of players: ")
plyrs_arr = plyrs.split()
print("Lets start the game")
base()
