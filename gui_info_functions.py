# -*- coding: utf-8 -*-

import info as i
import tkinter as tk

def f_enter():
    enter = tk.Tk()
    enter.title('Enter Your Information')
    enter.iconbitmap('icon.ico')
    
    frame = tk.LabelFrame(enter, padx=40, pady=40)
    frame.grid()
    
    # Text
    first_name = tk.Label(frame, text="First Name", font="Montserrat 10")
    last_name = tk.Label(frame, text="Last Name", font="Montserrat 10")
    cell_num = tk.Label(frame, text="Cellphone Number", font="Montserrat 10")
    email = tk.Label(frame, text="Email Address", font="Montserrat 10")
    id_pass = tk.Label(frame, text="ID Password", font="Montserrat 10")
    
    # Functions
    def submit_function():
        info_firstname = first_name_entry.get()
        info_lastname = last_name_entry.get()
        info_cellnum = cell_num_entry.get()
        info_email = email_entry.get()
        info_id_pass = id_pass_entry.get()
        
        check = i.query(info_id_pass)
        
        try:
            if check[0][1] == info_firstname:
                first_name_entry.delete(0, tk.END)
                last_name_entry.delete(0, tk.END)
                cell_num_entry.delete(0, tk.END)
                email_entry.delete(0, tk.END)
                id_pass_entry.delete(0, tk.END)
                tk.messagebox.showinfo(title="Information", message="Information Exists Already.")
                
        except:
            i.insert(info_firstname, info_lastname, info_cellnum, info_email, info_id_pass)
            enter.destroy()
            tk.messagebox.showinfo(title="Information", message="Successful.")
    
    # Buttons
    submit = tk.Button(frame, text="Submit", command=submit_function)
    
    # Entry Boxes
    first_name_entry = tk.Entry(frame)
    last_name_entry = tk.Entry(frame)
    cell_num_entry = tk.Entry(frame)
    email_entry = tk.Entry(frame)
    id_pass_entry = tk.Entry(frame, show="*")
    
    # Packing
    first_name.grid(row=0, column=0, columnspan=3)
    first_name_entry.grid(row=1, columnspan=3, sticky="nsew")
    last_name.grid(row=2, column=0, columnspan=3)
    last_name_entry.grid(row=3, columnspan=3, sticky="nsew")
    cell_num.grid(row=4, column=0, columnspan=3)
    cell_num_entry.grid(row=5, columnspan=3, sticky="nsew")
    email.grid(row=6, column=0, columnspan=3)
    email_entry.grid(row=7, columnspan=3, sticky="nsew")
    id_pass.grid(row=8, column=0, columnspan=3)
    id_pass_entry.grid(row=9, column=0, columnspan=3, sticky="nsew")
    submit.grid(row=10, column=1, sticky="nsew")
    
    enter.resizable(False, False)
    tk.mainloop()
    
def f_update():
    update = tk.Tk()
    update.title('Update Your Information')
    update.iconbitmap('icon.ico')
    
    frame = tk.LabelFrame(update, padx=40, pady=40)
    frame.grid()
    
    # Text
    first_name = tk.Label(frame, text="First Name", font="Montserrat 10")
    last_name = tk.Label(frame, text="Last Name", font="Montserrat 10")
    cell_num = tk.Label(frame, text="Cellphone Number", font="Montserrat 10")
    email = tk.Label(frame, text="Email Address", font="Montserrat 10")
    id_pass = tk.Label(frame, text="ID Password", font="Montserrat 10")
    
    # Functions
    def submit_function():
        info_firstname = first_name_entry.get()
        info_lastname = last_name_entry.get()
        info_cellnum = cell_num_entry.get()
        info_email = email_entry.get()
        info_id_pass = id_pass_entry.get()
        
        try:
            validate = i.query(info_id_pass)
            if validate != []:
                i.update(info_firstname, info_lastname, info_cellnum, info_email, info_id_pass)
                tk.messagebox.showinfo(title="Information", message="Information Updated.")
            else:
                tk.messagebox.showinfo(title="Information", message="ID Pass is not valid.")
        except:
            tk.messagebox.showinfo(title="Information", message="Error.")
    
    # Buttons
    submit = tk.Button(frame, text="Submit", command=submit_function)
    
    # Entry Boxes
    first_name_entry = tk.Entry(frame)
    last_name_entry = tk.Entry(frame)
    cell_num_entry = tk.Entry(frame)
    email_entry = tk.Entry(frame)
    id_pass_entry = tk.Entry(frame, show="*")
    
    # Packing
    first_name.grid(row=0, column=0, columnspan=3)
    first_name_entry.grid(row=1, columnspan=3, sticky="nsew")
    last_name.grid(row=2, column=0, columnspan=3)
    last_name_entry.grid(row=3, columnspan=3, sticky="nsew")
    cell_num.grid(row=4, column=0, columnspan=3)
    cell_num_entry.grid(row=5, columnspan=3, sticky="nsew")
    email.grid(row=6, column=0, columnspan=3)
    email_entry.grid(row=7, columnspan=3, sticky="nsew")
    id_pass.grid(row=8, column=0, columnspan=3)
    id_pass_entry.grid(row=9, column=0, columnspan=3, sticky="nsew")
    submit.grid(row=10, column=1, sticky="nsew")
    
    update.resizable(False, False)
    tk.mainloop()
    
def f_show():
    show = tk.Tk()
    show.title('Show Your Information')
    show.iconbitmap('icon.ico')
    
    frame = tk.LabelFrame(show, padx=40, pady=40)
    frame.grid()
    
    # Text
    id_pass = tk.Label(frame, text="ID Pass", font="Montserrat 10")
    
    # Entry
    id_pass_entry = tk.Entry(frame, show="*")
    
    # Button Function
    def show_function():
        item = i.query(id_pass_entry.get())
        id_pass_entry.delete(0, tk.END)
        
        for j in item:
            label = tk.Label(frame, text=j, font="Montserrat 10 bold")
            label.grid()
    
    # Button
    show_button = tk.Button(frame, text="Show", command=show_function)
    
    # Packing
    id_pass.grid(row=0)
    id_pass_entry.grid(row=1, sticky='nsew')
    show_button.grid(row=2, sticky='nsew')
    
    show.resizable(False, False)
    tk.mainloop()
    
def f_delete():
    delete = tk.Tk()
    delete.title('Delete your Information')
    delete.iconbitmap('icon.ico')
    
    frame = tk.LabelFrame(delete, padx=40, pady=40)
    frame.grid()
    
    # Text
    id_pass = tk.Label(frame, text="ID Pass", font="Montserrat 10")
    
    # Entry
    id_pass_entry = tk.Entry(frame, show="*")
    
    # Button Function
    def delete_function():
        try:
            validate = i.query(id_pass_entry.get())
            if validate != []:
                i.delete(id_pass_entry.get())
                id_pass_entry.delete(0, tk.END)
                tk.messagebox.showinfo(title="Information", message="Information Deleted.")
            else:
                tk.messagebox.showinfo(title="Information", message="ID Pass is not valid.")
        except:
            tk.messagebox.showinfo(title="Information", message="Error.")
    
    # Button
    delete_button = tk.Button(frame, text="Delete", command=delete_function)
    
    # Packing
    id_pass.grid(row=0)
    id_pass_entry.grid(row=1, sticky='nsew')
    delete_button.grid(row=2, sticky='nsew')
    
    delete.resizable(False, False)
    tk.mainloop()
    
