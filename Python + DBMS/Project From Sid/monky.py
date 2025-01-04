#Functions
def Encryption(c):  #To encrypt The user data and keep it protected
    import random
    
    r=random.randint(1,27)#can know how the data is bieng encrpted if you know python 
    x=""
    for i in c:      #I cannot explain it here for our user's privacy and data protection
        if i.isalpha():
            a=ord(i)
            b=a+r
            if i.isupper():
                if b>90:
                    x+=chr((b-90)+64)
                else:
                    x+=chr(b)
            else:
                if b>122:
                    x+=chr((b-122)+96)
                else:
                    x+=chr(b)
        elif i.isnumeric():
            a=int(i)
            b=a+r
            b=b%10
            x+=str(b)
        else:
            x+=i
    return(x+" "+str(r))

def Decryption(c): # To decrypt the data we encrypted
    for i in c.split():   # Because we cannot have only encryption 
        if i.isnumeric():
            r=i
    c=c[:-(len(r)+1)]
    x=""
    r=int(r)
    for i in c:
        if i.isalpha():
            a=ord(i)
            b=a-r
            if i.isupper():
                if b<65:
                    x+=chr(91-(65-b))
                else:
                    x+=chr(b)
            else:
                if b<97:
                    x+=chr(123-(97-b))
                else:
                    x+=chr(b)
        elif i.isnumeric():
            a=int(i)-r
            if r==10 or r==20:
                x+=str(i)
            elif a<=-20:
                x+=str(a+30)
            elif a<=-10:
                x+=str(a+20)
            elif a<0:
                x+=str(a+10)
            elif a>=0:
                x+=str(a)
        else:
            x+=i
    return(x)

def DecryptFile(m):  # To decrypt the who;e file of Our user data in one go 
    f1=open(m,"r")    #Using The decrypt function above
    a=f1.readlines()
    fl=[]
    for i in a:
        l=[]
        for j in i.split():
            l.append(j)
        fl.append(l)
    final=[]
    for i in fl:
        ans=[]
        for j in range(len(i)):
            if j%2==0:
                x=i[j]
            else:
                y=i[j]
                b=x+" "+y
                d=Decryption(b)
                ans.append(d)
        final.append(ans)
    return final
    f1.close()

def find(x):  # To find a user in our directory of all users
    a=DecryptFile("directory.txt")
    for i in a:
        for j in i:
            if j==x and j==i[3]:    # If user exists in our database 
                return False
                break
    else:                              # Else The username is free to use for other users
        pass
                

    