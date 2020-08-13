#Note, you may find it not working because "random_words" is not recognized in new python.
#Run it with Command Prompt by going to file location and simply typing "Hangman_Game_With_Global_Random_Words.py"
import random
from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()

print(word) #To see the word what is guessed by computer

print("*******************************")
print("           WELCOME")
print("       THE HANGMAN GAME")
print("*******************************")
print("Remember, CapsLock must be OFF")

real = ''.join(["["+x+"] " for x in word])
display = ['_'] * len(word)

for i in range (1,30):
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
