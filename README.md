# KITT 2.0 Penetration Testing Framework

The KITT Penetration Testing Framework was developed as an open source solution for pentesters and programmers alike to compile the tools they use with what they know into an open source project.
With KITT, users are able to easily access a list of commonly used tools to their profession which are all open to configuration in the source code.

If you prefer a CLI tool to a GUI tool KITT Lite, a lighter and more advanced tool for the command line, can be found [here](<https://github.com/Cisc0-gif/KITT-Lite.git>)

DISCLAIMER: This tool is for educational purposes only. I am not responsible for the misuse of others of this tool in any way, shape or form.


## Features

### OSINT
* FOCA - Fingerprinting Organizations w/ Collected Archives 
* Google Dorks List - Custom list of google dorks
* recon-ng - Web Reconnaissance Framework
* fbi_master - Facebook Informations Tool
* Autosploit - Automated Mass Exploiter
* net-creds.py - Network Traffic Credentials Sniffer
* Domainsticate - Custom domain enumeration tool 
* Shodan Search - Quick Shodan search tool
* PhoneInfoga - OSINT tool for phone numbers
* sonar.py - Mass email sender
* blackeye - Webpage Phishing Tool
* SET - Social Engineers Toolkit

### Exploitation
* Metasploit - Exploitation Framework
* LM Exploit for Windows - Custom Ubuntu usb boot exploit
* Unplug.sh - hosts file editor script
* Cisco_E4200_vuln.py - Cisco Router Vulnerability
* Redis-Server-Exploit.py - Redis Server Vulnerability
* Payloads - PHP Web shells, P4wnP1 ALOA HID Scripts
* OWASP-ZSC - Payload Encoder

### Enumeration
* BIOS_UBTU_Rooter.sh - Custom Ubuntu usb boot exploit
* LinEnum - Linux shell enumeration tool
* Linux - Linux Exploits and Enumeration Scripts
* Mimikatz_trunk - Windows post exploitation tool 
* mysql - MSQL exploits and enumeration scripts
* passwd_backdoor.sh - Custom passwd/ backdoor exploit for post-exploitation
* pspy - Process scanner for linux
* windows-privesc-check - Windows PrivEsc Scripts
* Windows-Privlege-Escalation - Windows PrivEsc Scripts

### Password Cracking
* append_num.py - appends number range 0-99 to any wordlist
* burpsuite - web app vulnerability scanner
* decoders - Popular website for encryption decoding
* ROT_Decrypt - ROT Cipher Brute-Forcer

### Network Cracking
* Airsuite-ng - Software suite w/ detector, packet sniffer, WEP and WPA/WPA2-PSK Cracker and analysis tool
* Wash & Reaver - WPS Cracking tools
* Wifite2 - Network Auditing Tool
* Ettercap - MiTM Attack Suite
* Fluxion - MiTM Attack Suite
* Airgeddon - Network Auditing Tool
* WiFi-Pumpkin - GUI AP Spoofing Tool

### IoT Exploitation
* HomePwn - IoT Exploitation Framework
* PentBox - HoneyPot Setup Tool
* Spooftooph - BT Spoofing
* BtVerifier - Rfcomm Channel Verifier

### Hardware Hacking
* Android Rootkits - HiddenSMSTracker & NewKingroot
* MouseJack - BT Keyboard and Mouse Hijacker
* Keyloggers - Winupdate, kidlogger(win) and staffcounter(lin)
* Digispark Tools - Duck2Spark converter for Digispark Devices
* GPIO_CTL - Custom GPIO Controller for RPi

### System Security
* MAC_changer - MAC Address Spoofer
* ssh_port_randomizer - SSHD Port Randomizer
* ssh rsa_key generator - RSA Key generator
* proxy router - Traffic Proxy Router
* ssh_encryption - Buffing SSHD Security Protocols
* static IP setter - Sets static IP for device
* Fail2ban Configurations - Fail2ban Protocol Auditer

### Misc.
* File Backup - File Backup Tool
* IRCssi - CLI IRC tool

## Getting Started

WARNING: KITT was developed and tested on Kali Linux for RPi, I have not added support for any other distro yet but plan to in the near future.

To begin, run ``` ./KITT_INSTALLER.sh ``` to install all necessary libraries and configure PATH usage.
Simply follow all instructions in the installer.

If you do not want to install KITT to alias then simply run ``` python3 lib_install.py ``` or ``` ./lib_install.py ``` to install necessary libraries


### Usage

To begin the framework, type ``` KITT2 ``` and execute in terminal. 


## Built With

* RPi 3B+ - Micro-Computer Developed by the Raspberry Pi Foundation
* Kali Linux - Pentesting OS Developed by Offensive Security
* GitHub - This Website!


## Authors

* **Cisc0-gif** - *Main Contributor/Author*: Ecorp7@protonmail.com

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details


## Acknowledgments

All credits are given to the authors and contributors to tools used in this software
