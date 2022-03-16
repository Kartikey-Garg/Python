def alert():
    print("Class Alerted")

def database(name):
    dict= {'Sumit Aggarwal': {'Cabin No': 1, 'Conatct': 8982232321}, 'Prakash Kher': {'Cabin No': 2, 'Conatct': 8982232327}, 'Ram Verma': {'Cabin No': 7, 'Conatct': 8982252383}}
    k=2
    while k!=0:
        k-=1
        name=input("Enter Name: " )
        for key in dict:
            if key==name:
                return dict[name]
        else:
            print("No such teacher Found")
    return

def search_t():
    name=input("Name teacher you want to search: ")
    details = database(name)
    if details != None:
        print(details)
    else:
        print("Session terminated")
    return

def complaint(user, SAP):
    name=SAP+"_"+user
    box=open(name+".txt", "w")
    if user == '1':
        statement=input("Enter detailed complain in a single line: ")
    else:
        statement=input("Enter name and reason of complain about teacher in a single line: ")
    box.write(statement)
    print("You wrote:")
    box=open(name+".txt","r+")
    str=box.read()
    print(str)
    box.close()
    choice=input("Do you want to submit the form?(Y/N): ")
    choice=choice.upper()
    if choice=="Y":
        print("Form Saved successfully")
    elif choice=="N":
        os.remove(name+".txt")
        print("File Deleted Successfully\nThankyou for visiting")        
    else:
        print("Wrong Input")
    return

def attendance_rec(user, SAP):
    name=SAP+"_"+user
    box=open(name+".txt", "w")
    statement=input("Enter valid reason in a single line: ")
    box.write(statement)
    print("You wrote:")
    box=open(name+".txt","r+")
    str=box.read()
    print(str)
    box.close()
    choice=input("Do you want to submit the form?(Y/N): ")
    choice=choice.upper()
    if choice=="Y":
        print("Form Saved successfully")
    elif choice=="N":
        os.remove(name+".txt")
        print("File Deleted Successfully\nThankyou for visiting")        
    else:
        print("Wrong Input")
    return

def class_cancel(user, SAP):
    name=SAP+"_"+user
    box=open(name+".txt", "w")
    if user == '1':
        statement=input("Enter your Input to inform class in a single line: ")
    else:
        statement=input("Enter valid reason in a single line: ")
    box.write(statement)
    print("You wrote:")
    box=open(name+".txt","r+")
    str=box.read()
    print(str)
    box.close()
    choice=input("Do you want to submit the form?(Y/N): ")
    choice=choice.upper()
    if choice=="Y":
        print("Form Saved successfully")
        if user == '1':
            alert()
    elif choice=="N":
        os.remove(name+".txt")
        print("File Deleted Successfully\nThankyou for visiting")        
    else:
        print("Wrong Input")
    return

def logdata(email, SAP, user, choice):
    box=open("log.txt", "a")
    box.write("\n\n")
    box.write(time.asctime(time.localtime(time.time())))
    box.write("\nEmail: {}, SAP: {}, Type: {}, Choice: {}".format(email, SAP, user, choice))
    box.close()
    return

if __name__ == '__main__':
    try:
        from datetime import date
        import time
        import os
        import sys
        email=''
        SAP=''
        user=''
        choice=''
        if os.path.isfile('./log.txt'):
            pass
        else:
            box=open("log.txt", "w")
            box.close()
        print(str(date.today())+"\nWelcome to DIT University")
        email=input("Enter your College ID: ")
        try:
            SAP = email[:email.index("@")]
        except ValueError:
            print("This is not your College Email, Session terminated :(")
            sys.exit()
        user=input("1.Faculty\t2. Student\nWho are you?(1/2): ")
        if user == '1':
            id = input("Enter Faculty ID: ")
        elif user == '2':
            id= input("Enter Roll no: ")
        else:
            print("Wrong Input, Session terminated :(")
            sys.exit()
        choice=int(input("1. Search teacher\t2. Submit Complain\n3. Request for Attendance\n4. Request/Inform for Class Cancellation\nWhat do you want? "))
        if choice == 1:
            search_t()
        elif choice==2:
            complaint(user, SAP)
        elif choice==3:
            attendance_rec(user, SAP)
        elif choice==4:
            class_cancel(user, SAP)
        else:
            print("Wrong Input, Session terminated :(")
            sys.exit()
    except Exception as e:
        print("It can be you or it's us. Contact Developer and tell him this error: ", str(e.args))
    finally:
        logdata(email, SAP, user, choice)
        print("Have a good Time ahead")