# Intro screen

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import Sign_func as sign
from Sign_func import signup,login
import Infopage

image = Image.open('Newest.png')
image.thumbnail((1400, 800))
image.save('Newest2.png')

root = Tk()
root.title(" LIBRARY X  ")
root.iconbitmap("Logo.ico")

root.configure(background = 'Black')



backimage=ImageTk.PhotoImage(Image.open("Newest2.png"))
root.state('zoomed') #Full screen
w = backimage.width()
h = backimage.height()

def ht():
    Infopage.infos()


cv = tk.Canvas(width=7, height=200,bd="0", highlightthickness="0")
cv.pack(side='bottom', fill='both', expand='yes')
cv.create_image(0, 0, image=backimage, anchor='nw')

image = Image.open('logo2.png')
new_image = image.resize((45, 45))
new_image.save('logo5.png')
                
photoImageObj = PhotoImage(file="logo5.png")
lab = Label(root, image=photoImageObj,bd="0", highlightthickness="0")
lab.pack(side='left', anchor='n')


lab = Label(root, text="Library X",font=("CenturyGothic",29),fg="white",bg="black")
lab.pack(side='left', anchor='n')

button = tk.Button(root, text="INFO", font=("bold",13),width="120", height="30", command=ht)
img1 = ImageTk.PhotoImage(file="gold.png") 
button.config(image=img1,compound=CENTER)
button.pack(side='right', padx=10, pady=5, anchor='n')

button1 = tk.Button(root, text="LOGIN", font=("bold",13),width="120", height="30",command=login)
img2 = ImageTk.PhotoImage(file="gold.png") 
button1.config(image=img2,compound=CENTER)
button1.pack(side='right', padx=10, pady=5, anchor='n')

button2 = tk.Button(root, text="SIGNUP", font=("bold",13),width="120", height="30",command=signup)
img3 = ImageTk.PhotoImage(file="gold.png") 
button2.config(image=img3,compound=CENTER)
button2.pack(side='right', padx=10, pady=5, anchor='n')
root.mainloop()