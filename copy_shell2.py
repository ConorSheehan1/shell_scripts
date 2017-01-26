import os
import sys
from Tkinter import Tk

def copy_cwd():    
	cwd = os.getcwd()
	
	# cmd arguements to change \ to / and add cd to start of sting 
	if "/" in sys.argv:
		cwd = cwd.replace("\\", "/")
		
	if "cd" in sys.argv:
		cwd = "cd " + cwd
	
	r = Tk()
	# hide tk window
	r.withdraw()
	
	# clear clipboard and add cwd to it
	r.clipboard_clear()
	r.clipboard_append(cwd)
	r.destroy()
			
if __name__ == "__main__":
	copy_cwd()