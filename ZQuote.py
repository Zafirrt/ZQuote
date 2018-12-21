

from tkinter import *
from tkinter import font
import imagesavebutton
import requests
from PIL import ImageTk, Image
from io import BytesIO
import random
import time

class ZQuote(Frame):
	'''
	Class yang digunakan untuk menampilkan quote random dari internet
	'''

	def __init__(self, root):
		super().__init__(root)

		# Root config
		self.master = root
		root.title("ZQuote, save your favorite quotes!")
		root.config(bg='white')
		root.resizable(0, 0)

		# Font utama untuk widget
		self.main_font = font.Font(family='Helvetica', weight='bold')


		def next_quote(event=None):
			'''
			Fungsi untuk mengambil quote dari internet dan menampilkannya
			'''

			# Selama mengunduh quote tidak boleh menekan next button
			# Dan beri waktu membaca sebesar 2 detik
			self.Button_next.config(command='')
			self.img = self.get_quote()
			time.sleep(2)

			# Save siap jika ingin save file
			self.Button_save.config(file=self.img)
	
			# Membuat ukuran menjadi cocok dengan gui
			# Dan membuat menjadi foto berwarna RGB
			self.img = self.img.resize((600,600))
			self.img = ImageTk.PhotoImage(self.img.convert('RGB'))
	
			# Menampilkan quote
			self.Image_place.config(image=self.img, anchor='center', height=615)
			self.Image_place.update()

			# Next button sekarang berguna
			self.Button_next.config(command=next_quote)

		# Database Fakta random
		self.facts = open(".facts.txt", 'r').readlines()

		# Widget
		self.Image_place = Label(self.master, height=36, bg='white', text="Welcome to ZQuote!\nClick 'Next' to begin.")
		self.Button_save = imagesavebutton.SaveButton(self.master, self.main_font)
		self.Button_next = Button(self.master, text='Next', font=self.main_font, command=next_quote)

		# Menempatkan widget
		self.Image_place.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W+E)
		self.Button_save.grid(row=1, column=0, ipadx=150)
		self.Button_next.grid(row=1, column=1, ipadx=150)
		self.Image_place.pack_propagate(0)

		root.mainloop()

	def get_quote(self):
		'''
		Fungsi untuk mengambil quote random dari internet
		dan mengembalikannya sebagai PIL.Image type
		'''

		def get_quote_url(url):
			'''
			Fungsi untuk mengembalikan link foto yang ingin ditampilkan
			'''
			r = requests.get(url)	
			lst = r.text.split('\n')
			return requests.get(lst[32][40:-3])

		# Menampilkan fakta random untuk sementara waktu
		random_fact = random.randint(0, 275)
		random_fact = "Random Fact #{}:\n{}".format(random_fact+1, self.facts[random_fact])
		self.Image_place.config(image='', text=random_fact,  wraplength=570, height=36)
		self.Image_place.update()

		# Url yang digunakan
		url = 'https://www.quoteload.com/quotes/random'
		image_url = get_quote_url(url)

		# PIL.Image type
		img = Image.open(BytesIO(image_url.content))
		return img


if __name__ == '__main__':
	root = Tk()
	main_program = ZQuote(root)