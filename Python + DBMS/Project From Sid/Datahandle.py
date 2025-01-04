
def datahandle():  
    import tkinter as tk
    #from tkinter import *
    from tkinter import ttk
    import csv
    import smtplib
    from tkinter import messagebox
    
    f1=open("BOOK3.csv","r")
    a=csv.reader(f1)
    lst=list(a)
    
    f1.close()

    names=[]
    for i in lst:
        if i != []:
            z=i[0]
            names.append(z)
    
    
    def update_tree(*args):
        search_term = entry_val.get()        # changing value in entry box
                   
        for item in names:              
            if search_term.lower() in item.lower():    # searching for the keywords entered
                for i in listBox.get_children():
                    listBox.delete(i) 
                newlist=[]
                for items in lst:
                    nameword=items[0]
                    if search_term.lower() in nameword.lower():
                        newlist.append(items)
                for i, (name, score,no,jk,k,l,m) in enumerate(newlist, start=1):
                    listBox.insert("", "end", values=(i, name, score,no,jk,k,l,m))
            elif search_term=="":
                for i in listBox.get_children():
                    listBox.delete(i) 
                for i, (name, score,no,jk,k,l,m) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=(i, name, score,no,jk,k,l,m))
            
        
    def select(*args):
        
        tem=listBox.focus()
        d=listBox.item(tem)
        a=d["values"]
        kt=a[1]
        entry_val.set(kt)
        return a
    
    
    scores = tk.Toplevel() 
    scores.iconbitmap("Logo.ico")
    scores.title("LIBRARY X")
    scores.configure(bg="Black")
    scores.geometry("1130x430+65+85")
    tk.Label(scores, text="Issued  Books  List", font=("Arial",30),fg="Light blue",bg="black").place(x=400,y=0)
    #Treeview with 8 columns
    cols = ("S.no", 'Name', 'Book','PhoneNo.',"Email Address",'Issue Date','Return Date','No. of Days')
    listBox = ttk.Treeview(scores, columns=cols, show='headings',selectmode="browse")
    listBox.bind('<<TreeviewSelect>>',select)
    
    
    entry_val = tk.StringVar()                # Value of entry box
    entry_val.trace('w', update_tree)         # Updates Treeview in w mode
    
    listBox.column("S.no", minwidth=0, width=40, stretch='NO')
    listBox.column("Email Address", minwidth=0, width=180, stretch='NO')
    listBox.column("Name", minwidth=0, width=160, stretch='NO')
    for i in cols:
        if i=="S.no" or i=="Email Address" or i=="Name":
            continue
        else:
            listBox.column(i, minwidth=0, width=150, stretch='NO')
    
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.place(x=0,y=50)
    
    tempList = lst
    tempList.sort(key=lambda e: e[5], reverse=False)
    
    for i, (name, score,no,jk,k,l,m) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, name, score,no,jk,k,l,m))
    
    #head=tk.Label(scores, text="Enter the SNo. of User:", font=("Arial",10),fg="Light blue",bg="black").grid(row=4, columnspan=4)
    
    closeButton = tk.Label(scores, text="SEARCH & SELECT From The Above Table To Proceed",height=1,fg="Yellow",bg="black")
    closeButton.place(x=425 ,y=286)
    entry=tk.Entry(scores,font=15,width=30,textvariable=entry_val,fg="dark grey")
    entry.insert(0, 'Search here')
    entry.place(x=430,y=310)
    
    
    
    def details(v):
        j=entry.get()
        
        ln=len(lst)
        for i in range(0,ln):
            
            if lst[i][0]==j:
                return lst[i][v]
                break
            
    
    
    def removal():
        lines = list()
    
        phoneno=details(2)
        
        
        with open('BOOK3.csv', 'r') as readFile:
        
            reader = csv.reader(readFile)
            
            for row in reader:
                lines.append(row)                            
                if row[2]==phoneno:                    
                    lines.remove(row)
                
               
        readFile.close()   
       
        
        with open('BOOK3.csv', 'w' ,newline="") as f:
        
            writer = csv.writer(f)
            
            writer.writerows(lines)
        f.close()
        
        new=open("BOOKLIST2.csv","r")
        read1=csv.reader(new)
        newlist=[]
        for i in read1:
            newlist.append(i)
        new.close()
        c=0
        for i in newlist:
            if i != []:
                c+=1
                if i[1]==details(1):
                    newlist[c-1][5]=int(newlist[c-1][5])-1
        new=open("BOOKLIST2.csv",'w',newline="")
        x1=csv.writer(new)
        x1.writerows(newlist)
        new.close() 
        
        f.close()
        messagebox.showinfo("ERROR", "Book Returned")
        
    
    def buttn():
        
        
        y=r.get()
        
        if y==2:
            removal()
            msg="\nLibrary X\n"
            name=details(0)
            book=details(1)
            msg1="Hi " + name + ","
            
            msg2="\nThank You for issuing the book '"+book+"' from our Library"
            msg4="You are welcome to our Library whenever that bookworm inside you starts squirming."
            message=(msg+"\n"+msg1+"\n"+msg2+"\n"+"\n"+msg4)
            
            to="To: "+details(3)
            
            email_text = "\r\n".join([
                          "From: assistance4library@gmail.com",
                          to,
                          "Subject: Thank You",
                          "",
                          message
                          ])
            server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
            
            server.login("assistance4library@gmail.com", "bookworm%^&")
            server.sendmail("assistance4library@gmail.com",details(3), email_text)
                    
            server.quit()
        elif y==1:
            
            msg="\n Library X "
            name=details(0)
            book=details(1)
            rdate=details(5)
            try:
                msg1="Hi " + name + ","
                
                msg2="\nPlease return the book '"+book+"' you issued earlier"
                msg3="\nThe return date was "+rdate
                msg4="Thank You"
                message=(msg+"\n"+msg1+"\n"+msg2+msg3+"\n"+"\n"+msg4)
                
                to="To: "+details(3)
                
                email_text = "\r\n".join([
                              "From: assistance4library@gmail.com",
                              to,
                              "Subject: Book Return",
                              "",
                              message
                              ])
                server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
                
                server.login("assistance4library@gmail.com", "bookworm%^&")
                server.sendmail("assistance4library@gmail.com",details(3), email_text)
                        
                server.quit()
                messagebox.showinfo("Sent", "Reminder Sent")
                scores.destroy()
            except:
                messagebox.showerror("ERROR", "Search Entry Missing!")
    r = tk.IntVar()
    r.set(1)
    
    a=tk.Radiobutton(scores,text="Send Reminder",selectcolor="Dark red",fg="white",bg="black",activebackground="black",activeforeground="white",font=14,variable=r,value=1)
    a.place(x=425,y=345)
    b=tk.Radiobutton(scores,text="Return Book",selectcolor="Dark red",fg="white",bg="black",activebackground="black",activeforeground="white",font=14,variable=r,value=2).place(x=590,y=345)
    
    
    Enterb = tk.Button(scores, text="Confirm & Proceed",font="20", width=30,fg="Light blue",bg="black",command=buttn).place(x=428,y=385)
                        
    
    
    scores.mainloop()
