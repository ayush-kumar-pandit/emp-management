import pymysql
from tkinter import messagebox

def connect_Database():
    global mycursor
    global con
    try:
        con=pymysql.connect(host='localhost',user='root',password='2230')
        mycursor=con.cursor()
    except:
        messagebox.showerror('Error','Something went wrong, Please open mysql app before running again')

    mycursor.execute('CREATE Database IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(20),Name VARCHAR(50),Phone VARCHAR(15),Role VARCHAR(50),Gender VARCHAR(20),Salary DECIMAL(10,2))')


def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute('SELECT * from data')
    result=mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gen,new_sal):
    mycursor.execute('UPDATE data SET name=%s, phone=%s, role=%s, gender=%s, salary=%s  WHERE id=%s',(new_name,new_phone,new_role,new_gen,new_sal,id))
    con.commit()


def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    con.commit()

def insert(id,phone,name,sal,role,gen):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gen,sal))
    con.commit()

def search(option,value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result

def Del_All():
    mycursor.execute('TRUNCATE TABLE data')
    con.commit()
connect_Database()