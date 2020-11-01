from Tkinter import * 
#from Tkinter import tkMessageBox
import tkinter
import tkinter.messagebox
from tkinter.ttk import *
from registerWindow import registerWindow
from fbposter import main
from tweetpost import main_tw
from ig_post import main_ig
from selenium import webdriver 
import mysql.connector
from datetime import date, datetime, timedelta
  
i = 0
master = Tk() 
master.title('Social Login')
master.geometry("450x410") 
tof = PhotoImage(file = "logo-design.png")
w = Label(master, image=tof)
w.pack()
master.configure(background = 'White')

messagebox.askquestion("OK","NO", icon="warning")
  
label = Label(master, text ="Social Home") 
label.pack(pady = 10) 

def get():
    print mail.get()
    print password.get()
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='social',use_pure=False)
    cursor = cnx.cursor()
    add_employee = ("update users set date_now =+1 where email = %s")
    data = (mail.get())
    cursor.execute(add_employee, data)
    emp_no = cursor.lastrowid

    print(emp_no)
    cnx.commit()
    cursor.close()
    cnx.close()
    
    messagebox.askquestion("OK","NO", icon="warning")
    #root.after(60000, openNewWindow, args)

maillabel = Label(master, text ="E-mail Adress") 
maillabel.pack(pady = 0,padx = 10) 
mail = Entry(master)
mail.pack(pady = 10)
mail.focus_set()

passwordlabel = Label(master, text ="Password") 
passwordlabel.pack(pady = 0) 
password = Entry(master)
password.pack(pady = 10)

text_if = "Register"

def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Social DASHBOARD") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("800x800") 
  
    # A Label widget to show in toplevel 
    Label(newWindow, text ="Social DASHBOARD").pack() 

    fb_btn = Button(newWindow, text ="Facebook post", command = main) 
    fb_btn.pack(pady = 10) 

    tw_btn = Button(newWindow, text ="Twitter post", command = main_tw) 
    tw_btn.pack(pady = 10) 

    ig_btn = Button(newWindow, text ="Instagramm post", command = main_ig) 
    ig_btn.pack(pady = 10) 
    

btn = Button(master, text ="Login", command = get) 
btn.pack(pady = 10) 


register = Button(master, text =text_if, command = registerWindow) 
register.pack(pady = 10) 

blabla = Button(master, text ="blabla", command = openNewWindow) 
blabla.pack(pady = 10) 

# mainloop, runs infinitely 
mainloop() 