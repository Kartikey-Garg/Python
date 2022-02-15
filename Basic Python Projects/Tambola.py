import random
name=input("Enter name: ")
print("Welcome to Tambola, "+name)
players=int(input("Enter the number of players (2 to 10): "))
if players >=2 and players <=10:
    for j in range(players):
        print("List for Player "+str(j+1)+": ", end='')
        for i in range(9):
            print(str(random.randrange(1,100))+ " ", end='')
        print()
    i=1
    print("\nYour Check List:\n")
    for i in range(players):
        for j in range (10):
            a=random.randint(1,100)
            print(str(a)+" ", end='')
        print()
    print()
    win=input("Enter Winner: ")
    print("Congratulations,",win)
else:
    print("Invalid Input")
