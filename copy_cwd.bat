@rem don't print all commands
@echo off

@rem try python 3
python C:\Users\conor\Documents\GitHub\shell_scripts\copy_shell3.py %*

@rem if python3 file fails, call python2 file
IF %ERRORLEVEL% == 0 Exit /b

python C:\Users\conor\Documents\GitHub\shell_scripts\copy_shell2.py %*

