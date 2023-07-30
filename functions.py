# -*- coding: utf-8 -*-

import gui_info as info
import tkinter as tk
import modules as md

def f_login():
    login = tk.Tk()
    login.title("Login")
    login.iconbitmap('icon.ico')
    
    # Frames
    frame = tk.LabelFrame(login, padx=10, pady=20)
    frame.grid(sticky="NSEW")
    
    # Function
    def login_check():
        username = user_box.get()
        password = password_box.get()
        login_code = int(code_box.get())
        
        # Checks if the user is an admin
        item = md.accounts_data_usersearch(username)
        if username == 'admin':
            login.destroy()
            f_admin()
            
        # Checks Data 
        elif item != []:
            for i in item:
                if i == (username, password, login_code):
                    login.destroy()
                    info.gui_info()
                    tk.messagebox.showinfo(title="Information", message="Login Successful!")
                else:
                    user_box.delete(0, tk.END)
                    password_box.delete(0, tk.END)
                    code_box.delete(0, tk.END)
                    tk.messagebox.showwarning("Information", "Incorrect Credentials")

                    
        else:
            user_box.delete(0, tk.END)
            password_box.delete(0, tk.END)
            code_box.delete(0, tk.END)
            tk.messagebox.showwarning("Information", "Username does not exists.")
    
    # Text
    login_label = tk.Label(frame, text="Enter your information", font="montserrat 11 bold", pady=10)
    user_label = tk.Label(frame, text="Username", font="montserrat 9")
    password_label = tk.Label(frame, text="Password", font="montserrat 9")
    code = tk.Label(frame, text="Login Code", font="montserrat 9")
    
    # Button
    enter = tk.Button(frame, text="Login", padx=20, command=login_check)
    
    # Entry box
    user_box = tk.Entry(frame)
    password_box = tk.Entry(frame, show="*")
    code_box = tk.Entry(frame, show="*")
    
    # Packing
    login_label.pack()
    user_label.pack()
    user_box.pack()
    password_label.pack()
    password_box.pack()
    code.pack()
    code_box.pack()
    enter.pack()
    
    login.resizable(False, False)
    tk.mainloop()
    
# Admin
def f_admin():
    # Main Window
    admin = tk.Tk()
    admin.title('Admin Mode')
    admin.iconbitmap('icon.ico')
    
    # Shows all saved data
    def selection():
        entry = heading_entry.get()
        if entry == "Show All":
            buffer = md.accounts_data_query()
            
            for item in buffer:
                data = tk.Label(frame2, text=item, pady=2)
                data.pack(anchor="w")
            else:
                data = tk.Label(frame2, text="End of List")
                data.pack(anchor="w")
            
        # Deletes the entire table. Creates a new table
        elif entry == "Delete Data":
            md.delete_data()
            tk.messagebox.showinfo("Information", "Data Deletion Successful!")
            md.accounts_data_create()
    
    # Frames
    frame = tk.LabelFrame(admin, padx=30, pady=30)
    frame.pack(anchor="n", fill=tk.BOTH)
    frame2 = tk.LabelFrame(admin, padx=30, pady=30)
    frame2.pack(anchor="s", fill=tk.BOTH)
    
    # Display
    heading = tk.Label(frame, text="Show All | Delete Data", font="montserrat 10")
    heading_entry = tk.Entry(frame)
    select_button = tk.Button(frame, text="Enter", command=selection)
    
    # Packing
    heading.grid(row=0, columnspan=3)
    heading_entry.grid(row=1, columnspan=3)
    select_button.grid(row=2, column=1, sticky="NSEW")
    
    admin.resizable(False, False)
    tk.mainloop()
    
# Register
def f_register():
    # Main Window
    register = tk.Tk()
    register.title('Register')
    register.iconbitmap('icon.ico')
    
    # Function
    def registration():
        username = user_box.get()
        password = password_box.get()
        login_code = int(code_box.get())
        
        # Checks if already registered
        item = md.accounts_data_usersearch(username)
        
        try:
            if item[0][0] == username:
                user_box.delete(0, tk.END)
                password_box.delete(0, tk.END)
                code_box.delete(0, tk.END)
                tk.messagebox.showinfo(title="Information", message="Already Registered!")
        except:
            # Inserts inputted data into the database
            md.accounts_data_insert(username, password, login_code)
            register.destroy()
            tk.messagebox.showinfo("Information", "Registration Successful!")
            

    # Frames
    frame = tk.LabelFrame(register, padx=30, pady=30)
    frame.grid(sticky="NSEW")
    
    # Text
    register_label = tk.Label(frame, text="Register your information", font="montserrat 11 bold", pady=10)
    user_label = tk.Label(frame, text="Username", font="montserrat 9")
    password_label = tk.Label(frame, text="Password", font="montserrat 9")
    code = tk.Label(frame, text="Login Code", font="montserrat 9")
    
    # Entry box
    user_box = tk.Entry(frame)
    password_box = tk.Entry(frame, show="*")
    code_box = tk.Entry(frame, show="*") 
    
    # Button
    register_button = tk.Button(frame, text="Register", padx=20, command=registration)
    
    # Packing
    register_label.grid(row=0, columnspan=3)
    user_label.grid(row=1, columnspan=3)
    user_box.grid(row=2, columnspan=3)
    password_label.grid(row=3, columnspan=3)
    password_box.grid(row=4, columnspan=3)
    code.grid(row=5, columnspan=3)
    code_box.grid(row=6, columnspan=3)    
    register_button.grid(row=7, column=1, sticky="NSEW")
    
    register.resizable(False, False)
    tk.mainloop()
    
def f_about():
    # Main Window
    about = tk.Tk()
    about.title('About')
    about.iconbitmap('icon.ico')
    
    # Frames
    frame = tk.LabelFrame(about, padx=30, pady=30)
    frame.pack()
    
    # Text
    member_title = tk.Label(frame, text="Members", font="montserrat 11 bold", pady=10)
    members_list = [{"Name": "Mayordo, Zherish Galvin"}, 
                    {"Name": "Genon, Twinkle"},
                    {"Name": "Estranero Jonlix"}
                    ]
    
    # Packing
    member_title.pack()
    for item in members_list:
       members_item = tk.Label(frame, text=item["Name"], font="montserrat 9")
       members_item.pack()
    
    about.resizable(False, False)
    tk.mainloop()
