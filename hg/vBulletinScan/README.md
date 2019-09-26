# Mass-Pwn-vBulletin
Identify vulnerable (RCE) vBulletin 5.0.0 - 5.5.4 instances using Shodan (CVE-2019-16759)

![Bulletin](https://raw.githubusercontent.com/Frint0/mass-pwn-vbulletin/master/vbulletin.png)

![Demo](https://raw.githubusercontent.com/Frint0/mass-pwn-vbulletin/master/demo-cli.png)

## Gathering Hosts:

This tool simply iterates over hosts on port 443 and 80 and runs a PoC to test if they are vulnerable to RCE. You can use Shodan to gather potential targets:

```
shodan download vbullet-443 'html:"vbulletin" port:443'
shodan parse vbullet-443.json.gz --fields ip_str > vbullet-443
shodan download vbullet-80 'html:"vbulletin" port:80'
shodan parse vbullet-80.json.gz --fields ip_str > vbullet-80
```

*By default I provide both host files with 1k hosts each for those of you without a Shodan API key! 😄*


## Special Thanks:

Thanks to the anonymous user who published this 0day over at https://seclists.org/fulldisclosure/2019/Sep/31

## Disclaimer:

I am not responsible for what you do with this tool, this is simply for research purposes.
