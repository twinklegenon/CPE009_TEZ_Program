import sqlite3

def create():
    # connect to  database
    conn = sqlite3.connect('students_info.db')
    #create a cursor
    c = conn.cursor()
    # create a table
    c.execute("""CREATE TABLE student_s (first_name text,\
              last_name text,\
              cellphone_no integer, email text, id_pass text)""")
    
        
        # to commit
    conn.commit()
        # close connection
    conn.close()  

def insert(firstname, lastname, cellnum, emailaddress, id_pass):
   # connect to  database
   conn = sqlite3.connect('students_info.db')
    #create a cursor
   c = conn.cursor()
    # create a table

   first_name = firstname
   last_name = lastname
   cp_no = cellnum
   email = emailaddress

   c.execute("""INSERT INTO student_s (first_name ,last_name, \
                cellphone_no , email, id_pass) VALUES (?,?,?,?,?)""", \
       (first_name, last_name, cp_no, email, id_pass))
    
   print("\nInformation encoded sucessfully")
    
   # to commit
   conn.commit()
   # close connection
   conn.close()   
   
def ret():
    # connect to  database
    conn = sqlite3.connect('students_info.db')
    #create a cursor
    c = conn.cursor()
    # create a table

     
    c.execute("SELECT rowid, * FROM student_s")
    
    
    items = (c.fetchone())

    for item in items:
        print(item)
    
    
    # to commit
    conn.commit()
    # close connection
    conn.close()
    
def query(id_pass):
    # connect to  database
    conn = sqlite3.connect('students_info.db')
    #create a cursor
    c = conn.cursor()
    # create a table

     
    c.execute("SELECT rowid, * FROM student_s WHERE id_pass = (?)", (id_pass,))
    
    
    items = (c.fetchall())

    for item in items:
        print(item)
    
    
    # to commit
    conn.commit()
    # close connection
    conn.close()
    
    return items


def update(firstname, lastname, cellnum, emailaddress, id_pass):
   # connect to  database
   conn = sqlite3.connect('students_info.db')
   #create a cursor
   c = conn.cursor()
   # Updates data
   
   c.execute("""UPDATE student_s SET first_name = (?), last_name = (?), cellphone_no = (?), email = (?)
             WHERE id_pass = (?)""",(firstname, lastname, cellnum, emailaddress, id_pass))

   # to commit
   conn.commit()
   # close connection
   conn.close()
  
                              
def delete(id_pass):
        # connect to  database
    conn = sqlite3.connect('students_info.db')
    #create a cursor
    c = conn.cursor()
    
    # Insert id number to delete
    id_num = id_pass
    c.execute("DELETE from student_s WHERE id_pass = (?)",(id_num,))

    # to commit
    conn.commit()
    # close connection
    conn.close()
    
def delete_table():
     # Connects to the database
    data = sqlite3.connect('students_info.db')
    
    # Creates the cursor
    c = data.cursor()
    
    # Deletes data
    c.execute("DROP TABLE student_s")
    
    # Commits the command and close connection
    data.commit()
    data.close()
    
if __name__ == '__main__':
    delete_table()
    create()