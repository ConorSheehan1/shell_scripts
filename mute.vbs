REM http://stackoverflow.com/questions/2216334/how-to-control-windows-system-volume-using-jscript-or-vbscript
REM &hAD toggles mute and unmute, so use loop to decrease volume until muted instead
Set WshShell = CreateObject("WScript.Shell")
For counter = 0 To 50
	WshShell.SendKeys(chr(&hAE))
Next