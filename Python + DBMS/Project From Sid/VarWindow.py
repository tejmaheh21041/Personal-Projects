def varwin(x):
    import tkinter as tk
    import csv
    from tkinter import messagebox
    import datetime
    from datetime import date
    f1=open("BOOKLIST2.csv","r")
    a=csv.reader(f1)
    d={}
    for i in a:
        d[i[1]]=i[:1]+i[2:]
    sign = tk.Tk()
    
    sign.iconbitmap("Logo.ico")
    sign.title("LibraryX")
    sign.configure(bg="black")
    if x in d:
        
        
        head=tk.Label(sign, text=x,fg="yellow",bg="black" ,font=("Arial",34))
        head.pack()
        
        l1=tk.Label(sign,text="Info",fg="yellow",bg="black" ,font=("Arial", 12))
        l1.pack(side="left")
        
        l2=tk.Label(sign,text=d[x][1],fg="yellow",bg="Black" ,font=("Arial", 12))
        l2.pack(side="left")
        
        l3=tk.Label(sign,text="Categories",fg="Light Blue",bg="Black" ,font=("Arial", 12))
        l3.pack(side="left")
        
        l4=tk.Label(sign,text=d[x][2],fg="Light Blue",bg="Black" ,font=("Arial", 12))
        l4.pack()
        
        l5=tk.Label(sign,text="No of Books",fg="Light Blue",bg="Black" ,font=("Arial", 12))
        l5.pack()
        
        l6=tk.Label(sign,text=d[x][3],fg="Light Blue",bg="Black" ,font=("Arial", 12))
        l6.pack()
        
        l7=tk.Label(sign,text="Issued",fg="Light Blue",bg="Black" ,font=("Arial", 12))
        l7.pack()
        
        l8=tk.Label(sign,text=d[x][4],fg="Light Blue",bg="Black" ,font=("Arial", 12))
        l8.pack()
    else:
        messagebox.showerror("ERROR", "Book Not Available!") 
    
    sign.mainloop()
varwin("Tin Tin")