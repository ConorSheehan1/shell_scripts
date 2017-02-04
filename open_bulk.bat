@rem @echo off@rem if no params are passed, open c files
IF "%1" == "" GOTO open_c

FOR /r %%i IN (%*) DO notepad++ %%i
Exit /b
	
:open_cecho "hi"
FOR /r %%i IN (*.C) DO notepad++ %%i