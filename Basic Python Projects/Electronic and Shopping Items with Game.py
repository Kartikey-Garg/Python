#based on options | shopping | name, welcome to xyz company | 4 options will be displayed related to electronic items | now which models you want tio purchase | when model will be displayed then its features too and price | fetures with price | buy right now or not | 10% discount now.. | payment mode | promocode | net payable amount | special category -> identify student or not | student 10 employee 20 management 25 | mens(trouser,jeans,tshirts,shirt)->brand name->shits, womens, kids | buy more ? | option electronic or cloth section | student, name, roll no, university ok | normal category -> no discount.. except promo code
def payment(n, val, user):
    n=n.upper()
    code=0
    try:
        p=int(input("1.Debit Card\n2.Credit card\n3.Net Banking\n4.UPI Payment\nChoose your payment method: "))
    except ValueError:
        print(":( Wrong input. A numerical value was expected")
    else:
        promo=input("Do you have a promo Code (Y/N): ")
        promo=promo.upper()
        if promo == "Y":
            code=input("Enter your code in BLOCK letters: ")
        elif promo == "N":
            pass
        else:
            print("Wrong Input, Session Terminated :(")
            return
        print("Actual price:", val)
        if n=="Y" and promo=="Y":
            if user==1:
                print("Net payable amount:", (val-((val*30)//100)))
            elif user==2:
                print("Net payable amount:", (val-((val*40)//100)))
            elif user==3:
                print("Net payable amount:", (val-((val*45)//100)))
            else:
                print("Net payable amount:", (val-((val*10)//100)))
        elif promo=="Y" and n=="N":
            if user==1:
                print("Net payable amount:", (val-((val*20)//100)))
            elif user==2:
                print("Net payable amount:", (val-((val*30)//100)))
            elif user==3:
                print("Net payable amount:", (val-((val*35)//100)))
            else:
                print("Net payable amount:", (val-((val*10)//100)))
        elif n=="Y" and promo=="N":
            if user==1:
                print("Net payable amount:", (val-((val*10)//100)))
            elif user==2:
                print("Net payable amount:", (val-((val*20)//100)))
            elif user==3:
                print("Net payable amount:", (val-((val*25)//100)))
            else:
                print("Net payable amount:", (val-((val*10)//100)))
        else:
            print("Net payable amount:", val)
        checkout=input("Do you want to continue checkout?(Y/N): ")
        checkout=checkout.upper()
        if checkout=="Y":
            dict={}
            try:
                dict['Name']=input("Name: ")
                dict['Email']=input("Email: ")
                dict['Contact']=int(input("Contact: "))
            except ValueError:
                dict['Contact']='None'
            try:
                dict['Address']=input("Address: ")
                dict['Card Number']=int(input("Card Number: "))
            except ValueError:
                dict['Card Number']='None'
            try:
                dict['CVV']=int(input("CVV: "))
            except ValueError:
                dict['CVV']='None'
            finally:
                for i in dict:
                    if dict[i]=='':
                        dict[i]='None'
            print("Payment Details:", dict)
            print("Order Placed Successfully")
        else:
            print("Order Cannot be placed")
    return

def cloths(user):
    k=0
    while k==0:
        try:
            a=int(input("1.Mens\t2.Womens\t3.Kids\nSelect category:"))
        except ValueError:
            print("Wrong Input, a number was expected")
        else:
            k=1
    if a==1 or a==2 or a==3:
        b=int(input("1.Trouser\t2.Jeans\t3.T-Shirt\t4.Shirt\nChoose your Choice: "))
        if b==1:
            trouser(a,user)
        elif b==2:
            jeans(a,user)
        elif b==3:
            tshirt(a,user)
        elif b==4:
            shirt(a,user)
        else:
            return
    return

def trouser(a,user):
    try:
        c=int(input("1.Peter England\t2.Park Avenue\t3.Van Heusen\nSelect Brand: "))
    except ValueError:
        print("Enter a number")
        return
    if a==1:
        if c==1:
            try:
                d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            except ValueError:
                print("A numerical value was expected")
                return
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nMaterial:Polyester\nPattern:Textured\nOccasion:Formal\nLeg Style:Trouser\nRise Style:Mid Waist\nClosure Type:Button Fly\nFit:Slim\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Check\nColor: Navy\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: terelene Rayon Spandex\nLength: Knee Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        elif c==2:
            try:
                d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            except ValueError:
                print("Numerical value was expected")
                try:
                    d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
                except ValueError:
                    print("Numerical value was expected")
                    return
            except:
                print("Something went Wrong")
                return

            if d==1:
                val=1000
                n=input("Features:-\nMaterial:Polyester\nPattern:Solid/Plain\nOccasion:Formal\nRise Style:Mid Waist\nFit:Regular\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=1200
                n=input("Features:-\nMaterial:Polyester\nPattern:Solid/Plain\nOccasion:Formal\nLeg Style: Straight\nRise Style:Mid Waist\nClosure Type:Button Fly\nFit:Regular\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=1154
                n=input("Features:-\nRelaxed Fit\nPolyester blend\nMachine wash\nMid Rise\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        elif c==3:
            try:
                d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            except ValueError:
                print("Numerical value was expected")
            except:
                print("Something Went Wrong")    
            if d==1:
                val=1379
                n=input("Features:-\nPattern:Solid\nOccasion:Formal\nColor:Black\nMaterial:64% Polyester, 34% Viscose and 2% Spandex\nTrouser Front:Flat Front\nBrand Fit:Slim Fit\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=1699
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Van Heusen\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=1380
                n=input("Features:-\nMaterial:Polyester\nPattern:Solid/Plain\nOccasion:Formal\nLeg Style: Trouser\nRise Style:Low Waist\nClosure Type:Zipper\nFit:Slim\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        else:
            return
    #women
    elif a==2:
        if c==1:
            try:
                d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            except ValueError:
                print("Numerical value is expected")
            except:
                print("Something went wrong")
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        else:
            return
    #kid
    elif a==3:
        if c==1:
            d=int(input("1.Olive Printed Track Pants\n2.Green Woven Trouser\n3.Textured Jogger Pants with Elasticated Drawstring Waistband\nChoose one: "))
            if d==1:
                val=399
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=699
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=374
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        else:
            return
    else:
        return

def jeans(a, user):
    c=int(input("1.Peter England\t2.Park Avenue\t3.Van Heusen\nSelect Brand: "))
    #men
    if a==1:
        if c==1:
            d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    trouser(a, user)
                else:
                    return
        else:
            return
        return
    #women
    elif a==2:
        if c==1:
            d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
        else:
            return
        return
    #kids
    elif a==3:
        if c==1:
            d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    jeans(a, user)
                else:
                    return
        else:
            return
    else:
        return
    return

def tshirt(a, user):
    c=int(input("1.Peter England\t2.Park Avenue\t3.Van Heusen\nSelect Brand: "))
    #men
    if a==1:
        if c==1:
            d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        else:
            return
    #women
    elif a==2:
        if c==1:
            d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        else:
            return
    #kids
    elif a==2:
        if c==1:
            d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    tshirt(a, user)
                else:
                    return
        else:
            return
    else:
        return
    return

def shirt(a, user):
    c=int(input("1.Peter England\t2.Park Avenue\t3.Van Heusen\nSelect Brand: "))
    #men
    if a==1:
        if c==1:
            d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
        else:
            return
    #women
    elif a==2:
        if c==1:
            d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
        elif c==2:
            d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
        elif c==3:
            d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            if d==1:
                val=1599
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==2:
                val=700
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    payment(n, val, user)
                elif n=="N":
                    shirt(a, user)
                else:
                    return
            elif d==3:
                val=1999
                n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                n=n.upper()
                if n=="Y":
                    result=payment(n, val, user)
                    if result=="Success":
                        print("Order Placed Successfully")
                    else:
                        print("Order Cannot be placed")
                elif n=="N":
                    shirt(a, user)
                else:
                    return
        else:
            return
    #kids
    elif a==2:
        if c==1:
            try:
                d=int(input("1.Black Solid Trousers\n2.Navy Blue Textured Trousers\n3.Navy Check Trousers\nChoose one: "))
            except ValueError:
                print("Numerical Input was expected")
            except:
                print("Something went wrong")
            else:
                if d==1:
                    val=1599
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
                elif d==2:
                    val=700
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
                elif d==3:
                    val=1999
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
        elif c==2:
            try:
                d=int(input("1.Blue Solid Trouser\n2.Black Solid Formal Trousers\n3.Solid Relaxed Fit Trousers\nChoose one: "))
            except ValueError:
                print("Numerical Input was expected")

            except:
                print("Something went wrong")
            else:
                if d==1:
                    val=1599
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
                elif d==2:
                    val=700
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
                elif d==3:
                    val=1999
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
        elif c==3:
            try:
                d=int(input("1.Van Heusen Black Trousers\n2.Black Solid Trousers\n3.Black Formal Trouser\nChoose one: "))
            except ValueError:
                print("Numerical Input was expected")
                return
            except:
                print("Something went wrong")
            else:
                if d==1:
                    val=1599
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
                elif d==2:
                    val=700
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
                elif d==3:
                    val=1999
                    n=input("Features:-\nPattern: Solid\nColor: Black\nBrand: Peter England Formal\nProduct Type: Trousers\nFit: Slim Fit\nProduct Material: Polyester Viscose\nLength: Full Length\nPrice: "+str(val)+"\nAre you asure you want to purchase this item?(Y/N): ")
                    n=n.upper()
                    if n=="Y":
                        payment(n, val, user)
                    elif n=="N":
                        shirt(a, user)
                    else:
                        return
        else:
            return
    else:
        return

def electronic(user):
    choice=input("1. Smartphoes    2.LED TV\n3.Washing Machine     4. Microwave\nWhat do you want to purchase: ")
    if choice.isalpha():
        choice=choice.lower()
    if choice == "1" or choice == "smartphones":
        try:
            model=int(input("1.POCO M2:-\n48MP AI Quad. Camera Array.\n16MP 16.9cm (6.67) FHD+ Full Screen Display.\n5000mAh. Battery.\n\n\n2.Redimi Y2:-\nAI Dual Camera. Beautify 4.0. Large 1.25 micron pixel size\nProcessor & Memory. 3GB+32GB / 4GB+64GB. Qualcomm Snapdragon 625]nBattery. 3080mAh（typ）/ 3000mAh（min)\nCamera. 16MP front camera with Selfie-light.\n\n\n3.Samsung J2:-\nDisplay 4.70-inch (540x960)\nProcessor Samsung Exynos 3475\nFront Camera 2MP\nRear Camera 5MP\nEnter serial no. for model you want to purchase:"))
        except ValueError:
            print("Numerical Input was expected")
            return
        except:
            print("Something went wrong")
            return
        if model==1:
            val=10000
            print("Features:-\n48MP AI Quad. Camera Array.\n16MP 16.9cm (6.67) FHD+ Full Screen Display.\n5000mAh. Battery.\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%' discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        elif model==2:
            val=11000
            print("Features:-\nAI Dual Camera. Beautify 4.0. Large 1.25 micron pixel size\nProcessor & Memory. 3GB+32GB / 4GB+64GB. Qualcomm Snapdragon 625]nBattery. 3080mAh（typ）/ 3000mAh（min)\nCamera. 16MP front camera with Selfie-light.\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        elif model==3:
            val=10000
            print("Features:-\nDisplay 4.70-inch (540x960)\nProcessor Samsung Exynos 3475\nFront Camera 2MP\nRear Camera 5MP\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        else:
            print("Invalid Input")
    elif choice=="2" or choice=="led tv":
        try:
            model=int(input("1.Samsung 1m 08cm (43'') AUE60 Crystal 4K UHD Smart TV:-Crystal Processor 4K\n4K UHD resolution\nMotion Xcelerator\nQ-Symphony\n\n\n2.Samsung80cm (32'') T4340 Smart HD TV:-\nHD picture quality\nFree TV, no strings attached\nUltra Clean View\nContrast Enhancer\n\n\n3.2m 16cm (85'') AU8000 Crystal 4K UHD Smart TV:-\nDynamic Crystal Color\nCrystal Processor 4K\4K UHD Resolution\nClean Cable Solution\nEnter serial no. for model you want to purchase: "))
        except ValueError:
            print("Numerical Input was expected")
            return
        except:
            print("Something went wrong")
            return
        if model==1:
            val=42000
            print("Features:-\nCrystal Processor 4K\n4K UHD resolution\nMotion Xcelerator\nQ-Symphony\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        elif model==2:
            val=33000
            print("Features:-\nHD picture quality\nFree TV, no strings attached\nUltra Clean View\nContrast Enhancer\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        elif model==3:
            val=57000
            print("Features:-\nDynamic Crystal Color\nCrystal Processor 4K\4K UHD Resolution\nClean Cable Solution\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        else:
            print("Invalid Input")
    elif choice=="3" or choice=="washing machines":
        try:
            model=int(input("1.WW60R20GLMA Front Load with Diamond Drum & Ceramic Heater 6.0Kg:-\n5 Star Energy Rating\nDiamond Drum\n15 Quick Wash\nSmart Check\nSteam\nDigital Inverter Motor\n\n\n2.Whirlpool 7.5 Kg 5 Star Semi-Automatic Top Loading Washing Machine (ACE 7.5 SUPREME, Grey Dazzle):-\nSpin Shower\n4wheels\nIn-built coller scrubber\nEasy Mobility\n\n\nLG 7.5 Kg 5 Star Semi-Automatic Top Loading Washing Machine (P7515SRAZ, Burgundy, Roller Jet Pulsator), Large:-\nRoller Jet Pulsator\nRats! No Way!\nSave Time & Water\nEnter serial no. for model you want to purchase: "))
        except ValueError:
            print("Numerical Input was expected")
            return
        except:
            print("Something went wrong")
            return
        if model==1:
            val=29999
            print("Features:-\n5 Star Energy Rating\nDiamond Drum\n15 Quick Wash\nSmart Check\nSteam\nDigital Inverter Motor\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)

        elif model==2:
            val=15786
            print("Features:-\nSpin Shower\n4wheels\nIn-built coller scrubber\nEasy Mobility\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)

        elif model==3:
            val=13989
            print("Features:-\nRoller Jet Pulsator\nRats! No Way!\nSave Time & Water\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        else:
            print("Invalid Input")
    elif choice=="4" or choice=="microwave":
        try:
            model=int(input("1.WONDERCHEF 19-Litre OTG Oven Toaster Grill (OTG)  (Black):-\nSturdy and Long-lasting\nCompact Size\nPower Consumption: 1280 W\n1 Year Wonderchef Warranty\nAutomatic Power-off\nWindow with Heat-resistant Glass\n\n\n2.Haier 20L Solo Microwave Oven(Renewed):-\n20L Capacity: Suitable for bachelors or small families\nSolo: Can be used for reheating, defrosting and cooking\nWarranty: 1 year on product, 1 year on magnetron\nMagnetron Power: 940W\n\n\nSamsung MS23J5133AG Solo MWO with Ceramic Enamel Cavity 23L:-\nCapacity: 23L (0.8Cu.ft)\nPower: 1150 W\nDisplay Type:LED (Ice Blue)\nEnter serial no. for model you want to purchase: "))
        except ValueError:
            print("Numerical Input was expected")
            return
        except:
            print("Something went wrong")
        if model==1:
            val=4289
            print("Features:-\nSturdy and Long-lasting\nCompact Size\nPower Consumption: 1280 W\n1 Year Wonderchef Warranty\nAutomatic Power-off\nWindow with Heat-resistant Glass\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        elif model==2:
            val=2999
            print("Features:-\n20L Capacity: Suitable for bachelors or small families\nSolo: Can be used for reheating, defrosting and cooking\nWarranty: 1 year on product, 1 year on magnetron\nMagnetron Power: 940W\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        elif model==3:
            val=6390
            print("Features:-\nCapacity: 23L (0.8Cu.ft)\nPower: 1150 W\nDisplay Type:LED (Ice Blue)\nPrice:Rs."+str(val)+"/-")
            n=input("*You will get '10%'discount on purchase\nDo you want to Purchase now* (Y/N) : ")
            payment(n, val, user)
        else:
            print("Invalid Input")
    else:
        print("Wrong input")
    return

def complaint(name):
    box=open(name+".txt", "w")
    statement=input("Enter your wholde complaint in a single line: ")
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
        print("File Deleted Successfully\nthankyou for visiting")        
    else:
        print("Wrong Input")
    return

def contact(name, user): #email details must be here
    return

class game:
    def __init__(self, players, name):
        self.players=players
        self.name=name

    def tambola(self):
        import random
        print("Welcome to Tambola, "+self.name)
        players=self.players
        if players >=2 and players <=10:
            for j in range(players):
                print("List for Player "+str(j+1)+": ", random.sample(range(1,100), 9))
            print("\nYour Check List:\n", random.sample(range(1,100), (players*10)))
            win=input("Enter Winner: ")
            print("Congratulations,",win)
        else:
            print("Invalid Input")
        return

class shopping:
    def __init__(self, identity, user, g):
        self.identity=identity
        self.user=user
        self.g=g
    
    def special(self):
        try:
            user=int(input("1.Student\t2.Employee\t3.Management\nWho are you : "))
        except ValueError:
            print("Please Enter your input in numbers")
        else:
            if user==1:
                college=input("College name: ")
                try:
                    roll=int(input("Roll No.: "))
                except ValueError:
                    print("Please Enter your input in numbers")
                else:
                    print("You got Verified !!, Eligible for '10%' discount")
            elif user==2:
                print("Eligible for '20%' discount")
            elif user==3:
                print("Eligible for '25%' discount")
            else:
                print("Invalid Input, Session terminated")
                sys.exit()
        return user

    def main(self):
        user=self.user
        identity=self.identity
        if identity==1 or identity==2:
            if identity==2:
                user = shopping.special(user)
            try:
                g=self.g
                if g==1:
                    electronic(user)
                elif g==2:
                    cloths(user)
                elif g==3:
                    complaint(name)
                elif g==4:
                    contact(name, user)
                else:
                    print("Session Terminated")
            except ValueError:
                print("Please Enter your input in numbers")
        else:
            print("Wrong Input")
        return

if __name__=="__main__":
    try:
        import sys
        import time
        import os
        import re
        localtime=time.asctime(time.localtime(time.time()))
        print(localtime)
        name = input("Enter your name: ")
        print(name.upper()+", Welcome to ElectroniKart\n")
        try:
            choice=int(input("1. Shopping\t2. Game\nWhat do you want to do? "))
        except ValueError:
            print("Please Enter your input in numbers")
        else:
            if choice==1:
                try:
                    choose=shopping(int(input("1.Normal Customer\t2.Special Customer\nWho are you: ")),0,int(input("1.Electronic items\t2.Cloths\t3.Complaint\t4.contact\nChoose Your category: ")))
                except ValueError:
                    print("Please Enter your input in numbers")
                else:
                    choose.main()
            elif choice==2:
                choose = game(int(input("Enter the number of players (2 to 10): ")), name)
                choose.tambola()
            else:
                print("Wrong Input")

    except Exception as e:
        print("It can be you or it's us. Contact Developer and tell him this error: ", str(e.args))
    finally:
        print("have a Good Time :)")