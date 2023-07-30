# -*- coding: utf-8 -*-

import tkinter as tk
import gui_info_functions as func

def gui_info():
    # Main Window
    root = tk.Tk()
    root.title('T.E.Z. Program')
    root.iconbitmap('icon.ico')
    
    # Frames
    frame = tk.LabelFrame(root, padx=20, pady=20)
    frame.pack()
    
    # Text
    title = tk.Label(frame, text = "Welcome User! This is T.E.Z.\nThe Information Manager App", font="Montserrat 12 bold")
    sub = tk.Label(frame, text = "Manage your information", font="Montserrat 8")
    
    # Button Functions
    def enter_function():
        func.f_enter()
    
    def update_function():
        func.f_update()
    
    def show_function():
        func.f_show()
    
    def delete_function():
        func.f_delete()
    
    # Buttons
    enter_info = tk.Button(frame, text="Enter your Information", command=enter_function)
    update_info = tk.Button(frame, text="Update your Information", command=update_function)
    show_info = tk.Button(frame, text="Show your Information", command=show_function)
    delete_info = tk.Button(frame, text="Delete your Information", command=delete_function)
    exit_button = tk.Button(frame, text="Exit", command=root.destroy)
    
    # Packing
    title.grid(row=0, columnspan=5)
    sub.grid(row=1, columnspan=5)
    enter_info.grid(row=2, column=2, sticky="nsew")
    update_info.grid(row=3, column=2, sticky="nsew")
    show_info.grid(row=4, column=2, sticky="nsew")
    delete_info.grid(row=5, column=2, sticky="nsew")
    exit_button.grid(row=6, column=2, sticky="nsew")
    
    root.resizable(False, False)
    tk.mainloop()
    
if __name__ == '__main__':
    gui_info()
