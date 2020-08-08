import tkinter as tk
from tkinter import messagebox
from tkinter import *
import smtplib

def signup():
     global nameE
     global dobE
     global roots
     global emailE
     global userE
     global entryP
     global entryCP

     roots=tk.Tk()
     roots.title('Signup')
     roots.geometry('500x580')

     label=Label(roots,text='Name:',font=('arial', 15, 'bold'))
     label.place(x=7,y=10)
     nameE=Entry(roots,relief='solid',bg="white",fg="black")
     nameE.place(x=7,y=50)

     gender=tk.Label(roots, text='Gender:',font=('arial', 15, 'bold'))
     gender.place(x=7,y=90)
     rb1=tk.IntVar()
     rb2=tk.IntVar()
     radio1=tk.Radiobutton(roots, text='Male',font=('arial', 15), value=0)
     radio2=tk.Radiobutton(roots, text='Female',font=('arial', 15),value=1)
     radio1.place(x=100, y=90)
     radio2.place(x=180, y=90)

     label=Label(roots,text='Date Of Birth(DD/MM/YYYY):',font=('arial', 15, 'bold'))
     label.place(x=7,y=140)
     dobE=Entry(roots,relief='solid',bg="white",fg="black")
     dobE.place(x=7,y=180)

     label=Label(roots,text='Email:',font=('arial', 15, 'bold'))
     label.place(x=7,y=220)
     emailE=Entry(roots,relief='solid',bg="white",fg="black")
     emailE.place(x=7,y=260)

     label=Label(roots,text='Username:',font=('arial', 15, 'bold'))
     label.place(x=7,y=300)
     userE=Entry(roots,relief='solid',bg="white",fg="black")
     userE.place(x=7,y=340)

     label=Label(roots,text='Password:',font=('arial', 15, 'bold'))
     label.place(x=7,y=380)
     entryP=Entry(roots,relief='solid',bg="white",fg="black", show='*')
     entryP.place(x=7,y=420)

     button=Button(roots,text='Signup', font=('calbri', 20), command=signup_success)
     button.place(x=380,y=495)
     roots.mainloop()
     
def signup_success():
     global root
     root=tk.Tk()
     root.geometry('400x100')
     root.title('Signup Success')
     label=Label(root,text='Signup Successful, Now you can Login', font=('arial', 14, 'bold'))
     label.place(x=7,y=7)
     button=Button(root,text='OK', font=('calbri', 13), command=data_store)
     button.place(x=320,y=50)
     root.mainloop()
     
def data_store():
     f=open('P1DB.txt', "w")
     f.write(nameE.get())
     f.write('\n')
     f.write(dobE.get())
     f.write('\n')
     f.write(emailE.get())
     f.write('\n')
     f.write(userE.get())
     f.write('\n')
     f.write(entryP.get())
     f.close()
     roots.destroy()
     root.destroy()

def login():
     global win_2
     global uE
     global PE
     
     win_2=tk.Tk()
     win_2.title('Login')
     win_2.geometry('300x200')

     label=Label(win_2,text='Username:',font=('arial', 15, 'bold'))
     label.place(x=7,y=7)
     uE=Entry(win_2,relief='solid',bg="white",fg="black")
     uE.place(x=7,y=40)

     label=Label(win_2,text='Password:',font=('arial', 15, 'bold'))
     label.place(x=7,y=70)
     PE=Entry(win_2,relief='solid',bg="white",fg="black", show='*')
     PE.place(x=7,y=103)

     button=Button(win_2,text='Login', font=('calbri', 15), command=check_login)
     button.place(x=220,y=140)
     win_2.mainloop()

def check_login():
     f=open('P1DB.txt', "r")
     data=f.readlines()
     uname = data[3].rstrip() 
     pword = data[4].rstrip()
     if uE.get()==uname and PE.get()==pword:
          win_2.destroy()
          messenger()
     else:
        r =tk.Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()



def messenger():

     global send_email
     global send_pass
     global recv_email
     global sub_var
     global msg_body

     send_email=StringVar()
     send_pass=StringVar()
     recv_email=StringVar()
     sub_var=StringVar()
     msg_body=None

     f=open('P1DB.txt', "r")
     data=f.readlines()
     eid=data[2].rstrip()
     
    
     
     win_3=tk.Tk()
     win_3.geometry('500x500')
     win_3.title('Messenger')

     wel=Label(win_3, text='Welcome')
     wel.place(x=7,y=7)
     sender_name=Label(win_3, text=(data[0]))
     sender_name.place(x=65, y=7)

     sender_email=Label(win_3,text="Sender's Gmail ID: ")
     sender_email.place(x=7, y=30)

     sender_entry=Entry(win_3, text=send_email,bd=3)
     sender_entry.place(x=107, y=30)

     sender_pass=Label(win_3,text="Gmail Password: ")
     sender_pass.place(x=7, y=53)

     pass_Entry=Entry(win_3,show='*',textvariable=send_pass,bd=3)
     pass_Entry.place(x=107, y=53)

     receiver_email=Label(win_3,text="Receiver's Email: ")
     receiver_email.place(x=7, y=76)

     receiver_entry=Entry(win_3,textvariable=recv_email, bd=3)
     receiver_entry.place(x=107, y=76)

     subject=Label(win_3, text='Subject')
     subject.place(x=7, y=110)

     sub_entry=Entry(win_3, relief='solid', textvariable=sub_var, width= 50)
     sub_entry.place(x=107, y=110)

     msg_label=Label(win_3,text='Message')
     msg_label.place(x=7, y=160)
     
     
     msg_body=Text(win_3,height=15,width=40,bd=3)
     msg_body.place(x=107, y=180)

     send_button=Button(win_3, text='Send', command=mail)
     send_button.place(x=440, y=450)

     attach_button=Button(win_3, text='Attach')
     attach_button.place(x=7, y=450)

     win_3.mainloop()

def mail_info():
     tk.messagebox.showinfo("Confirmation", "Email Sent")

def mail():
    try:
        if send_email.get()=="" or send_pass.get()=="" or recv_email.get()=="":
            messagebox.showerror("Error","Please enter the complete details.")
        else:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            a=send_email.get()
            b=send_pass.get()
            c=msg_body.get('1.0',END)
            d=recv_email.get()
            server.login(a,b)
            server.sendmail(a,d,c)
            server.close()
            mail_info()
    except Exception as e:
        print(e)
        a=messagebox.askokcancel("Error","Read instructions")
     
        
win_1=Tk()
win_1.title('Login/Signup Panel')
win_1.geometry('350x400')
label=Label(win_1,text='Login or Signup ?', font=('arial', 14, 'bold'))
label.place(x=100,y=50)
button=Button(win_1,text='Signup', font=('calbri', 20, 'bold'), command=signup)
button.place(x=130,y=120)
label=Label(win_1,text='OR', font=('arial', 14, 'bold'))
label.place(x=170,y=210)
button=Button(win_1,text='Login', font=('calbri', 20, 'bold'), command=login)
button.place(x=140,y=270)




