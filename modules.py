# -*- coding: utf-8 -*-

import sqlite3 as s
from os import system, name

# Clear display
def clear():
    if name == 'nt':
        _ = system('cls')
        
    else:
        _ = system('clear')

# Creates table for accounts.db
def accounts_data_create():
    
    # Connects to the database
    data = s.connect('accounts.db')
    
    # Creates the cursor
    c = data.cursor()
    
    # Creates the table
    c.execute("""CREATE TABLE users (
              username text,
              password text,
              login_code integer
              )""")
  
    # Commits the command and close connection
    data.commit()
    data.close()
    
# Inserts data into database  
def accounts_data_insert(username, password, login_code):
    
    # Connects to the database
    data = s.connect('accounts.db')
    
    # Creates the cursor
    c = data.cursor()
    
    # Stores data into a buffer
    buffer = (username, password, login_code)
    
    # Stores data from buffer to database
    c.execute("INSERT INTO users VALUES (?,?,?)", buffer)
    
    # Commits the command and close connection
    data.commit()
    data.close()
    
# Query the database
def accounts_data_query():
    
    # Connects to the database
    data = s.connect('accounts.db')
    
    # Creates the cursor
    c = data.cursor()
    
    # Query and Fetch
    c.execute("SELECT rowid, * FROM users")
    buffer = c.fetchall()
    
    # Commits the command and close connection
    data.commit()
    data.close()
    
    return buffer

# Search for specific data
def accounts_data_usersearch(user):
    
    # Connects to the database
    data = s.connect('accounts.db')
    
    # Creates the cursor
    c = data.cursor()
    
    # Checks for username
    c.execute("SELECT * FROM users WHERE username = (?)", (user,))
    
    items = c.fetchall()
    
    # Commits the command and close connection
    data.commit()
    data.close()
    
    return items
    
def accounts_data_update(user_id, code, new_password):
    
    # Connects to the database
    data = s.connect('accounts.db')
    
    # Creates the cursor
    c = data.cursor()
    
    # Updates data
    try:
        c.execute("""UPDATE users SET password = (?)
              WHERE username = (?) AND login_code = (?)
              """, new_password, user_id, code)
              
    except:
        print("Incorrect Credentials")
              
    # Commits the command and close connection
    data.commit()
    data.close()
    
def delete_data():
    
    # Connects to the database
    data = s.connect('accounts.db')
    
    # Creates the cursor
    c = data.cursor()
    
    # Deletes data
    c.execute("DROP TABLE users")
    
    # Commits the command and close connection
    data.commit()
    data.close()