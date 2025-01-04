# Signup Page

#importss

from tkinter.scrolledtext import ScrolledText
import monky as func
import tkinter as tk
import smtplib
from tkinter import messagebox
from datetime import date
from PIL import ImageTk, Image
import csv
import random
from datetime import timedelta
import Datahandle
import webbrowser


def signup():
    global sign
    try:
        win.destroy()
    except:
        pass
    try:
        sign.destroy()
    except:
        pass
    sign = tk.Tk()
    sign.geometry("340x400+450+150") # Window Geometry
    sign.iconbitmap("Logo.ico") # Icon Setup
    sign.title("LIBRARY X")  # Title
    sign.configure(bg="Black") # Background  color
    sign.resizable(0,0)  # This prevents from resizng the window
    
    #BUTTONS, LABELS and ENTRIES
    head=tk.Label(sign, text="SIGN-UP",fg="Light Blue",bg="Black" ,font=("Arial",34))
    head.grid(column=1, row=0) 
    
    l1=tk.Label(sign,text="Name:",fg="Light Blue",bg="Black" ,font=("Arial", 12))
    l1.grid(column=0,row=1) 
    
    txt1=tk.Entry(sign,fg="Light blue",bg="Black", width="30",insertbackground='yellow')
    txt1.grid(column=1, row=1) 
    
    l1=tk.Label(sign,text="Surname:",fg="Light Blue",bg="Black" ,font=("Arial", 12))
    l1.grid(column=0,row=2)
    
    txt2=tk.Entry(sign,fg="Light blue",bg="Black", width="30",insertbackground='yellow')
    txt2.grid(column=1, row=2)   
    
    l1=tk.Label(sign,text="Email-ID:",fg="Light Blue",bg="Black" ,font=("Arial", 12))
    l1.grid(column=0,row=3)
    
    txt3=tk.Entry(sign,fg="Light blue",bg="Black", width="30",insertbackground='yellow')
    txt3.grid(column=1, row=3)   
    
    l1=tk.Label(sign,text="Username:",fg="Light Blue",bg="Black" ,font=("Arial", 12))
    l1.grid(column=0,row=4)
    
    txt4=tk.Entry(sign,fg="Light blue",bg="Black", width="30",insertbackground='yellow')
    txt4.grid(column=1, row=4)   
    
    
    l1=tk.Label(sign,text="Password:",fg="Light Blue",bg="Black" ,font=("Arial", 12))
    l1.grid(column=0,row=5)
    
    txt5=tk.Entry(sign,fg="Light blue",bg="Black", show="*",width="30",insertbackground='yellow')
    txt5.grid(column=1, row=5)   #Password Entry
    
    l1=tk.Label(sign,text="Re-Enter:",fg="Light Blue",bg="Black" ,font=("Arial", 12))
    l1.grid(column=0,row=6)
    
    txt6=tk.Entry(sign,fg="Light blue",bg="Black", show="*",width="30",insertbackground='yellow')
    txt6.grid(column=1, row=6)   #Password Rentry
    
    f1=open("directory.txt",'r')
    a=f1.readlines()
    
    if a==[]: # First person to signup will be the administrator
        head=tk.Label(sign, text="Signin As the Administrator",fg="yellow",bg="Black" ,font=("Arial",12))
        head.grid(column=1,row=7)
    else:
        l1=tk.Label(sign,text="Code",fg="Light Blue",bg="Black" ,font=("Arial", 12))
        l1.grid(column=0,row=7)
        
        txt7=tk.Entry(sign,fg="Light blue",bg="Black",insertbackground='yellow',width="30")
        txt7.grid(column=1, row=7)   #Password Rentry
        
    f1.close()
    
    def mold(*args):
        f1=open("directory.txt",'r') # Directory.txt contains the encrypted details of staff
        a=f1.readlines()
        if a!=[]: # Signup Condition for Admistrator
            # Obtaining Values through get()
            name=txt1.get()
            surname=txt2.get()
            email=txt3.get()
            username=txt4.get()
            password=txt5.get()
            renter=txt6.get()
            code=txt7.get()
            
            # Error Conditions:
            condition="@" and "." in email # Email Condition
            
            if name=="":
                messagebox.showerror("ERROR","Pls Enter a Name") # Empty Entry box error
            elif surname=="":
                messagebox.showerror("ERROR","Pls Enter a Surname")
            elif email=="":
                messagebox.showerror("ERROR","Pls Enter a Email")
            elif username=="":
                messagebox.showerror("ERROR","Pls Enter a username")
            elif password=="":
                messagebox.showerror("ERROR","Pls Enter a password")
            elif renter=="":
                messagebox.showerror("ERROR","Pls Re-enter your password")
            elif code=="":
                messagebox.showerror("ERROR","Pls Enter a code given to you")
            else:
                f1=open("Codes.txt","r") # Code search in codes.txt contains all codes
                a=f1.readlines()
                for i in a:
                    if "\n" in i:
                        i=i[:-1]
                        a.append(i)
                if func.find(username)!=False and renter == password and code in a: # If username already exists error shows
                    if condition==True:
                        
                        f1=open("directory.txt","a")
                        f1.write(func.Encryption(name))     # Details have been encrypted for security
                        f1.write(" ")                       # Using Encrytion() in monky library
                        f1.write(func.Encryption(surname))
                        f1.write(" ")
                        f1.write(func.Encryption(email))
                        f1.write(" ")
                        f1.write(func.Encryption(username))
                        f1.write(" ")
                        f1.write(func.Encryption(password))        
                        f1.write("\n")
                        f1.close()
                        
                        reveal=("Your password is : ",password)     # Sending welcome mail to the user
                        rev=''.join(reveal)
                        msg="\nLibrary X "
                        msg1="Hi"+""+name+","
                        msg2="\nWelcome to LibraryX, The newest library app"
                               
                        message=(msg+"\n"+msg1+"\n"+"Your username is : "+username+"\n"+rev+msg2)
                        
                        to="To: "+email
            
                        email_text = "\r\n".join([
                          "From: assistance4library@gmail.com",
                          to,
                          "Subject: Welcome to Library X",
                          "",
                          message
                          ])
                        
                        server=smtplib.SMTP_SSL("smtp.gmail.com", 465) # Opening Connection to gmail
                        
                        server.login("assistance4library@gmail.com", "bookworm%^&") # Email Login
                        server.sendmail("assistance4library@gmail.com",email, email_text)
                                
                                
                        server.quit() # Quitting Server
                        messagebox.showinfo("Welcome", "Signin Successful!🎉")
                        f=open("Codes.txt",'r')
                        a=f.readlines()
                        var=[]
                        for i in a:
                            
                            var.append(i)
                        var.remove(code+"\n")
                        f.close()
                        f1=open("Codes.txt",'w')
                        f1.writelines(var)
                        f1.write("          ")
                        
                        sign.destroy()                      # destroy() can be used to close tk windows
                    else:
                       
                        messagebox.showerror("ERROR", "Invalid email!") 
            
                else:
                    
                    if func.find(username)==False:
                        messagebox.showerror("ERROR", "Username Already Exists")
                    elif renter != password:
                        messagebox.showerror("ERROR" , "Re-enter Correctly!")
                    elif code not in a:
                        messagebox.showerror("ERROR" , "Code doesn't match") 
        else: # Signup Condition for General Staff(Same as above but with code entry)
            name=txt1.get()
            surname=txt2.get()
            email=txt3.get()
            username=txt4.get()
            password=txt5.get()
            renter=txt6.get()

            condition="@" and "." in email
            if name=="":
                messagebox.showerror("ERROR","Pls Enter a Name")
            elif surname=="":
                messagebox.showerror("ERROR","Pls Enter a Surname")
            elif email=="":
                messagebox.showerror("ERROR","Pls Enter an EmailID")
            elif username=="":
                messagebox.showerror("ERROR","Pls Enter a username")
            elif password=="":
                messagebox.showerror("ERROR","Pls Enter a password")
            elif renter=="":
                messagebox.showerror("ERROR","Pls Re-enter your password")
            
            else:
                f1=open("Codes.txt","r")
                a=f1.readlines()
                if func.find(username)!=False and renter == password:
                    if condition==True:
                        head=tk.Label(sign, text="   Signing Successful!   ",fg="yellow",bg="Black" ,font=("Arial",12))
                        head.grid(column=1, row=10)
                        sign.destroy()
                        f1=open("directory.txt","a")
                        f1.write(func.Encryption(name))
                        f1.write(" ")
                        f1.write(func.Encryption(surname))
                        f1.write(" ")
                        f1.write(func.Encryption(email))
                        f1.write(" ")
                        f1.write(func.Encryption(username))
                        f1.write(" ")
                        f1.write(func.Encryption(password))        
                        f1.write("\n")
                        f1.close()
                        
                        reveal=("Your password is : ",password)
                        rev=''.join(reveal)
                        msg="\n Library X "
                        msg2="\nWelcome to LibraryX, The newest library app"
                        msg1="Hi"+name+","    
                        message=(msg+"\n"+msg1+"\n"+"Your username is : "+username+"\n"+rev+msg2)
            
                        to="To: "+email
            
                        email_text = "\r\n".join([
                          "From: assistance4library@gmail.com",
                          to,
                          "Subject: Welcome to LibraryX",
                          "",
                          message
                          ])
                        
                        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
                        
                        server.login("assistance4library@gmail.com", "bookworm%^&") # Email Login
                        server.sendmail("assistance4library@gmail.com",email, email_text) # Arguments (From, To, Message)
                                
                                
                        server.quit() #Quitting Server
                        messagebox.showinfo("Welcome", "Signin Successful!🎉")
                    else:
                        messagebox.showerror("ERROR","Pls Enter a valid EmailID")
                else:
                    if func.find(username)==False:
                        messagebox.showerror("ERROR", "Username Already Exists")
                    elif renter != password:
                        messagebox.showerror("ERROR" , "Re-enter Correctly!")
    rad3=tk.Button(sign, text="SIGN-UP",fg="Light Blue",bg="Black", font=("Arial",22),command=mold)
    rad3.grid(column=1, row=11)
    
    sign.bind('<Return>', mold)  # Entry binded to mold function
    
    sign.mainloop()
 

# Forgot Password
    
def dont_forget():
    forgot=tk.Tk()
    forgot.geometry("300x200+470+180")
    forgot.iconbitmap("Logo.ico")
        
    forgot.title("FORGOT PASSWORD")
    forgot.configure(bg="Black")
    forgot.resizable(0,0)  # this prevents from resizng the window
            
             
        
    #BUTTONS and ENTRIES
    head=tk.Label(forgot, text="Forgot",fg="Light blue",bg="Black" ,font=("Arial",25))
    head.grid(column=0, row=1)
    
    head=tk.Label(forgot, text="Password?",fg="Light blue",bg="Black" ,font=("Arial",25))
    head.grid(column=1, row=1)
    
    head=tk.Label(forgot, text="",fg="Light blue",bg="Black" ,font=("Arial",12))
    head.grid(column=1, row=3)
    
    head=tk.Label(forgot, text="Enter Your Email-",fg="Light blue",bg="Black" ,font=("Arial",12))
    head.grid(column=1, row=4)
       
    l1=tk.Label(forgot,text="Email ID:",fg="Light blue",bg="Black",font=("white", 12))
    l1.grid(column=0,row=5)
        
    txt1=tk.Entry(forgot,fg="Light blue",bg="Black", width="30",insertbackground='yellow')
    txt1.grid(column=1, row=5)   #Username Entry
    
    
        
    d=func.DecryptFile("directory.txt")
               
    def forget(*args): 
        email=txt1.get()            
        for i in d:
            if i!=[]:        
                if i[2]==email: # Checking if email exists in Directory
                    password=i[4]
                    
                    reveal=("Your password is : ",password)   # Mail for Password Recovery
                    rev=''.join(reveal)
                    msg="\n Library X "
                    msg2="\nYou can now login "+i[0]+" ...WELCOME BACK!"
                           
                    message=(msg+"\n"+rev+msg2)
        
                    to="To: "+email
                
                    email_text = "\r\n".join([
                      "From: assistance4library@gmail.com",
                      to,
                      "Subject: Password Recovery",
                      "",
                      message
                      ])
                    
                    server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    
                    server.login("assistance4library@gmail.com", "bookworm%^&")
                    server.sendmail("assistance4library@gmail.com",email, email_text)
                            
                            
                    server.quit()
                    condition=1
                    break
                else:
                
                    condition=0
            else:
                
                condition=0
        
        if  condition==0 :
            messagebox.showerror("ERROR", "Email not registered or Wrong Email!")
            
        if  condition==1 :  
            messagebox.showinfo("SENT", "Email Sent!")
            forgot.destroy()
    
            
    head=tk.Label(forgot, text="",fg="Light blue",bg="Black",font=("Arial",12))
    head.grid(column=1, row=7)
    
    rad3=tk.Button(forgot, text="GET PASSWORD",fg="Light blue",bg="Black", font=("Arial",15), command=forget)
    rad3.grid(column=1, row=8)
        
    forgot.bind('<Return>', forget)    
    forgot.mainloop()
#Login Page

def login():
    global win
    try:
        sign.destroy()
    except:
        pass
    try:
        win.destroy()
    except:
        pass
    win=tk.Tk()
    win.geometry("340x360+450+150")
    
    win.iconbitmap("Logo.ico")
    win.title("LIBRARY X")
    win.configure(bg="Black")
    win.resizable(0,0)  # this prevents from resizng the window
        
         
    
        #BUTTONS and ENTRIES
    head=tk.Label(win, text="LOGIN",fg="Light blue",bg="Black" ,font=("Arial",34))
    head.grid(column=1, row=0)  #Login Heading
    
    l1=tk.Label(win,text="Username:",fg="Light blue",bg="Black",font=("Arial", 12))
    l1.grid(column=0,row=1)
    
    txt1=tk.Entry(win,fg="Light blue",bg="Black", width="30",insertbackground='yellow')
    txt1.grid(column=1, row=1)   #Username Entry
    
        
    l1=tk.Label(win,text="Password:",fg="Light blue",bg="Black",font=("Arial", 12))
    l1.grid(column=0,row=2)
      
    txt2=tk.Entry(win,fg="Light blue",bg="Black",show="*" ,width="30",insertbackground='yellow')
    txt2.grid(column=1, row=2)   #Password Entry
    
    
    def gold(*args):
        username=txt1.get()
        password=txt2.get()
          
        
        
        d=func.DecryptFile("directory.txt")
            
        condition=0          
        for i in d: # Paasword Condition
            if i!=[]:
                if i[3]==username:
                    if i[4]==password:
                        head=tk.Label(win, text="Welcome to Library X",fg="Light blue",bg="Black" ,font=("Arial",12))
                        head.grid(column=1, row=7)
                        win.destroy()
                        condition=1
                        
                        break
                    else:
                        messagebox.showerror("ERROR", "Wrong Password!")
                        condition=2
                        break
                else:
                    continue
                    condition=0
            else:
                continue
                
        if condition==0:
            messagebox.showerror("ERROR", "Wrong Username!") 
            
        if condition==1:
            def mainpage(): # Function for searchbox
                
                
                root = tk.Toplevel()
                root.state('zoomed')
                root.iconbitmap("Logo.ico")
                root.title("Test Cashier")
                root.configure(background = 'Black')
                head=tk.Label(root, text="Itemname",fg="Light Blue",bg="Black" ,font=("Century Gothic",60))
                head.place(x=510,y=230) 
                
                def update_listbox(*args):         #fuction for updatingthe list  # *args for variable number of arguments 
                  
                  search_term = entry_val.get()        # changing value in entry box
                  
                      
                  listbox.delete(0, tk.END)            # (0,tk.end) is the range of listbox
                  for item in all_items:
                    if search_term=="":                #If nothing is entered the listbox is emptied
                        listbox.delete(0, tk.END)
                        
                    elif search_term.lower() in item.lower():    #searching for the keywords entered
                        listbox.insert(tk.END, item)             #updating the listbox as the user enters
                    
                entry_val = tk.StringVar()                # Value of entry box
                entry_val.trace('w', update_listbox)      #writes the updated results in listbox
                
                searchbox = tk.Entry(root, width="40",font="Arial 18",textvariable=entry_val)
                
                searchbox.place(x=400, y=340)
                
                
                def issue2(*args):
                    
                    sign2.destroy()
                    sign = tk.Toplevel()
                    sign.geometry("537x270+392+180")
                    sign.iconbitmap("Logo.ico")
                    sign.title("LibraryX")
                    sign.configure(bg="Black")                    
                    ab=searchbox.get()
                    
                    head=tk.Label(sign, text=ab,fg="Light Blue",bg="Black",font=("Arial",34))
                    head.grid(column=1, row=0)                 
                    
                    l1=tk.Label(sign,text="Enter Your Name",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                    l1.grid(column=0,row=1)
                    
                    l2=tk.Entry(sign,fg="Light Blue",bg="Black",insertbackground="Yellow",font=("Arial", 12))
                    l2.grid(column=1,row=1)
                    
                    l3=tk.Label(sign,text="Enter Your Phone No.",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                    l3.grid(column=0,row=2)
                    
                    l4=tk.Entry(sign,fg="Light Blue",bg="Black",insertbackground="Yellow",font=("Arial", 12))
                    l4.grid(column=1,row=2)
                    
                    l5=tk.Label(sign,text="Enter Your Email address",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                    l5.grid(column=0,row=3)
                    
                    l6=tk.Entry(sign,fg="Light Blue",bg="Black",insertbackground="Yellow",font=("Arial", 12))
                    l6.grid(column=1,row=3)
                    
                    l7=tk.Label(sign,text="Enter No of days",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                    l7.grid(column=0,row=4)
                    def jam(): # Function for no. of. days
                        global NODays
                        NODays=clicked.get()
                    clicked= tk.StringVar()
                    clicked.set("           1 Week           ")

                    drop=tk.OptionMenu(sign, clicked, "           3 Days           ","           1 Week           ", "           2 Weeks           ", "           1 Month           ") # Dropbox contain options for duration of issue
                    drop.config(width = 23)
                    drop.grid(column=1,row=4)
                                
                    
                    f1=open("BOOK3.csv",'a',newline="")
                    a=csv.DictWriter(f1,["Name","BookName","Phone No","Email","Issuedate","Return Date","No of days"])
                    
                    
                    def ex(*args):       
                        jam()
                        datex = date.today() # Obtaining Date
                        name=l2.get()
                        phone=l4.get()
                        email=l6.get()
                        
                        opening=open("BOOK3.csv","r")
                        reading=csv.reader(opening)
                        lists=[]
                        for i in reading:
                            lists.append(i)
                        for i in range(len(lists)): 
                            if phone==lists[i][2]:
                                condition2=2
                                break
                            else:
                                condition2=1
                        
                        
                        condition3=0
                        max_no_list=[]
                        for i in range(len(lists)):
                            if name==lists[i][0]:
                                condition3=1
                                try:
                                    int(lists[i][0][-1])
                                except:
                                    integer_not_present=True
                                    
                                if integer_not_present==True:
                                    signno=0
                                    max_no_list.append(signno)
                                else:
                                    
                                    signno=int(lists[i][0][-1])
                                    max_no_list.append(signno)
                            else:
                                continue
                        
                        if condition3==1:
                            max_no=str(max(max_no_list)+1)
                            name=name+max_no
                        
                        condition="@" and "." in email
                        if name=="":
                            messagebox.showerror("ERROR","Pls Enter a Name")                   
                        
                        elif phone=="":
                            messagebox.showerror("ERROR","Pls Re-enter your Phoneno.")
                        
                        elif email=="":
                            messagebox.showerror("ERROR","Pls Enter a EmailID")
                        else:
                            if condition==True:                            
                                if NODays=="           3 Days           ":
                                    day=3
                                elif NODays=="           1 Week           ":
                                    day=7
                                elif NODays=="           2 Weeks           ":
                                    day=14
                                elif NODays=="           1 Month           ":
                                    day=30
                                y=NODays.strip()
                                
                                x=5*day
                                final="Issuing Successful!"+"\nAmount to be paid is : ₹" + str(x)
                                messagebox.showinfo("Bill",final)
                                    
                                xdate= datex + timedelta(days=day)
                                
                                a.writerow({"Name":name,"BookName":ab,"Phone No":phone,"Email":email,"Issuedate":datex,"Return Date":xdate,"No of days":y})
                                head=tk.Label(sign, text="   Issuing Successful!   ",fg="yellow",bg="Black" ,font=("Arial",12))
                
                                head.grid(column=1, row=6)
                                f1.close()
                                
                                f=open("BOOK3.csv","r")
                                a3=csv.reader(f)
                                newl=[]
                                for i in a3:
                                    newl.append(i)
                                f.close()
                                
                                f2=open("BOOK3.csv","w",newline="")
                                for i in newl:
                                    if len(i)<7:
                                        newl.remove(i)
                                a2=csv.writer(f2)
                                a2.writerows(newl)
                                f2.close()
                                
                                new=open("BOOKLIST2.csv","r")
                                read1=csv.reader(new)
                                newlist=[]
                                for i in read1:
                                    newlist.append(i)
                                new.close()
                                c=0
                                
                                for i in newlist:
                                    c+=1
                                    if i != []:
                                        if i[1]==ab:
                                            newlist[c-1][5]=int(newlist[c-1][5])+1
                                new=open("BOOKLIST2.csv",'w',newline="")
                                x1=csv.writer(new)
                                x1.writerows(newlist)
                                new.close()
                                sign.destroy()
                            else:
                                messagebox.showerror("ERROR", "Invalid Email")
                        
                    rad=tk.Button(sign, text="Issue",fg="Light blue",bg="Black", font=("Arial",20),command=ex)
                    rad.grid(column=1,row=7)
                    sign.bind('<Return>', ex)

                def varwin(x):
                    global sign2
                    import tkinter as tk
                    import csv
                    from tkinter import messagebox
                    
                    f1=open("BOOKLIST2.csv","r")
                    a=csv.reader(f1)
                    d={}
                    for i in a:
                        if i != []:
                            d[i[1]]=i[:1]+i[2:]
                    f1.close()
                    if x in d:
                        sign2 = tk.Tk()
                        sign2.geometry("537x340+392+150")
                        sign2.iconbitmap("Logo.ico")
                        sign2.title("LibraryX")
                        sign2.configure(bg="Black")
                        
                        def issue(*args):
                            
                            if int(d[x][3])-int(d[x][4])==0:
                                sign2.destroy()
                                messagebox.showerror("ERROR", "Sorry No more books available at the time")
                                f1.close()
                            else:
                                issue2()
                        f1.close()                   
                        head=tk.Label(sign2, text=x,fg="deepskyblue1",bg="Black" ,font=("Arial",34))
                        head.grid(column=1, row=0) 
                        
                        l1=tk.Label(sign2,text="OVERVIEW: ",fg="white",bg="Black" ,font=("Arial", 15))
                        l1.grid(column=0,row=2)
                        
                        l2=ScrolledText(sign2,width=18,height=6,fg="yellow",bd="0", highlightthickness="0",bg="Black" ,font=("Arial", 12),insertbackground='yellow')
                        l2.grid(column=1,row=2)
                        l2.insert(tk.INSERT,d[x][1])
                        l2.configure(state ='disabled') 
                        
                        l3=tk.Label(sign2,text="CATEGORY: ",fg="white",bg="Black" ,font=("Arial", 15))
                        l3.grid(column=0,row=3)
                        
                        l4=tk.Label(sign2,text=d[x][2],fg="yellow",bg="Black" ,font=("Arial", 12))
                        l4.grid(column=1,row=3) 
                        
                        l5=tk.Label(sign2,text="COPIES: ",fg="white",bg="Black" ,font=("Arial", 15))
                        l5.grid(column=0,row=4)
                        
                        l6=tk.Label(sign2,text=d[x][3],fg="yellow",bg="Black" ,font=("Arial", 12))
                        l6.grid(column=1,row=4)
                        
                        l7=tk.Label(sign2,text="ISSUED: ",fg="white",bg="Black" ,font=("Arial", 15))
                        l7.grid(column=0,row=5)
                        
                        l8=tk.Label(sign2,text=d[x][4],fg="yellow",bg="Black" ,font=("Arial", 12))
                        l8.grid(column=1,row=5)
                        
                        l9=tk.Label(sign2,text="AUTHOR",fg="white",bg="Black" ,font=("Arial", 15))
                        l9.grid(column=0,row=6)
                        
                        l10=tk.Label(sign2,text=d[x][5],fg="yellow",bg="Black" ,font=("Arial", 12))
                        l10.grid(column=1,row=6)
                        
                        rad2=tk.Button(sign2, text="ISSUE",fg="black",bg="grey", font=("Arial",20),command=issue)
                        rad2.grid(column=1, row=7)
                        sign2.bind('<Return>', issue)
                        sign2.mainloop()
                    else:
                        messagebox.showerror("ERROR", "Book Not Available!") 
                        forgot=tk.Tk()
                        forgot.geometry("300x200")
                        forgot.iconbitmap("Logo.ico")
                        forgot.geometry("340x400+450+150")
                        forgot.title("FORGOT PASSWORD")
                        forgot.configure(bg="Black")
                                #BUTTONS and ENTRIES
                        head=tk.Label(forgot, text="Suggest book",fg="Light blue",bg="Black" ,font=("Arial",25))
                        head.grid(column=1, row=1)#Login Heading
                        
                        head=tk.Label(forgot, text="",fg="Light blue",bg="Black" ,font=("Arial",12))
                        head.grid(column=1, row=3)
                        
                        head=tk.Label(forgot, text="Enter Your Suggestion-",fg="Light blue",bg="Black" ,font=("Arial",12))
                        head.grid(column=1, row=4)
                           
                        l1=tk.Label(forgot,text="BOOK :",fg="Light blue",bg="Black",font=("white", 12))
                        l1.grid(column=0,row=5)
                            
                        txt1=tk.Entry(forgot,fg="Light blue",bg="Black",insertbackground='yellow', width="30")
                        txt1.grid(column=1, row=5)   #Username Entry
                        
                        def Suggest(*args):
                            f1=open("Suggestion.txt",'a')
                            x=txt1.get()
                            f1.write(x)
                            f1.write("\n")
                            l1=tk.Label(forgot,text="Thank You for Your Suggestion",fg="Light blue",bg="Black",font=("white", 12))
                            l1.grid(column=1,row=7)
                        
                        rad3=tk.Button(forgot, text="Done",fg="Light Blue",bg="Black", font=("Arial",22),command=Suggest)
                        rad3.grid(column=1, row=11)
                        forgot.bind('<Return>', Suggest)
                        forgot.mainloop()

                def NewEmployee():
                    x=''
                    for i in range(8): #Random 8 digit code is generated
                        a=random.randint(0,9) 
                        x+=str(a)
                    data_string = tk.StringVar()
                    data_string.set(x)
                    sign = tk.Tk()
                    sign.geometry("320x100+480+50")
                    sign.iconbitmap("Logo.ico")
                    sign.title("LibraryX")
                    sign.configure(bg="Black") 
                    
                    
                    
                    lab=tk.Label(sign,text="Copy the code for adding new staff:",fg="deepskyblue1",bg="Black" ,font=("Arial", 15))
                    lab.grid(column=0,row=0)
                    
                    ent = tk.Entry(sign,text=x,fg="black",bg="Black",font=("Arial", 18))
                    ent.insert(0, x)
                    ent.configure(width=8)
                    ent.configure(state='readonly')
                    ent.grid(column=0, row=1)
                    f1=open("Codes.txt",'a+')
                    f1.write(x)
                    f1.write("\n")
                    f1.close()
                    
                def CurSelet(*args):
                    a=listbox.get("anchor")    #get the value of the item in list
                    entry_val.set(a)           #setting value in entry box as selected
                 
                def useful():
                    ab=searchbox.get()         #get value from searchbox
                    return ab
                
                def veryuseful(*args):
                    y=useful()                 #recieve updated search results when function is called
                    varwin(y)
                
                listbox = tk.Listbox(root ,width="40",bg="Black", fg="Light Blue",bd="0", highlightthickness="0",font="Arial 18")        #Listbox
                listbox.bind('<<ListboxSelect>>',CurSelet)  #< Listbox binding to selects the items
                                                    
             
                
                f1=open("BOOKLIST2.csv","r")
                a=csv.reader(f1)
                l=[]
                d={}
                
                for i in a:
                    if i != []:
                        l.append(i[1])
                        d[i[1]]=i[:1]+i[2:]
                    else:
                        pass
                if "Name" in d.keys():
                    d.pop("Name")
                if "Name" in l:
                    l.remove("Name")
                
                for i in l:
                        
                    listbox.insert(tk.END, i)           #inserting values from the dictionary
                
                listbox.place(x=400, y=380)
                all_items = listbox.get(0, tk.END)    #Items present in the listbox
                listbox.delete(0, tk.END)
                
                
                imango=Image.open("logo2.png")
                photo = ImageTk.PhotoImage(imango)
                
                lab = tk.Label(root, image=photo, bd=0, highlightthickness=0)
                lab.image=photo
                lab.place(x=430,y=245)
                
                button = tk.Button(root, text="Search",font="CenturyGothic",fg="Darkred",width="70", height="24",command=veryuseful)
                img1 = ImageTk.PhotoImage(file="gold.png") 
                button.config(image=img1,compound="center")
                root.bind('<Return>', veryuseful)
                button.place(x=850,y=340)
                
                def menu():
                    
                    win3=tk.Tk()
                    win3.geometry("300x200+975+85")
                    win3.configure(background = 'Black')
                    win3.iconbitmap("Logo.ico")
                        
                    win3.title("")
                    
                    win3.resizable(0,0)
                    
                    def data():
                        win3.destroy()
                        Datahandle.datahandle()
                    
                    but1=tk.Button(win3,text="Issued books",bg="black",fg="white",font=("Arial",20), width=20,command=data)
                    but1.grid(column=0,row=1)
                    
                    def Addbook():
                        sign = tk.Tk()
                        sign.geometry("300x370+975+310")
                        sign.iconbitmap("Logo.ico")
                        sign.title("LibraryX")
                        sign.configure(bg="Black")

                        head=tk.Label(sign, text="AddBook",fg="Light Blue",bg="Black" ,font=("Arial",34))
                        head.grid(column=1, row=0) 
                                                
                        l11=tk.Label(sign,text="Name",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                        l11.grid(column=0,row=3)
                        
                        l12=tk.Entry(sign,fg="Light Blue",bg="Black" ,font=("Arial", 12),insertbackground='yellow')
                        l12.grid(column=1,row=3)
                        
                        l9=tk.Label(sign,text="Author",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                        l9.grid(column=0,row=4)
                        
                        l10=tk.Entry(sign,fg="Light Blue",bg="Black" ,font=("Arial", 12),insertbackground='yellow')
                        l10.grid(column=1,row=4)
                        
                        l1=tk.Label(sign,text="Overview",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                        l1.grid(column=0,row=7)
                        
                        l2=ScrolledText(sign,width=18,height=6,fg="Light Blue",bg="Black" ,font=("Arial", 12),insertbackground='yellow')
                        l2.grid(column=1,row=7)
                        
                        l3=tk.Label(sign,text="Categories",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                        l3.grid(column=0,row=5)
                        
                        l4=tk.Entry(sign,fg="Light Blue",bg="Black" ,font=("Arial", 12),insertbackground='yellow')
                        l4.grid(column=1,row=5) 
                        
                        l5=tk.Label(sign,text="No of Books",fg="Light Blue",bg="Black" ,font=("Arial", 12))
                        l5.grid(column=0,row=6)
                        
                        l6=tk.Entry(sign,fg="Light Blue",bg="Black" ,font=("Arial", 12),insertbackground='yellow')
                        l6.grid(column=1,row=6)
                
                        def info1(*args):
                            info=l2.get('1.0', tk.END)
                            cat=l4.get()
                            NOBooks=l6.get()
                            author=l10.get()
                            name=l12.get()
                            if info=="":
                                messagebox.showerror("ERROR","Pls Enter Info")
                            elif cat=="":
                                messagebox.showerror("ERROR","Pls Enter a Category")
                            elif NOBooks=="":
                                messagebox.showerror("ERROR","Pls Enter Quantity")
                            elif author=="":
                                messagebox.showerror("ERROR","Pls Enter Author Name")
                            elif name=="":
                                messagebox.showerror("ERROR","Pls Enter Book Name")
                            else:
                                f1=open('BOOKLIST2.csv','r')
                                reader = csv.reader(f1)
                                listos=[]
                                for row in reader:
                                    listos.append(row)
                                if listos[-1]!=[]:
                                    s=listos[-1][0]
                                else:
                                    count=-1
                                    for i in range (0,len(listos)):
                                        count-=1
                                        if listos[count]!=[]:
                                            s=listos[count][0]
                                            break
                                        else:
                                            continue
                                        
                                f1.close()
                                f1=open("BOOKLIST2.csv","a",newline="")
                                a=csv.DictWriter(f1,["S.No","Name","Info","Categories","Quantity","Issued","Author"])
                                a.writerow({"S.No":int(s)+1,"Name":name,"Info":info,"Categories":cat,"Quantity":NOBooks,"Issued":0,"Author":author})
                                f1.close()
                                l1=tk.Label(sign,text="Added Successfully",fg="yellow",bg="Black" ,font=("Arial", 12))
                                l1.grid(column=1,row=8)
                            
                        rad2=tk.Button(sign, text="ADD",fg="Light blue",bg="Black", font=("Arial",20),command=info1)
                        rad2.grid(column=1, row=9)
                        sign.bind('<Return>', info1)
                        sign.mainloop()
                    
                    but2=tk.Button(win3,text="Add books",bg="black",fg="white",font=("Arial",20),width=20,command=Addbook)
                    but2.grid(column=0,row=2)
                    
                    def Suggestion():
                       webbrowser.open("Suggestion.txt") 
                       win3.destroy()
        
                    but3=tk.Button(win3,text="Suggestion",bg="black",fg="white",font=("Arial",20),width=20,command=Suggestion)
                    but3.grid(column=0,row=3)
                    
                    exitbut=tk.Button(win3, text="EXIT MENU",bg="black",fg="red",font=("Arial",13,'underline'),bd="0", highlightthickness="0", command=win3.destroy)
                    exitbut.grid(column=0,row=4)
                    
                    win3.mainloop()
                
                image = Image.open('ninedots.png')
                new_image = image.resize((50, 50))
                new_image.save('nine.png')
                
                img2 = tk.PhotoImage(file="nine.png")  
                mmbutton = tk.Button(root,width=50,height=50,bd="0", highlightthickness="0",image=img2, command=menu)
                
                
                mmbutton.place(x=1220,y=10)
                
                def Extra():
                    e = tk.Tk()
                    e.geometry("340x400")
                    e.iconbitmap("Logo.ico")
                    e.title("LibraryX")
                    e.configure(bg="Black")
                    e.resizable(0,0) 
                    rad1=tk.Button(e, text="SIGN-UP",fg="Light Blue",bg="Black", font=("Arial",22),command=issue2)
                    rad1.grid(column=1, row=11)
                    e.bind('<Return>', issue2)
                    
                for i in func.DecryptFile("directory.txt"):
                    if username in i:
                        if func.DecryptFile("directory.txt").index(i)==0:
                            lab7=tk.Label(root,text="ADMINISTRATOR",fg="Light blue",bg="Black" ,font=("Arial", 22))
                            lab7.place(x=550,y=10)
                            rad2=tk.Button(root, text="GENERATE CODE",fg="Light blue",bg="Black", font=("Arial",12),command=NewEmployee)
                            rad2.place(x=10,y=10)
                            
                root.mainloop()

            mainpage()
            
    
    
    rad2=tk.Button(win, text="Forgot password?",fg="Light blue",bg="Black", font=("Arial",10),command=dont_forget)
    rad2.grid(column=1, row=10)
       
    
    rad3=tk.Button(win, text="LOGIN",fg="Light blue",bg="Black", font=("Arial",22),command=gold)
    rad3.grid(column=1, row=8)
    
    win.bind('<Return>', gold)
    
    win.mainloop()






