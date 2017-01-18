| File         | Function                                   | Requirements |
|--------------|--------------------------------------------|--------------|
| copy_cwd2.py | copy current working directory to cliboard | python2      |
| copy_cwd3.py | copy current working directory to cliboard | python3      |
| copy_cwd.bat | call appropriate python file               | Windows OS   |


[http://www.tablesgenerator.com/markdown_tables](http://www.tablesgenerator.com/markdown_tables)

## Why use this at all
If you use `echo pwd |clip` you can copy the current working directory to the clipboard in windows, so what's the point of this anyway?  

If you have cygwin installed, you get `/cygdrive/` before the file path, so I decided to write a python script to copy the working directory from the console to the clipboard, without the prefix.

[This stack exchange post](http://unix.stackexchange.com/questions/44677/how-do-i-get-rid-of-cygwins-cygdrive-prefix-in-all-paths/44680#44680?newreg=5bf3947c5aaa46d5b08916062b6196c6) also explains how to remove the cygwin prefix by modifying `/etc/fstab` but that still leaves a `/` prefix, which means you can't use `cd ctrl+v` because you'll be using a relative path, not an absolute one. 

So basically, I couldn't fix this problem properly, so here's my python/batch work around.