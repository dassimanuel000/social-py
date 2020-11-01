from instabot import Bot 
#import instabot as bot
#from instabot-py import Bot 

def main_ig():

	def post(): 

        bot = Bot() 
        bot.login(username = username.get(),  password = password.get()) 
        bot.upload_photo(image_path_.get(), caption =message_.get()) 


	ig_master = Tk() 
	ig_master.title('INSTAGRAM AUTO POST')
	ig_master.geometry("450x410") 
	ig_label = Label(ig_master, text ="Entrez les elements a poster") 
	ig_label.pack(pady = 10) 

	username_label = Label(ig_master, text ="Nom d'utilisateur ou telephone sur INSTAGRAM") 
	username_label.pack(pady = 0,padx = 10) 
	username = Entry(ig_master)
	username.pack(pady = 10)
	username.focus_set()

	passwordlabel = Label(ig_master, text ="Mot de Passe sur INSTAGRAM") 
	passwordlabel.pack(pady = 0,padx = 10) 
	password = Entry(ig_master)
	password.pack(pady = 10)

	message_label = Label(ig_master, text ="Message du Posst") 
	message_label.pack(pady = 0,padx = 10) 
	message_ = Entry(ig_master)
	message_.pack(pady = 10)

	image_path_label = Label(ig_master, text ="Lien de l'image a joindre") 
	image_path_label.pack(pady = 0,padx = 10) 
	image_path_ = Entry(ig_master)
	image_path_.pack(pady = 10)

	submit = Button(ig_master, text ="POSTER", command = post) 
	submit.pack(pady = 10) 


if __name__ == '__main__':
  main_ig()