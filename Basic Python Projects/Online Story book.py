#online story book | name ? | which storybook ? | remembered any last keywoard ? where you last read | are you satisfied ? no- jump to 2nd keyword and continues | 
class OnlineStoryBook:
    print("Welcome to Online story book")
    def __init__(self, name):
        self.name=name
        self.path="C://Users//Kartikey Garg//Documents//DITU Library"
        self.book=None

    def filedisp(self, b):
        fo=open(self.path+"//"+self.book,"r+", encoding="utf8")
        for line in fo:
            if b==-1:
                for line in fo:
                    print(line)
                    try:
                        input("\nPress enter to Continue....")
                    except:
                        ("Thankyou for reading")
                        return
            else:
                if b in line:
                    for line in fo:
                        print(line)
                        try:
                            input("\nPress enter to Continue....")
                        except:
                            print("Thankyou for reading")
                            return
        fo.close()
        return

    def books(self):
        k=os.listdir(self.path)
        for x in k:
            if x.endswith(".pdf"):
                print(x)
        self.book=input("Which storybook you want to read ? ")
        if self.book in k:
            #fo= os.path.abspath(self.path)
            #path_to_acrobat = os.path.abspath('C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe')
            fo=open(self.path+"//"+self.book,"r", encoding="utf8")
            word=input("Where you were at? (None/last keyword): ")
            lines = fo.readlines()
            if word=="None":
                #process = subprocess.Popen([path_to_acrobat, '/A', 'page=1', fo], shell=False, stdout=subprocess.PIPE)
                #process.wait()
                return -1
                
            elif type(word):
                new_list = []
                index = 0
                for line in lines: 
                    if word in line:
                         new_list.insert(index, line)
                         index+=1
                if len(new_list)==0:
                    print("\n\"" +word+ "\" is not found in \"" +self.book+ "\"!")
                else:
                    lineLen = len(new_list)
                    print("\n**** Lines containing \"" +word+ "\" ****\n")
                    for i in range(lineLen):
                        #print(end=new_list[i])
                        searchObj = re.search(r'(.*) '+word+' (.*?) .*', new_list[i], re.M|re.I)
                        if searchObj:
                            print(searchObj.group(1)+" '"+word+"' "+searchObj.group(2))
                            x=input("\nIs this the line: ")
                            x=x.upper()
                            if x == "Y":
                                b=new_list[i]
                                print("Happy reading :)\n\n", new_list[i])
                                fo.close()
                                break
                    return b
            else:
                print("Wrong Input")
            fo.close()    
        else:
            print("Wrong Input")   
        fo.close()

if __name__=='__main__':
    import os
    import re
    store=OnlineStoryBook(input("Enter Name: "))
    b=store.books()
    store.filedisp(b)