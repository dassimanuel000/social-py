from Tkinter import * 
import mysql.connector
from getmac import *
from getmac import get_mac_address as gma
from datetime import date, datetime, timedelta
from selenium import webdriver 

def registerWindow():

    newWindow2 = Toplevel()
    newWindow2.title("Social Register") 
  
    # sets the geometry of toplevel 
    newWindow2.geometry("500x400") 
    newWindow2.configure(background = 'White')
  
    # A Label widget to show in toplevel 
    Label(newWindow2, text ="Enregistrer vous ici",).pack(pady = 3) 


    def func_register():
        print register_name.get()
        print register_mail.get()
        print register_password.get()
        print register_tel.get()
        print(gma())

        cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='social',use_pure=False)
        cursor = cnx.cursor()
        add_employee = ("INSERT INTO users " "(name, email, password, mac_address, tel, usertype, key_licence, date_start, date_now, created_at, updated_at)" 
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_employee = (register_name.get(), register_mail.get(), register_password.get(), gma(), register_tel.get(), 'client', '0', date(2020, 8, 9), '1', datetime.now().date(), datetime.now().date())
        
        cursor.execute(add_employee, data_employee)
        emp_no = cursor.lastrowid

        print(emp_no)
        cnx.commit()
        cursor.close()
        cnx.close()
        newWindow2.destroy()

        driver = webdriver.Firefox() 
        driver.get("http://localhost:8000/add_licence") 


    register_namelabel = Label(newWindow2, text ="User name") 
    register_namelabel.pack(pady = 0) 
    register_name = Entry(newWindow2)
    register_name.pack(pady = 10)
    register_name.focus_set()

    maillabel2 = Label(newWindow2, text ="E-mail Adress") 
    maillabel2.pack(pady = 0,padx = 10) 
    register_mail = Entry(newWindow2)
    register_mail.pack(pady = 10)

    register_passwordlabel = Label(newWindow2, text ="Password") 
    register_passwordlabel.pack(pady = 0) 
    register_password = Entry(newWindow2)
    register_password.pack(pady = 10)

    register_tellabel = Label(newWindow2, text ="Telephone") 
    register_tellabel.pack(pady = 0) 
    register_tel = Entry(newWindow2)
    register_tel.pack(pady = 10)

    btn_register = Button(newWindow2, text ="DEMANDER UNE LICENCE", command = func_register) 
    btn_register.pack(pady = 10)

registerWindow