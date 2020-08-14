print("*******************************")
print("           WELCOME")
print("    THE PASSWORD GENERATOR")
print("*******************************")
import random
chars='abcdefghijklmnopqrstuvwxyz'
charz='!@#$%^&*'
chari='1234567890'
yes=['Y','y']
no=['N','n']
def passw():
 spec = input('Special characters required(Y/N): ')
 if spec in yes or spec in no:
  integ = input('Numbers required(Y/N): ')
  if integ in yes or integ in no:
   length = int(input('Password Length(: ')) 
   for p in range(int(input('Enter Password Range: '))):
    password = ''
    if spec in no and integ in no:
     for c in range(length):
       password = password + random.choice(chars)
     print(password)
    elif spec in no and integ in yes:
       for c in range(length):
         password = password + random.choice(random.choice(chars) + random.choice(chari))
       print(password)
    elif spec in yes and integ in no:
       for c in range(length):
        password = password + random.choice(random.choice(chars) + random.choice(charz))
       print(password)
    else:
       for c in range(length):
        password = password + random.choice(random.choice(chars) + random.choice(charz) + random.choice(chari))
       print(password)
  else:
      print('Wrong Input Value')
 else:
      print('Wrong Input Value')
x = 'Y'
while x in yes:
   passw()
   x = input('Do you want to continue(Y/N): ')
