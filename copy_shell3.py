import os
import sys

def copy_cwd():    
	cwd = os.getcwd()
	
	# cmd arguements to change \ to / and add cd to start of sting 
	if "/" in sys.argv:
		cwd = cwd.replace("\\", "/")
		
	if "cd" in sys.argv:
		cwd = "cd " + cwd
			
	command = 'echo ' + cwd + '| clip'
	os.system(command)
			
if __name__ == "__main__":
	copy_cwd()