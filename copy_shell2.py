import os
from Tkinter import Tk

def copy_cwd():    
	cwd = os.getcwd()
	
	r = Tk()
	# hide tk window
	r.withdraw()
	
	# clear clipboard and add cwd to it
	r.clipboard_clear()
	r.clipboard_append(cwd)
	r.destroy()
			
if __name__ == "__main__":
	copy_cwd()