print("******************************")
print("           Welcome")
print("     Rock, Paper, Scissor")
print("******************************")
import random
comp = ['Scissor','Paper','Rock']
x = int(input("Enter Number of times you want to play: "))
for i in range (x, 0, -1):
    com = random.choice(comp)
    usr = str(input("\nEnter your word: "))
    if usr == comp[0]:
        if com == comp[1]:
            print("You Won !!\nMy choice:", com)
        elif com == com[2]:
            print("Ha Ha, I won\nMy choice:", com)
        else:
            print("Tie, I won't let you win\nMy choice:", com)
    elif usr == comp[1]:
        if com == comp[0]:
            print("You loose\nMy choice:", com)
        elif com == comp[2]:
            print("Bravo!!, You won\nMy choice:", com)
        else:
            print("Tie, I will not let let you win\nMy choice:", com)
    elif usr == comp[2]:
        if com == comp[0]:
            print("I Loose :(\nMy choice:", com)
        elif com == comp[1]:
            print("I win :)\nMy choice:", com)
        else:
            print("Tie, I won't let you win\nMy choice:", com)
    else:
        print("Wrong input, make your 1st letter capital\nFor Example:", com)
