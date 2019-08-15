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
