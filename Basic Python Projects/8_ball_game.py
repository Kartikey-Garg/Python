import random
print("*******************************")
print("           Welcome")
print("    THE MAGIC 8 BALL GAME")
print("*******************************")
ans = ['My sources say YES','100% YES','An Immortal said NO','My sources say NO','It is up to you','You mortal Yes you can','Even immortals do not know','My crew left me cause you asked this question']
input("Type your question: ")
input("Choose a ball between 1 to 8: ")
print("Answer:", random.choice(ans))
