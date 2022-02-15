import random
name=input("Enter name: ")
print("Welcome to Tambola, "+name)
players=int(input("Enter the number of players (2 to 10): "))
if players >=2 and players <=10:
    for j in range(players):
        print("List for Player "+str(j+1)+": ", random.sample(range(1,100), 9))
    print("\nYour Check List:\n", random.sample(range(1,100), (players*10)))
    win=input("Enter Winner: ")
    print("Congratulations,",win)
else:
    print("Invalid Input")
