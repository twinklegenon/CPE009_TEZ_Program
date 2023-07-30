# -*- coding: utf-8 -*-

import tkinter as tk
import functions as fn


# Main Window
root = tk.Tk()
root.title('T.E.Z. Program')
root.iconbitmap('icon.ico')

# Frames
frame = tk.LabelFrame(root, padx=10, pady=20)
frame.pack()

# Text
title = tk.Label(frame, text="Welcome to T.E.Z. Program", font="Montserrat 13 bold")
sub = tk.Label(frame, text="A program by Zherish, Twinkle, and Jonlix", font="Montserrat 8")

# Button Functions
def login():
    fn.f_login()
    
def register():
    fn.f_register()

def about():
    fn.f_about()
    
# Buttons
b_login = tk.Button(frame, text="Login", command=login)
b_register = tk.Button(frame, text="Register", command=register)
b_about = tk.Button(frame,text="About", command=about)
b_exit = tk.Button(frame, text="Exit", command=root.destroy)

# Specify Grid
tk.Grid.rowconfigure(root,0,weight=1) 
tk.Grid.columnconfigure(root,0,weight=1)  
tk.Grid.rowconfigure(root,1,weight=1) 

# Packing
title.grid(row=0, columnspan=4)
sub.grid(row=1, columnspan=4)
b_login.grid(row=2, column=1, columnspan=2, sticky="NSEW")
b_register.grid(row=3, column=1, columnspan=2, sticky="NSEW")
b_about.grid(row=4, column=1, sticky="NSEW")
b_exit.grid(row=4, column=2, sticky="NSEW")

root.resizable(False, False)
tk.mainloop()
