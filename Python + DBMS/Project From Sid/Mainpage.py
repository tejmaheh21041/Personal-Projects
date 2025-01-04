import csv

import tkinter as tk
from PIL import ImageTk,Image

def mainpage():
                
                
    root = tk.Toplevel()
    root.state('zoomed')
    root.configure(background = 'Black')
    head=tk.Label(root, text="Itemname",fg="Light Blue",bg="Black" ,font=("Century Gothic",60))
    head.place(x=530,y=230) 
    
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
    
    
    
    def CurSelet(*args):
        a=listbox.get("anchor")    #get the value of the item in list
        entry_val.set(a)
     
    
    
    listbox = tk.Listbox(root ,width="40",bg="Black", fg="Light Blue",bd="0", highlightthickness="0",font="Arial 18")        #Listbox
    listbox.bind('<<ListboxSelect>>',CurSelet)  #<<ListboxSelect>> binding selects the item
                                        
       
    def useful():
        ab=searchbox.get()
        return ab
    def veryuseful():
        y=useful()
       
        
    listbox = tk.Listbox(root ,width="40",bg="Black", fg="Light Blue",bd="0", highlightthickness="0",font="Arial 18") #Listbox
    listbox.bind('<<ListboxSelect>>',CurSelet)  #<<ListboxSelect>> binding selects the item
    
    f1=open("BOOKLIST2.csv","r")
    a=csv.reader(f1)
    l=[]
    d={}
    for i in a:
        l.append(i[1])
        d[i[1]]=i[:1]+i[2:]
    
    for i in d:
            
        listbox.insert(tk.END, i)           #inserting values from the dictionary
    
    listbox.place(x=400, y=380)
    all_items = listbox.get(0, tk.END)    #Items present in the listbox
    listbox.delete(0, tk.END)
    
    
    imango=Image.open("logo2.png")
    photo = ImageTk.PhotoImage(imango)
    
    lab = tk.Label(root, image=photo, bd=0, highlightthickness=0)
    lab.image=photo
    lab.place(x=460,y=245)
    
    button = tk.Button(root, text="Search",font="CenturyGothic",fg="Darkred",width="70", height="24",command=veryuseful)
    img1 = ImageTk.PhotoImage(file="gold.png") 
    button.config(image=img1,compound="center")
    button.place(x=850,y=340)
    
    mmbutton = tk.Button(root, height=10, width=10, text="Main Menu")
    mmbutton.place(x=100,y=200)
    
    
    root.mainloop()
    
mainpage()
            