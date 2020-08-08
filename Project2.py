import os
from tkinter import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def register():
    global re_screen
    re_screen=Toplevel(main_screen)
    re_screen.title("Register")
    re_screen.geometry("300x300")
    global username
    global password
    global u_entry
    global p_entry
    username=StringVar()
    password=StringVar()
    Label(re_screen,text="Please enter your details below",bg="black",fg="white").pack()
    Label(re_screen,text="").pack()
    u_label=Label(re_screen,text="Username")
    u_label.pack()
    u_entry=Entry(re_screen,textvariable=username)
    u_entry.pack()
    p_label=Label(re_screen,text="Password")
    p_label.pack()
    p_entry=Entry(re_screen,textvariable=password)
    p_entry.pack()
    Label(re_screen,text="").pack()
    Button(re_screen,text="Register",width=10,height=1,command=reg_user).pack()
# define login function
def login():
    
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

def reg_user():
    us_info=username.get()
    pass_info=password.get()
    file1=open('username.txt',"a")
    file1.write(us_info+"\n")
    file2=open('password.txt',"a")
    file2.write(pass_info)
    file1.close()
    file2.close()
    u_entry.delete(0,END)
    p_entry.delete(0,END)
    Label(re_screen,text="Registration Success").pack()
def login_verify():
#get username and password
    global username_login_entry
    global password_login_entry
    username1 = username_login_entry.get()
   
    password1=password_login_entry.get()
   
   

 

  
 
#defining verification's conditions 
    #if username1 in list_of_files:
    file1 = open('username.txt', "r")   # open the file in read mode
    cu=file1.readlines()

    
    for l in range(0,len(cu)):
        if username1==cu[1]:

            
#read the file, 
#as splitlines() actually splits on the newline character,
#the newline character is not left hanging at the end of each line. if password1 in verify:
            file2=open('password.txt',"r")
            verify=file2.readlines()
            
            for i in range(0,len(verify)):
                if verify[i]==password1:
                    Label(text="Login successful", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
                    Label(text="").pack()
                    subject = "An email with attachment from Python"
                    body = "This is an email with attachment sent from Python"
                    sender_email = "my@gmail.com"
                    receiver_email = "your@gmail.com"
                    password = input("Type your password and press enter:")

# Create a multipart message and set headers
                    message = MIMEMultipart()
                    message["From"] = sender_email
                    message["To"] = receiver_email
                    message["Subject"] = subject
                    message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
                    message.attach(MIMEText(body, "plain"))

                    filename = "document.pdf"  # In same directory as script

# Open PDF file in binary mode
                    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
                    encoders.encode_base64(part)

# Add header as key/value pair to attachment part
                    part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                    )

# Add attachment to message and convert message to string
                    message.attach(part)
                    text = message.as_string()

# Log in to server using secure context and send email
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, text)
 
                else:
                    Label(text="wrong password", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
                    Label(text="").pack() 
 
        else:
            Label(text="user not found", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
            Label(text="").pack() 

def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window
    # create a Form label
    Label(text="Choose Login",fg="white",bg="black",width="300",height="2").pack()
    Label(text="").pack()
    # create Login Button 
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register",height="2",width="30",command=register).pack()
# create a Form label 


 
# create a register button
 #Button(text="Register", height="2", width="30").pack()
 

 
main_account_screen() # call the main_account_screen() function
