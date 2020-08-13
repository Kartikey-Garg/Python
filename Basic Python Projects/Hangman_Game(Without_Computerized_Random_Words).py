import random
print("*******************************")
print("           WELCOME")
print("       THE HANGMAN GAME")
print("*******************************")
WORDS = ['HANGMAN','GAME','WELCOME','CHANCES','CORRECT','WRONG']
word = random.choice(WORDS)
real = ''.join(["["+x+"] " for x in word])
display = ['_'] * len(word)

for i in range (1,10):
 print(''.join(["["+x+"] " for x in display]))
 A = ''.join(["["+x+"] " for x in display])
 
 if A == real:
     print("Congo !!, You are done")
     break
 letter = input("\nGuess a letter: ")
 
 if letter in word:
  print("CORRECT!!")
  
  for i,x in enumerate(word):
    if x is letter:
        display[i] = letter
                
 else:
     print("Wrong!!")
     print("Chances left: ",i)
