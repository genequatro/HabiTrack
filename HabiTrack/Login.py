from customtkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox
import pymysql


root = CTk()


# Functions
    
def signup_user():
  if nameEntry.get()=="" or emailEntry.get()=="" or password1Entry.get()=="" or password2Entry.get()=="" :
    messagebox.showerror("Error" , "All fields are required")
  elif password1Entry.get() != password2Entry.get():
    messagebox.showerror("Error", "Password Mismatch")
  else:
    try:
      con = pymysql.connect(host='localhost', user='root', password='Jinqtro25.')
      cur = con.cursor()
    except:
      messagebox.showerror("Error", "Database connectivity issue, Please try again.")
      return
    
    try:
      cur.execute('CREATE DATABASE HabiTrack')
      cur.execute('USE HabiTrack')
      cur.execute("""CREATE TABLE user (
      userid INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      email VARCHAR(100) NOT NULL,
      password VARCHAR(100) NOT NULL
      ); """)
    except:
      cur.execute('USE HabiTrack')

    cur.execute('SELECT * FROM user where email=%s', (emailEntry.get()))
    row = cur.fetchone()
    if row != None:
      messagebox.showerror('Error', 'Email already exists')
    else:

      cur.execute("INSERT INTO user (name, email, password) VALUES (%s,%s,%s)",(nameEntry.get(), emailEntry.get(), password1Entry.get()))
      con.commit()
      con.close()
      messagebox.showinfo("Success", "Registration is succesful")

      login_page()

def login_user(): 
  if login_emailEntry.get() == "" or login_passwordEntry.get() == "":
    messagebox.showerror("Error", "All fields are required")
  else: 
    try:
      # Establishing database connection
      con = pymysql.connect(host='localhost', user='root', password='Jinqtro25.')
      cur = con.cursor()
    except:
      messagebox.showerror("Error", "Database connectivity issue, Please try again.")
      return
    try:
      # Verifying user credentials
      cur.execute('USE HabiTrack')
      cur.execute('SELECT * FROM data WHERE email=%s AND password=%s', (login_emailEntry.get(), login_passwordEntry.get()))
      record = cur.fetchone()
      
      if record is None:
        messagebox.showerror("Error", "Wrong Email or Password")
      else: 
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()  # Close the login window 
      
    finally:
      con.close()  # Ensure the database connection is closed


def signup_page():
  loginFrame1.grid_forget()
  loginFrame2.grid_forget()

  signupFrame1.grid(row=1, column=1)
  signupFrame2.grid(row=1, column=2, pady=50)
  
def login_page():
  global loginFrame1, loginFrame2, login_emailEntry, login_passwordEntry

  signupFrame1.grid_forget()
  signupFrame2.grid_forget()


  # Login Frame
  loginFrame1 = CTkFrame(root, width=500, height=300, fg_color="#bfd8af", corner_radius=0,)
  loginFrame1.grid(row=1, column=1, pady=94)

  loginFrame2 = CTkFrame(root, width=600, height=300, fg_color="#d4e7c5", corner_radius=0)
  loginFrame2.grid(row=1, column=2, pady=50)

  loginBottomFrame = CTkFrame(loginFrame2, fg_color="#d4e7c5")
  loginBottomFrame.grid(row=7, column=0, pady=(0,20))


  #Login Images 
  logo = Image.open('C:\\Users\\cadev\\projects\\Final Project (Python)\\HabiTrack\\logo.png')
  logo = logo.resize((780,500))
  logoPhoto = ImageTk.PhotoImage(logo)

  #Login Label
  headingLabel = CTkLabel(loginFrame2, text="Welcome Back!",font=("bookman old style",40,"bold"),text_color="black",bg_color="#d4e7c5")
  headingLabel.grid(row=0, column=0, padx=30, pady=(20,0))

  subheadingLabel = CTkLabel(loginFrame2, text="Log in to access your account.",font=("bookman old style",20),text_color="black",bg_color="#d4e7c5")
  subheadingLabel.grid(row=1, column=0, pady=(0,20))

  #Login Entry
  login_emailEntry = CTkEntry(loginFrame2, placeholder_text="Enter Email",font=("bookman old style", 15),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10, height=40, width=380)
  login_emailEntry.grid(row=2, column=0,padx=10, pady=(0,20))

  login_passwordEntry = CTkEntry(loginFrame2, placeholder_text="Enter Password",font=("bookman old style", 15),text_color="black", fg_color="white", border_color="#bdbdbd",show="*",corner_radius=10, height=40, width=380)
  login_passwordEntry.grid(row=3, column=0, padx=10, pady=(0,20))

  # Login Buttons
  loginButton = CTkButton(loginFrame2, text="Login",font=("bookman old style", 20, "bold"), text_color="white",fg_color="#bfd8af",height=40, width=380, hover_color="#bdbaba", cursor='hand2', command=login_user)
  loginButton.grid(row=6, column=0, pady=(0,20))

  loginhereButton = CTkButton(loginBottomFrame, text="Login Here",font=("bookman old style", 15, "underline"),text_color="blue", fg_color="#d4e7c5", hover_color="#d4e7c5", cursor='hand2', command=signup_page)
  loginhereButton.grid(row=0, column=2)

  # Login Label
  logoLabel = CTkLabel(loginFrame1, image=logoPhoto, text="")
  logoLabel.grid(row=0, column=0, padx=20, pady=20)

  memberLabel = CTkLabel(loginBottomFrame, text="Not a member?",font=("bookman old style",15),text_color="black",bg_color="#d4e7c5")
  memberLabel.grid(row=0, column=1)

  

# Frames 
signupFrame1 = CTkFrame(root, width=700, height=300, fg_color="#bfd8af", corner_radius=0)
signupFrame1.grid(row=1, column=1)

signupFrame2 = CTkFrame(root, width=600, height=300, fg_color="#d4e7c5", corner_radius=0)
signupFrame2.grid(row=1, column=2, pady=50)

signupBottomFrame = CTkFrame(signupFrame2, fg_color="#d4e7c5")
signupBottomFrame.grid(row=7, column=0, pady=(0,20))

# Images
logo = Image.open('C:\\Users\\cadev\\projects\\Final Project (Python)\\HabiTrack\\logo.png')
logo = logo.resize((780,500))
logoPhoto = ImageTk.PhotoImage(logo)


# Label
headingLabel = CTkLabel(signupFrame2, text="Join us today!",font=("bookman old style",40,"bold"),text_color="black",bg_color="#d4e7c5")
headingLabel.grid(row=0, column=0, padx=30, pady=(20,0))

subheadingLabel = CTkLabel(signupFrame2, text="Sign up now to become a member.",font=("bookman old style",20),text_color="black",bg_color="#d4e7c5")
subheadingLabel.grid(row=1, column=0, pady=(0,20))

memberLabel = CTkLabel(signupBottomFrame, text="Already a member?",font=("bookman old style",15),text_color="black",bg_color="#d4e7c5")
memberLabel.grid(row=0, column=0)

logoLabel = CTkLabel(signupFrame1, image=logoPhoto, text="")
logoLabel.grid(row=0, column=0, padx=20, pady=20)

#Entry
nameEntry = CTkEntry(signupFrame2, placeholder_text="Enter Name",font=("bookman old style", 15),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10, height=40, width=380)
nameEntry.grid(row=2, column=0,padx=10, pady=(0,20))

emailEntry = CTkEntry(signupFrame2, placeholder_text="Enter Email",font=("bookman old style", 15),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10, height=40, width=380)
emailEntry.grid(row=3, column=0, padx=10, pady=(0,20))

password1Entry = CTkEntry(signupFrame2, placeholder_text="Choose A Password",font=("bookman old style", 15),text_color="black", fg_color="white", border_color="#bdbdbd", show="*",corner_radius=10, height=40, width=380)
password1Entry.grid(row=4, column=0, padx=10, pady=(0,20))

password2Entry = CTkEntry(signupFrame2, placeholder_text="Re-Enter Password",font=("bookman old style", 15),text_color="black", fg_color="white", border_color="#bdbdbd",show="*",corner_radius=10, height=40, width=380)
password2Entry.grid(row=5, column=0, padx=10, pady=(0,20))


#Button
signupButton = CTkButton(signupFrame2, text="Signup",font=("bookman old style", 20, "bold"), text_color="white",fg_color="#bfd8af",height=40, width=380, hover_color="#bdbaba", cursor='hand2', command=signup_user)
signupButton.grid(row=6, column=0, pady=(0,20))

loginhereButton = CTkButton(signupBottomFrame, text="Login Here",font=("bookman old style", 15, "underline"),text_color="blue", fg_color="#d4e7c5", hover_color="#d4e7c5", cursor='hand2', command=login_page)
loginhereButton.grid(row=0, column=1)


# Root Page
root.title("Login")
root.geometry("1000x600+230+70")
root.config(bg="#bfd8af")
root.resizable(0,0)


root.mainloop()