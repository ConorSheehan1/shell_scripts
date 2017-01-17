import os
def copy_cwd():    
	cwd = os.getcwd()
	command = 'echo ' + cwd + '| clip'
	os.system(command)
			
if __name__ == "__main__":
	copy_cwd()