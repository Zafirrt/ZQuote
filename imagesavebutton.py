

from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox

class NoFileError(Exception):
	'''
	Custom error jika tidak ada file yang disiapkan
	'''
	pass

class SaveButton(Button):
	
	def __init__(self, root, main_font=None, file=None):
		super().__init__(root, font=main_font)
		super().config(text="Save", command=self.save_file)
		self.file = file

	def config(self, file):
		self.file = file

	def save_file(self, file=None):
		if not file == None:
			self.file = file

		try:
			if(self.file == None):
				raise NoFileError

			# Jika dapat dilakukan, simpan file
			filename = asksaveasfilename(defaultextension='.JPEG')
			self.file.save(filename, 'JPEG')
			messagebox.showinfo("", "Image saved successfully")

		# Bukan foto
		except AttributeError:
			messagebox.showerror("Error!", "Invalid File Type!")

		# Tidak ada file untuk disimpan
		except NoFileError:
			messagebox.showerror("Error!", "No Image Loaded!")

		# General Error
		except:
			messagebox.showerror("Error!", "Error!")