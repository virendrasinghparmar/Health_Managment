
def getdate():
    import datetime
    return datetime.datetime.now()

def insert(k):
    if k==1:
        c=int(input("Enter 1 for Exercise and 2 for Food"))
        if c==1:
            value=input("Type Here")
            with open("virendra.txt","a") as f:
               f.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value=input("Type Here")
            with open("virendra2.txt","a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
    elif k==2:
        c=int(input("Enter 1 for Exercise and 2 for Food"))
        if c==1:
            value=input("Type Here")
            with open("anu.txt","a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value=input("Type Here")
            with open("anu2.txt","a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
    elif k==3:
        c=int(input("Enter 1 for Exercise and 2 for Food"))
        if c==1:
            value=input("Type Here")
            with open("deepak.txt.txt","a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value=input("Type Here")
            with open("deepak2.txt","a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")

def retrive(k):
    if k==1:
        c=int(input("Enter 1 for Exercise 2 for Food"))
        if c==1:
            with open("virendra.txt") as f:
                content= f.read()
                print(content)
        elif c==2:
            with open("virendra2.txt") as f:
                content=f.read()
                print(content)
    elif k==2:
        c=int(input("Enter 1 for Exercise 2 for Food"))
        if c==1:
            with open("anu.txt") as f:
                content= f.read()
                print(content)
        elif c==2:
            with open("anu2.txt") as f:
                content=f.read()
                print(content)
    elif k == 3:
        c = int(input("Enter 1 for Exercise 2 for Food"))
        if c == 1:
            with open("deepak.txt") as f:
                content = f.read()
                print(content)
        elif c == 2:
            with open("deepak2.txt") as f:
                content = f.read()
                print(content)


print("Health Managment System")

while(True):
     a=input("Press 1 for INSERT data Press 2 for RETRIVE data and 3 for Exit")
     if a=="1":
          b=int(input("Press 1 for Virendra Press 2 for Anu Press 3 for Deepak"))
          insert(b)
     elif a=="2":
          b=int(input("Press 1 for Virendra Press 2 for Anu Press 3 for Deepak"))
          retrive(b)
     elif a=="3":
           exit()
     else:
          print("PLEASE press correct input")
