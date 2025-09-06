from  customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or PassEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be Empty')
    elif usernameEntry.get()=='Ayush' and PassEntry.get()=='2230':
        messagebox.showinfo('Success','Login successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid Credentials')



root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')

img=CTkImage(Image.open('Login.png'),size=(930,478))
imageLabel=CTkLabel(root,image=img,text='')
imageLabel.place(x=0,y=0)

headinglabel=CTkLabel(root,text='Employee Management System',bg_color='white',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headinglabel.place(x=20,y=50)

usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=50,y=100)

PassEntry=CTkEntry(root,placeholder_text='Enter Password',width=180,show='*')
PassEntry.place(x=50,y=150)

loginbutton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginbutton.place(x=70,y=200)


root.mainloop()