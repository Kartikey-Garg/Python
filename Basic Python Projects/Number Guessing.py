def hint(num):
    return num
import random
print("*********************************")
print("             WELCOME")
print("    The Number Guessing Game")
print("*********************************")
print("Total chances 3")
try:
    while (True):
        dif = int(input("Chose Difficulty Level 1/2/3: "))
        if dif==1:
            num = random.randint(0,10)
            maxi=10
            break
        elif dif==2:
            num = random.randint(0,50)
            maxi=50
            break
        elif dif==3:
            num = random.randint(0,100)
            maxi=100
            break
        else:
            print("Wrong Input, Please try again")   
    #print(num)
    for i in range (2,-1,-1):
        x = input("\nGuess the number between 0 to "+str(maxi)+": ")
        print(x)
        if x == 'H':
            print(hint(num))
        elif int(x) > num:
            print("Fortunately, you guessed it bigger")
            print("Number of chances left: ",i," press H for HINT")
        elif int(x) == num:
            print("Yep, you guess it correct. Congo!!")
            print("Number of chances left: ",i,)
            break
        else:
            print("Nope, you guessed it smaller")
            print("Number of chances left: ",i," press H for HINT")
    if x!=num:
        print("The Secret Number is: ",num)
    if i==2:
        print("Score: 10")
    elif i==1:
        print("Score: 5")
    else:
        print("Score: 0")
except Exception as E:
    print(E)
finally:
    print("Program Exited")