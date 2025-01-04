l=[] #We have created an empty stack
def add(): #Function for push
    bookno = int(input("Enter bookno.")) 
    bookname = input("Enter bookname")
    item = (bookno, bookname) #Creating item in tuple
    l.append(item)
    
def remove(): #Function for pop()
    if len(l)==0: #Condition for empty stack
        print("The stack is empty")
    else:
        l.pop() #Removing the last item from stack
        
h=True
while h==True:
    choice=input("Enter add/remove")
    if choice=="add":
        add()
    elif choice=="remove":
        remove()
    print(l)
    c=input("Would you like to continue?(y/n)")
    if c=="y":
        continue
    elif c=="n":
        h=False
    