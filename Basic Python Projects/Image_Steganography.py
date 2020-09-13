# PLEASE REMEMBER THE CURRENT CODE WILL NOT WORK IN IDLE (PYTHON DOES NOT SUPPORT STEPIC ANYMORE). ALTHOUGH YOU CAN RUN THIS CODE BY OPENING PYTHON IN COMMAND PROMPT
# MAKE SURE YOUR PYTHON & PIP ARE UPGRADED AND ALSO YOU HAVE "PILLOW" INSTALLED, TO INSTALL IT RUN THE FOLLOWING COMMAND IN CMD "pip install pillow"

from PIL import Image
import stepic
print("*******************")
print(" Image Steganography")
print("*******************")
yes = ['y', 'Y', 'YES', 'yes']
no = ['n', 'N', 'NO', 'no']
E = ['E', 'e', 'ENCODE', 'Encode', 'encode']
D = ['D', 'd', 'DECODE', 'Decode', 'decode']
tech = input("What do you want ENCODE or DECODE (E/D)? ")
if tech in E:
    img = input("Enter your Image location with image name here\nFor Ex: C/Users/.../Img_Name: ")
    im = Image.open(img)
    enc = input("Enter the data you want to hide: ")
    print("Processing....")
    enc = bytes(enc, 'utf-8')
    im1 = stepic.encode(im, enc)
    print("Done :)")
    sav = input("With what name you want to save it ?\n")
    print("Your image will be saved in PNG format only so when you are saving your file please mention extension '.png' also.")
    
    im1.save(sav, 'PNG')
    print("You are all done..")
    bol = input("Would you like to open up the image (Y/N) ?\n")
    if bol in yes:
        im1 = Image.open(sav)
        im1.show()
        act = input("Would youb like to see actual image too (y/n) ?\n")
        if act in yes:
            im.show()
        else:
            print("Bye!!")
    else:
        print("Bye!!")
else:
    img = input("Enter your Image location with image name here\nFor Ex: C/Users/.../Img_Name: ")
    im = Image.open(img)
    dec = stepic.decode(im)
    print("Your Decoded data is: ", dec)
