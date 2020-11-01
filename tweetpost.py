from Tkinter import * 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def main_tw():

		#your account user and password, path to image and message


	def post(): 
		usr = user.get()
		pwd = password.get()
		message = message_.get()
		image_path = image_path_.get()

		#delete cache
		profile = webdriver.FirefoxProfile()
		profile.set_preference("browser.cache.disk.enable", False)
		profile.set_preference("browser.cache.memory.enable", False)
		profile.set_preference("browser.cache.offline.enable", False)
		profile.set_preference("network.http.use-cache", False)

		# Path to geckodriver executable
		#driver = webdriver.Firefox(executable_path=r'D:\Desktop\selenium\geckodriver')
		driver = webdriver.Firefox()
		driver.get("https://twitter.com")
		#driver.implicitly_wait(15)

		# Login to twitter
		#driver.get("https://twitter.com")
		sleep(3)
		elem = driver.find_element_by_name("session[username_or_email]")
		elem.send_keys(usr)
		elem = driver.find_element_by_name("session[password]")
		elem.send_keys(pwd)
		c = driver.find_element_by_class_name("EdgeButton")
		c.click()
		sleep(3)
		# Enter the text we want to post to twitter and the image 
		mess = driver.find_element_by_id("tweet-box-home-timeline")
		mess.send_keys(message)
		sleep(5)
		ima = driver.find_element_by_name("media_empty")
		sleep(3)
		ima.send_keys(image_path)
		# Get the 'Post' button and click on it
		Post_button = driver.find_element_by_class_name("tweet-action")
		sleep(3)
		Post_button.click()
		sleep(3)
		driver.close()



	face_master = Tk() 
	face_master.title('TWITTER AUTO POST')
	face_master.geometry("450x410") 
	face_label = Label(face_master, text ="Entrez les elements a poster") 
	face_label.pack(pady = 10) 

	userlabel = Label(face_master, text ="Nom d'utilisateur ou telephone sur TWITTER") 
	userlabel.pack(pady = 0,padx = 10) 
	user = Entry(face_master)
	user.pack(pady = 10)
	user.focus_set()

	passwordlabel = Label(face_master, text ="Mot de Passe sur TWITTER") 
	passwordlabel.pack(pady = 0,padx = 10) 
	password = Entry(face_master)
	password.pack(pady = 10)

	message_label = Label(face_master, text ="Message du Posst") 
	message_label.pack(pady = 0,padx = 10) 
	message_ = Entry(face_master)
	message_.pack(pady = 10)

	image_path_label = Label(face_master, text ="Lien de l'image a joindre") 
	image_path_label.pack(pady = 0,padx = 10) 
	image_path_ = Entry(face_master)
	image_path_.pack(pady = 10)

	submit = Button(face_master, text ="POSTER", command = post) 
	submit.pack(pady = 10) 


if __name__ == '__main__':
  main_tw()