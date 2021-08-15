import random
print("*********************************")
print("             WELCOME")
print("    The Number Guessing Game")
print("*********************************")
print("Total chances 3")
num = random.randint(0,100)
print(num)
for i in range (2,-1,-1):
 x = int(input("\nGuess the number between 0 to 100: "))
 if x > num:
     print("Fortunately, you guessed it bigger")
     print("Number of chances left: ",i)
 elif x == num:
     print("Yep, you guess it correct. Congo!!")
     print("Number of chances left: ",i)
     break
 else:
     print("Nope, you guessed it smaller")
     print("Number of chances left: ",i)
if x!=num:
   print("The Secret Number is: ",num)
