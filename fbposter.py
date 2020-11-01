from Tkinter import * 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def main():

	#your account user and password, path to image, links to groups and message

	def post(): 
		usr = user.get()
		pwd = password.get()
		message = message_.get()
		image_path = image_path_.get()
		group_links = [group_links_]

		#delete cache
		profile = webdriver.FirefoxProfile()
		profile.set_preference("browser.cache.disk.enable", False)
		profile.set_preference("browser.cache.memory.enable", False)
		profile.set_preference("browser.cache.offline.enable", False)
		profile.set_preference("network.http.use-cache", False)

		# Path to geckodriver executable
		driver = webdriver.Firefox()
		driver.implicitly_wait(15)

		#Login to facebook
		driver.get("http://www.facebook.com")
		elem = driver.find_element_by_id("email")
		elem.send_keys(usr)
		elem = driver.find_element_by_id("pass")
		elem.send_keys(pwd)
		c = driver.find_element_by_id('u_0_b')
		c.click()

		for group in group_links:
			# Go to the Facebook Group and
			driver.get(group)
			sleep(5)
			post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

			post_box.send_keys(message)
			sleep(5)

			if image_path != "" :
				addMedia = driver.find_element_by_xpath("//*[@data-testid='media-attachment-selector']")
				addMedia.click()

				# Provide picture file path
				driver.find_element_by_xpath("//*[@name='composer_photo']").send_keys(image_path)

			# Get the 'Post' button and click on it
			Post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
			sleep(5)
			Post_button.click()
			sleep(5)
		driver.close()


	face_master = Tk() 
	face_master.title('FACEBOOK AUTO POST')
	face_master.geometry("450x410") 
	face_label = Label(face_master, text ="Entrez les elements a poster") 
	face_label.pack(pady = 10) 

	userlabel = Label(face_master, text ="Nom d'utilisateur ou telephone sur Faceboox") 
	userlabel.pack(pady = 0,padx = 10) 
	user = Entry(face_master)
	user.pack(pady = 10)
	user.focus_set()

	passwordlabel = Label(face_master, text ="Mot de Passe sur Faceboox") 
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

	group_linkslabel = Label(face_master, text ='Liens des groupes encadrer des ("") a cahque fois') 
	group_linkslabel.pack(pady = 0,padx = 10) 
	group_links_ = Entry(face_master)
	group_links_.pack(pady = 10)

	submit = Button(face_master, text ="POSTER", command = post) 
	submit.pack(pady = 10) 

if __name__ == '__main__':
	
  	main()
