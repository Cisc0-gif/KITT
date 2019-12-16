### v0.5 6/25/19 
* development started 
* added Metasploit,device_rootkits,rootkits,hashcat,hydra,burpsuite,joomlascan,theHarvester,Winupdate,kidlogger,duck2spark,duckencoder, & homebrew scripts
* added options 8-12 with functioning libraries and a basic package installer
* added option info and re-did UI with a clock, FOCA and OSINT websites feature
* added VMware images, phishing tool sonar.py, README and LOG options, and added LOG.txt
* added append_num.py to hashcat dir

### v0.5 6/26/19 
* added decoders.txt in crackers
* added recon-ng, google dorks, and osint sites to hg

### v0.5 6/27/19 
* migrated from repl.it to KALI-NAS
* localized source code, homebrews, and directories
* added all available scripts and programs to source code
* added win10,win8,win7,kali, and ubuntu 18 images for vmware

### v0.5 6/28/19
* added crunch and cewl to hg
* added packetcapture.sh and domain_sticate.sh

### v0.5 7/1/19
* added IRC client to menu
* added postgresql start before msfconsole start
* improved hydra command format in weblogin_cracker.sh

### v0.5 7/2/19
* added telnet to lib_install.sh
* added sdefense directory with macchanger.sh and ssh_randomizer.sh

### v0.7 7/3/19
* added ftp to lib_install.sh
* added port listener to menu
* added shellter to lib_install.sh and menu
* added RSA key generator to rdefense

### v0.7 7/5/19
* added fbi-master to hg

### v0.7 7/7/19
* added R0T_decrypter to crackers

### v0.7 7/8/19
* debugged R0T_decrypter

### v0.7 7/10/19
* added colorama to menu and lib_install.py
* changed menu to red

### v0.7 7/11/19
* added AutoSploit to hg
* added proxy_config.sh to sdefense
* added OWASP and AutoSploit installers to lib_install's

### v0.7 7/15/19
* added custom inputs for proxy_config.sh

### v0.7 7/17/19
* added radare2, gdb, strace, and xdd forensics tools to lib_install.sh
* added forensics tools to menu
* changed log viewer from print to more
* added exiftool and steghide to forensics
* added exiftool and steghide to lib_install.sh

### v1.0 7/17/19
* changed name from KodHak7 to KITT1.0
* changed version number from 0.7 to 1.0

### v1.0 7/19/19
* added ssh_encr7pt.sh to sdefense and to menu

### v1.0 7/22/19
* added static_ip.sh to sdefense and menu
* added figlet to static_ip.sh

### v1.0 8/1/19
* fixed lib_install.py errors
* added proxychains install and config to lib_install.sh

### v1.0 8/2/19
* added psutil to lib_install.py
* added bluespoof.sh to menu
* added p7zip to lib_install.sh

### v1.0 8/4/19
* added macchanger to lib_install.sh

### v1.0 8/5/19
* changed format of package install command in lib_install.sh
* added hddtemp,lm-sensors, and python3 to lib_install.sh
* added proxies to proxychains.conf config
* added postgresql to lib_install.sh and command to start main cluster
* reverted format of package install command to original
* added pip installations to python2 and python3 in lib_install.sh

### v1.0 8/6/19
* added btscanner and spooftooph to lib_install.sh
* added PATH exec file and renamed python source from KITT_1.py to KITT.py
* added Cisco_E4200_vuln.py to exploits 
* added Cisco_E4200_vuln.py to exploits menu
* created KITT_INSTALLER.sh to write KITT to PATH
* compiled lib_install.py into lib_install.sh
* removed lib_install.py
* changed OWASP-ZSC from installation execution to python execution
* added apache2 and git to lib_install.sh
* removed AutoSploit installation and simplified for kali linux installation
* added msf database initialization and postgres cluster booting
* added content to README.txt and added LICENSE.txt using the MIT License
* debugged PATH execution in source

### v1.0 8/7/19
* initialized KITT as git repo
* formatted LOG.txt as CHANGELOG.md
* push all files to origin master
* commits 0-9 were added

### v1.0 8/9/19
* removed git signatures from OWASP-ZSC, 7zipcrack, hashcat, theHarvester
* add shodan pip install to lib_install.sh
* reinitialized repo to fix git signatures
* added shodan_search.py to menu
* fixed option list error

### v1.0 8/10/19
* revamped entire KITT.py UI
* added unmade hashcat
* removed some useless features
* added autoremove to init of KITT.py and closing statement of lib_install.sh
* reformatted dorks.txt and decoders.txt to markdown and removed osint_sites.txt
* debugged recursion() errors
* removed accidental hydra.restore file
* fixed syntax error in KITT_INSTALLER.sh
* renamed sketch.ino to filename.ino in convert.sh
* added goog-mail.py to hg

### v1.0 8/11/19
* debugged success message in file copy
* added success and failure events to os check
* reformatted domain_sticate.sh to python and added lib_install.sh check and shodan search to domain scan
* added domain_sticate.py to menu

### v1.0 8/12/19
* swapped tor command for msfvenom shell in KITT.py
* added os detection message
* began implementation of runtime log in RUNTIME.log

### v1.0 8/13/19
* added upgrade message and continued implementation of runtime log
* added irc.rb psnuffle module config to lib_install.sh
* added runtime messages to lib_install.sh

### v1.0 8/14/19
* added SMB drive mounting tools to lib_install.sh
* added dsniffer to lib_install.sh
* added net-creds.py dependency libraries to lib_install.sh
* added net-creds.py to hg/ and callable to KITT.py
* added distro warning to README.md
* continued implementation of runtime log
* debugged multiple runtime logs occurance
* added rwx perms to RUNTIME.log after being wrote

### v1.0 8/15/19
* continued implementation of runtime log at option 18
* finished implementing runtime log
* debugged small variable errors in source

### v1.0 8/16/19
* added bluelog, redfang, and bluesnarfer to lib_install.sh for bluetooth hacking
* added btverifier.py to menu and source

### v1.0 8/17/19
* extended port scan in domain_sticate.py to max port range

### v1.0 8/18/19
* added vigenere bruteforcer to decoders.md

### v1.0 8/20/19
* added aircrack-ng to lib_install.sh
* fixed ssh-copy-id id file error
* fixed root call to ~ for all users
* added sherlock libs to lib_install.sh
* added sherlock to KITT
* added blackeye to phishing 

### v1.0 8/23/19
* added coreutils to lib_install.sh

### v1.0 8/24/19
* added WPA/WPA2 cracking dependencies to lib_install.sh
* added hcxdumptool and hcxtools to crackers and make in lib_install.sh

### v1.0 8/25/19
* added reaver to lib_install.sh
* added network_crack.py to KITT.py
* added wash network scan to network_crack.py

### v1.0 8/27/19
* added schoolloop phishing site to blackeye and edited blackeye menu

### v1.0 8/28/19
* added john the ripper and snort to lib_install.sh

### v1.0 8/31/19
* added tshark, netcat, unicornscan, fierce, openvas, nikto, wpscan
* added fluxion necessary libs to lib_install: mawk, curl, dhcpd, hostapd, lighttpd, mdk3, php-cgi, pyrit, unizip, xterm, openssl, rfkill, strings
* added fluxion to network_crack.py
* added fluxion install to lib_install.sh
* added list of lib_install.sh installation candidates: LIB_REGISTER.md
* added SSHauth_check.py to sdefense to check IPs accessing local ssh server

### v1.0 9/1/19
* added sqlmap to lib_install.sh

### v1.0 9/2/19
* added source configuration to lib_install.sh
* added SET to phishing
* added SET libs: pexpect, pycrypto, pyopenssl, pefile, impacket, qrcode, pillow, and pymssql to lib_install.sh
* updated LIB_REGISTER.md

### v1.0 9/3/19
* piped 'Y' into Y/n lib install questions

### v1.0 9/4/19
* added nikto scan to domain_sticate.py in hg/
* added http to pip install

### v1.0 9/8/19
* added masscan to lib_install.sh
* added SSH server check to beginning of SSHauth_check.py
* added Drupalgeddon2 to hg/
* added Drupalgeddon2 shell attempt to domain_sticate.py

### v1.0 9/12/19
* extended range in append_num.py from 100 to 1000000
* added ncrack, arp-scan, and medusa to lib_install.sh

### v1.0 9/13/19
* added sqlmap and dirb to domain_sticate.py
* added dirb, dirbuster, and wfuzz to lib_install.sh
* removed pytz from KITT.py and replaced it with time.ctime() method

### v1.0 9/15/19
* added argparse and dnspython to lib_install.sh
* added Sublist3r to domain_sticate.py
* added CyberChef to crackers/decoders.md
* fixed output directory in domain_sticate.py to outputs
* removed bloat space from hg/outputs
* added outputs directory creation to domain_sticate.py

### v1.0 9/17/19
* added update feature to menu in KITT.py

### v1.0 9/19/19
* added Privesc feature to KITT.py with SimpleHTTPServer to host and Private and Public IP check

### v1.0 9/22/19
* removed most shell tools from KITT.py selections
* compiled all domain_sticate.py outputs to output/report.txt
* removed options 9,10,11, and 12 from KITT.py
* added append_num.py outside of hashcat
* updated hashcat
* added gevent to lib_install.sh
* added XSStrike to domain_sticate.py

### v1.0 9/26/19
* added Wifite2 to network_crack.py
* added vBulletin 5-5.5.4 Scan to domain_sticate.py and vBulletinScan

### v1.0 9/28/19
* added fluxion to network_crack.py - for real this time
* added ettercap to network_crack.py and lib_install.sh
* added necessary libs for running ettercap
* fixed numerical error in choices list in KITT.py

### v1.0 10/4/19
* added pentbox1.8 honeypot tool to KITT.py
* added HiddenSMSTracker apk to rooters
* fixed directory error with rootkits

### v1.0 10/9/19
* added fail2ban to lib_install.sh and added jail.local configuration
* removed SSHauth_checker.py
* added fail2ban to KITT.py

### v1.0 10/14/19
* added php to lib_install.py

### v1.0 10/20/19
* added SSH protocol 2 enforcement, disabled X11 forwarding, set idle timeout, and limited password attempts to ssh_encr7pt.sh

### v1.0 10/27/19
* added HomePWN to KITT
* changed timecheck() output to time.ctime()

### v1.0 11/1/19
* began documentation for KITT.py

### v1.0 11/3/19
* added Ubuntu USB Boot SAM hack method to escalate

### v1.0 11/6/19
* removed rootkits
* replaced rootkits with mousejack and jackit
* added mousejack and jackit firmware upload tools to lib_install.sh
* added mousejack and jackit git configuration to lib_install.sh
* added PhoneInfoga to KITT.py and necessary libs to lib_install.sh

### v1.0 11/8/19
* added sudo support to make and make install for mousejack firmware upload

### v1.0 11/13/19
* fixed domainsticate execution without domain input 

### v1.0 11/14/19
* added linux and mysql escalation scripts from PrivEsc git repo to escalate
* added weevely to lib_install.sh

### v1.0 11/20/19
* added termcolor(pip) and redis(apt) to lib_install.py
* added redis-server-exploit to KITT and /exploits
* added passwd_backdoor.sh exploit to escalate

### v1.0 11/24/19
* added payloads/ w/ P4wnP1 ALOA and php-webshell payloads
* fixed bugs in KITT.py

### v1.0 11/27/19
* redesigned p4wnp1 payloads as templates

### v2.0 11/28/19
* updatd UI into a more organized system
* removed certain features that can be done outside KITT
* updated to KITT2.0
* fixed unspecified names in backup.sh
* updated UI w/ colorama and standardized option color scheme

### v2.0 12/1/19
* updated file error in KITTexe.sh execution to KITT2.py
* added line to payloads/p4wnp1/Reverse_TCP.js
* added mimikatz to escalate

### v2.0 12/2/19
* fixed major functionality bugs in Exploits
* added ddos/ to payloads

### v2.0 12/4/19
* added Net_Share.js and fixed minor bugs in File_Thief and Reverse_TCP

### v2.0 12/7/19
* added GPIO_CTL.py to hardware hacking
* fixed lowercase letter option use in menu error

### v2.0 12/8/19
* fixed pcap file error in network_crack.py
* revamped network_crack.py invalid option method
* added airgeddon to network_crack.py
* added airgeddon to repo

### v2.0 12/10/19
* added AP_Spoofer module to Network Cracking
* added some customization to /AP_Spoof/setup.sh

### v2.0 12/11/19
* reworked minor details in README.md

### v2.0 12/13/19
* fixed wait() call error in KITT2.py
* added git pull origin master to update cloned repo
* added -h to dnsmasq cmd in AP_Spoof/setup.sh to single out specified hostnames in fakehosts.txt
* added Features to README.md
* replaced fluxion/ with official version of fluxion
* added WiFi-Pumpkin as a more advanced method of AP Spoofing to network_crack.py

### v2.0 12/15/19
* changed airmon-ng stop/start exe time in network_crack to specific options
* fixed git issues
* removed sleep calls in airgeddon and add hashcat-utils make to lib_install in airgeddon/

### v2.0 12/16/19
* updated net-creds and added libs to lib_install.sh
* added cap_crack to network_crack.py for WPA/WPA2 handshake cracking
