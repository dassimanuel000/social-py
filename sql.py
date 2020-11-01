#import mysql.connector
#from mysql.connector import *

#cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='Social',use_pure=False)

#if cnx == True:
    #print('OK')
#cnx.close()*/

import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='social',use_pure=False)

cursor = cnx.cursor()
#tomorrow = datetime.now().date() + timedelta(days=1)
add_employee = ("INSERT INTO users " "(firstname, lastname, mail, password, mac_address, key_licence, date, created_at, updated_at)" 
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
#add_salary = ("INSERT INTO salaries "
#"(emp_no, salary, from_date, to_date) "
#"VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
data_employee = ('Geert', 'Vanderkelen', 'mail@mail.conm', 'password', 'mac_address', 'key_licence', date(2020, 8, 9), 'created_at', 'updated_at')
# Insert new employee
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

print(emp_no)
# Insert salary information
#data_salary = {
#'emp_no': emp_no,
#'salary': 50000,
#'from_date': tomorrow,
#'to_date': date(9999, 1, 1),
#}
#cursor.execute(add_salary, data_salary)
# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()