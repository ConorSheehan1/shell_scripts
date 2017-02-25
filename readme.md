| File          | Function                                   | Requirements |
|---------------|--------------------------------------------|--------------|
| copy_cwd2.py  | copy current working directory to cliboard | python2      |
| copy_cwd3.py  | copy current working directory to cliboard | python3      |
| copy_cwd.bat  | call appropriate python file               | Windows OS   |


## Arguments   
1. copy_cwd.bat
	* `/` will replace all `\` in the path with `/`  
	* `cd` will add `cd ` to the beginning of the current working directory    
	
	for example `%cwd% \ cd` will change `c:\user\documents` to `cd c:/user/documents`
	![shell example](img/shell.PNG)
	
