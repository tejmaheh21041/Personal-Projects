def infos():
    import tkinter as tk
    from tkinter import ttk
    
    
    root = tk.Toplevel()
    root.configure(bg="Black")
    root.state('zoomed')
    root.iconbitmap("Logo.ico")
    root.title("LIBRARY X")
    
    container = ttk.Frame(root)
    
    canvas = tk.Canvas(container,width=1258, height=1000)
    canvas.configure(bg="Black")
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    
    photoImageObj = tk.PhotoImage(file="info.png")           # Image 
    lab = tk.Label(scrollable_frame,width="1258",image=photoImageObj,bd="0", highlightthickness="0")
    lab.pack()
    
    
    
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    root.mainloop()
