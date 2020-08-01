'''
This program demonstrates the use of Tkinter library.
This is a simple registration form that stores the entries in an sqlite3 database
Author: Harshit Jain
'''

from tkinter import *
import sqlite3

#root is the root of the Tkinter widget
root = Tk()

#geometry is used to set the dimensions of the window
root.geometry('550x580')

#title shows the title of the Tkinter window
root.title("Employee Form")


Name=StringVar() #Tkinter module to store strings
Email=StringVar()
Designation=StringVar()
Gender = IntVar()
Languages=IntVar()

def database():
   name=Name.get()
   email=Email.get()
   designation=Designation.get()
   gender=Gender.get()
   languages=Languages.get()
   # lang=Favorite_Language.get()
   connection = sqlite3.connect('Form.db') #Connection instance
   with connection:
      cursor=connection.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Employee (Name TEXT, Email TEXT, Designation TEXT, Gender TEXT,Languages TEXT)')
   cursor.execute('INSERT INTO Employee (Name,Email,Designation,Gender,Languages) VALUES(?,?,?,?,?)',(name,email,designation,gender,languages))
   connection.commit()
   exit()
   
             
label_title = Label(root, text="Employee form",width=20,font=("bold", 30))
label_title.place(x=35,y=53)


label_name = Label(root, text="Name",width=20,font=("bold", 13))
label_name.place(x=40,y=130)

entry_box_name = Entry(root,textvar=Name)
entry_box_name.place(x=240,y=130)

label_email = Label(root, text="Email",width=20,font=("bold", 13))
label_email.place(x=40,y=180)

entry_box_email = Entry(root,textvar=Email)
entry_box_email.place(x=240,y=180)

label_gender = Label(root, text="Gender",width=20,font=("bold", 13))
label_gender.place(x=40,y=230)

var=IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 5, variable=var, value=2).place(x=235,y=250)

label_designation = Label(root, text="Designation",width=20,font=("bold", 13))
label_designation.place(x=40,y=280)

designation_list = ['Software Developer','Software Intern','Software Tester','HR Manager','Business Development Manager']

droplist=OptionMenu(root,Designation, *designation_list)
droplist.config(width=15)
Designation.set('Choose Designation') 
droplist.place(x=240,y=280)

label_languages = Label(root, text="Languages Known",width=20,font=("bold", 13))
label_languages.place(x=40,y=330)

english_var= IntVar()
hindi_var=IntVar()
french_var=IntVar()
Checkbutton(root, text="English", variable=english_var).place(x=235,y=330)
Checkbutton(root, text="Hindi", variable=hindi_var).place(x=235,y=350)
Checkbutton(root, text="French", variable=french_var).place(x=235,y=370)

Button(root, text='Submit',width=20,bg='green',fg='white',command=database).place(x=180,y=410)
root.mainloop()

