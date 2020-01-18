Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "winupdate.exe" & Chr(34), 0
Set WshShell = Nothing