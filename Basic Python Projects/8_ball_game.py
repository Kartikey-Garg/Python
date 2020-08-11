import random
print("*******************************")
print("           Welcome")
print("    THE MAGIC 8 BALL GAME")
print("*******************************")
ans = ['My sources say YES','My reply is yes','Why to Delay in Good Work','Yes','Yep','NO you are not','It is certain','Absolutely not','An Immortal say NO','No','My sources say NO','It is up to you','No one knows except ONE','You mortal Yes you can','Even immortals do not know','No you are wrong','My crew left me cause you asked this question','All the best','Never','You are alone']
Ques = input("Type your question: ")
Ball = int(input("Choose a ball between 1 to 8: "))
print("Answer:", random.choice(ans))
