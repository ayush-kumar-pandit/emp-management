from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import DB

def del_all():
    res=messagebox.askyesno('Confirm','Do you want to delete all the records?')
    if res:
        DB.Del_All()
    treeview_data()

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    salaryEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')

def selection(event):
    sel_Item=tree.selection()
    if sel_Item:
        clear()
        r=tree.item(sel_Item)['values']
        idEntry.insert(0,r[0])
        nameEntry.insert(0,r[1])
        phoneEntry.insert(0,r[2])
        roleBox.set(r[3])
        genderBox.set(r[4])
        salaryEntry.insert(0,r[5])

def update_emp():
    sel_item=tree.selection()
    if not sel_item:
        messagebox.showerror('Error','Select data to update')
    else:
        DB.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Seccess','Data is updated')

def del_emp():
    sel_item=tree.selection()
    if not sel_item:
        messagebox.showerror('Error','Select employee to delete')
    else:
        DB.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Employee is deleted')

def search_emp():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please select an option')
    else:
        search_data=DB.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for e in search_data:
            tree.insert('',END,values=e)

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')


def treeview_data():
    emp=DB.fetch_employees()
    tree.delete(*tree.get_children())
    for e in emp:
        tree.insert('',END,values=e)

def add_employee():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='': 
        messagebox.showerror('Error','All fields are required')
    elif DB.id_exists(idEntry.get()):
        messagebox.showerror('Error','ID already exists!')
    elif not idEntry.get().startswith('AGI'):
        messagebox.showerror('Error',"Invalid ID format. Use 'AGI' followed by a number (e.g., 'AGI1').")
        
    else:
        DB.insert(idEntry.get(), phoneEntry.get(), nameEntry.get(),salaryEntry.get(),roleBox.get(),genderBox.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is added')




win=CTk()
win.geometry('1050x580')
win.resizable(0,0)
win.title('Employee Management System')
win.configure(fg_color="#17182c")

logo=CTkImage(Image.open('bg.jpg'),size=(1050,160))
logoLabel=CTkLabel(win,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(win,fg_color="#17182c")
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='ID',font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')

role_options=['Web Developer','Cloud Engineer','Technical  Writer','Data Scientist','Data Analytic','DBA','Tester','IT Consultant','UI/UX Designer','Dev Ops Engineer']
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'),text_color='white')
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_options=['Male','Female']
genderBox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly')
genderBox.grid(row=4,column=1,padx=20,pady=15,sticky='w')
genderBox.set('Male')

salaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'),text_color='white')
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(win)
rightFrame.grid(row=1,column=1)

search_options=['ID','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame,font=('arial',15,'bold'))
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_emp)
searchButton.grid(row=0,column=2)

ShowAllButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
ShowAllButton.grid(row=0,column=3)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('ID','Name','Phone','Role','Gender','Salary')

tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('ID',width=100)
tree.column('Name',width=160)
tree.column('Phone',width=160)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=140)

style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',18,'bold'))

style.configure('Treeview',font=('arial',15,'bold'),rowheight=30,background='#17182c',foreground='white')


scrollbar=ttk.Scrollbar(rightFrame,orient='vertical',command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(win,fg_color='#17182c')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=7)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newButton.grid(row=0,column=1,padx=5,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=2,padx=5,pady=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_emp)
updateButton.grid(row=0,column=3,padx=5,pady=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=del_emp)
deleteButton.grid(row=0,column=4,padx=5,pady=5)

DeleteAllButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=del_all)
DeleteAllButton.grid(row=0,column=5,padx=5,pady=5)



treeview_data()


win.bind('<ButtonRelease>',selection)
win.mainloop() 