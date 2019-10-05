import os
root = os.getcwd()
import time
start = time.time()
import socket
import requests
import sys
import time
import calendar
import datetime
import random
from datetime import date
from colorama import Fore, Back, Style

def timecheck():
  global check
  check = time.time()
  msg = str(check - start)
  return msg

def logwrite(msg):
  with open(root + '/RUNTIME.log', 'a+') as f:
    f.write(msg + '\n')
    f.close()

os.system('sudo chmod 777 RUNTIME.log')

logwrite('--[*]KITT Initialized in ' + timecheck() + ' seconds--')

print(Fore.CYAN + '[*]Checking OS Version...' + Style.RESET_ALL)
if sys.platform != 'linux':
  logwrite("--[*]User OS Doesn't Register as Debian/Linux @ " + timecheck() + "--")
  print(Fore.RED + "[*]User OS Doesn't Register as Debian/Linux!" + Style.RESET_ALL)
  wait()
  exit()
else:
  logwrite("--[+]User OS Registers as Debian/Linux @ " + timecheck() + "--")
  print(Fore.GREEN + '[+]User OS Registers as Debian/Linux!' + Style.RESET_ALL)

print(Fore.CYAN + '[*]Updating System Libs...' + Style.RESET_ALL)
os.system('sudo apt-get update')
os.system('sudo apt-get upgrade')
os.system('sudo apt autoremove')

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

def home():
  global root
  os.chdir(root)
  os.system("figlet -f slant '   K I T T 1.0'")
  print('================================================================')
  print(' [R] README   | ' + time.ctime() + ' |   [L] CHANGELOG')
  print('                      [U]Update')
  print('================================================================')
  print(Fore.RED + '*[1]  Metaspl0!it - metasploit-framework                       *')
  print('*[2]  dev_r00ters - device rootkits for apk and iphone         *')
  print('*[3]  Rootkit_tens - remote rookits for injection              *')
  print('*[4]  The Cr@ckin - hash/login crackers                        *')
  print('*[5]  Hunter/Gatherer - OSINT gatherers                        *')
  print('*[6]  Key!0ggers - keyloggers                                  *')
  print('*[7]  Ruba_digi_spark - Digispark rubberducky tool             *')
  print('*[8]  Xspl0!ts - viruses, exploits, trojans, misc. (WARNING)   *')
  print('*[9]  little_phishy - phshing tools                            *')
  print('*[10] i_m_a_g_e_s - VMware images                              *')
  print('*[11] b@cker_upper - file backup tool                          *')
  print('*[12] packetdump - packet capture tool                         *')
  print('*[13] domainsticate - doamin recon tool                        *')
  print('*[14] IRCssi - IRC client                                      *')
  print('*[15] self-DeFENSE - track wipers                              *')
  print('*[16] port jack - port listener                                *')
  print('*[17] OWASP-ZSC - payload encoder                              *')
  print('*[18] Investig@te - forensics tools                            *')
  print('*[19] Spooftooph - bluetooth device spoofer                    *')
  print('*[20] ShodanSearch - Shodan Lookup Tool                        *')
  print('*[21] BtVerifier - BT RfComm and Active Verification Tool      *')
  print('*[22] Network_Cr@ck - WEP/WPA/WPA2 Network Cracker             *')
  print('*[23] Enumeration - Lin & Win Enumeration and Privesc Tools    *')
  print('*[24] HoneyPot - Honeypot Network Defense Tool                 *')
  print('*[X]  Fuck_0ff                                                 *')
  print(Style.RESET_ALL + '================================================================')
  in_put = input(Fore.CYAN + os.getcwd() + ': ' + Style.RESET_ALL)
  nums = ['X', 'R', 'L', 'U']
  for i in range(1,25):
    nums.append(str(i))
  if in_put not in nums:
    print(Fore.RED + '[*]Invalid Option' + Style.RESET_ALL)
    wait()
    home()
  elif in_put == '1':
    try:
      logwrite("--[*]Started Msfconsole @ " + timecheck() + '--')
      print(Fore.CYAN + '[*]Starting Metasploit-Framework...')
      os.system('service postgresql start')
      os.system('msfconsole')
      print(Fore.GREEN + '[+]Metasploit-Framework Ran Successfully!' + Style.RESET_ALL)
      logwrite("--[+]Msfconsole ended @ " + timecheck() + '--')
    except:
      logwrite("--[*]Error starting postgresql or msfconsole @ " + timecheck() + '--')
      print(Fore.RED + '[*]Error starting postgresql or msfconsole!' + Style.RESET_ALL)
    wait()
  elif in_put == '2':
    try:
      os.chdir('rooters')
      wait()
      os.system('ls')
      print(Fore.CYAN + '[*]Select a dev rooter for use: ' + Style.RESET_ALL)
      dev_rooter = input('')
      os.system('cp ' + dev_rooter + ' ~')
      print(Fore.GREEN + '[+]dev_rooter ha$ /bin/ cOpied to r00t!' + Style.RESET_ALL)
      logwrite('--[+]Successfully copied dev rooter to root @ ' + timecheck() + '--')
    except:
      logwrite("--[*]Error copying dev rooter @ " + timecheck() + '--')
      print(Fore.RED + '[*]dev_rooter not found!' + Style.RESET_ALL)
    wait()
  elif in_put == '3':
    os.chdir('rootkittens')
    try:
      os.system('ls')
      dev_rooter = input(Fore.CYAN + '[*]Select a rootkit for use: ' + Style.RESET_ALL)
      os.system('cp -R ' + dev_rooter + ' ~')
      print(Fore.GREEN + '[+]r--tkit has /bin/ cOpied to r00t!' + Style.RESET_ALL)
      logwrite("--[+]Successfully copied rootkit to root @ " + timecheck() + '--')
    except:
      logwrite("--[*]Error copying rootkit @ " + timecheck() + '--')
      print(Fore.RED + '[*]rootkit not found!' + Style.RESET_ALL)
      print(os.getcwd())
    wait()
  elif in_put == '4':
    os.chdir('crackers')
    print('[1] append_num')
    print('[2] burpsuite')
    print('[3] dec0ders')
    print('[4] R0T_decrypt - :WARNING: Due to extensive wordlist, KITT may crash under this!')
    print('[5] go home' + Style.RESET_ALL)
    crack = input(Fore.CYAN + "[*]So what'll it be?: " + Style.RESET_ALL)
    if crack == '1':
      logwrite('--[*]Starting append_num.py @ ' + timecheck() + '--')
      os.system('python3 append_num.py')
      wait()
    elif crack == '2':
      logwrite('--[*]Starting burpsuite @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Running Burpsuite..." + Style.RESET_ALL)
      os.system("burpsuite")
      wait()
    elif crack == '3':
      logwrite('--[*]Reading decoders.txt @ ' + timecheck() + '--')
      with open('decoders.txt', 'r') as f:
        contents = f.read()
      print(contents)
      wait()
    elif crack == '4':
      logwrite('--[*]Running ROT Bruteforcer @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      def recursion():
        message = input("[*]ROT Cipher Text: " + Style.RESET_ALL).lower().split(' ')
        if message == 'q':
          wait()
          home()
        else:
          LETTERS = 'abcdefghijklmnopqrstuvwxyz'
          l = []
          for word in list(message):
            for key in range(len(LETTERS)):
              translated = ''
              for symbol in word:
                if symbol in LETTERS:
                  num = LETTERS.find(symbol)
                  num = num - key
                  if num < 0:
                    num = num + len(LETTERS)
                  translated = translated + LETTERS[num]
                else:
                  translated = translated + symbol
              l.append(translated)
          with open('Edictionary.txt', 'r') as f:
            wordlist = f.read().splitlines()
            for i in l:
              if i in wordlist:
                print(Fore.GREEN + '[+]Decrypted Ciphertext: "' + i + '"' + Style.RESET_ALL)
          wait()
          recursion()

      recursion()
    elif crack == '5':
      wait()
  elif in_put == '5':
    os.chdir('hg')
    print(Fore.RED + 'Welcome to 2/3 of you life...')
    print('[1] FOCA - Windows')
    print('[2] g00gle dorks')
    print('[3] r#con-ng')
    print('[4] fbi_master')
    print('[5] Aut0Sp!oit')
    print('[6] Net-Creds SNiffer')
    print('[7] go home' + Style.RESET_ALL)
    hg = input(Fore.CYAN + os.getcwd() + ': ' + Style.RESET_ALL)
    if hg == '1':
      try:
        os.system('cp -R FOCA ~')
        print(Fore.GREEN + '[+]FOCA copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied FOCA to root @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]FOCA not found!' + Style.RESET_ALL)
        logwrite('--[*]Error copying FOCA @ ' + timecheck() + '--')
      wait()
    elif hg == '2':
      logwrite('--[*]Reading dorks.md @ ' + timecheck() + '--')
      try:
        with open('dorks.md', 'r') as f:
          contents = f.read()
        print(contents)
      except:
        logwrite('--[*]Error reading dorks.md @ ' + timecheck() + '--')
        print(Fore.RED + '[*]dorks not found!' + Style.RESET_ALL)
      wait()
    elif hg == '3':
      try:
        print(Fore.CYAN + '[*]Starting recon-ng...' + Style.RESET_ALL)
        logwrite('--[*]Starting recon-ng @ ' + timecheck() + '--')
        os.system('recon-ng')
        print(Fore.GREEN + '[+]Successfully ended recon-ng!' + Style.RESET_ALL)
        logwrite('--[*]Successfully ended recon-ng @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error running recon-ng!' + Style.RESET_ALL)
        logwrite('--[*]Error running recon-ng @ ' + timecheck() + '--')
      wait()
    elif hg == '4':
      try:
        os.chdir('fbi-master')
        print(Fore.CYAN + '[*]Running fbi.py...' + Style.RESET_ALL)
        logwrite('--[*]Running fbi.py @ ' + timecheck() + '--')
        os.system('python fbi.py')
        print(Fore.GREEN + '[+]Successfully ended fbi.py!' + Style.RESET_ALL)
        logwrite('--[*]Successfully ended fbi.py @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error in running fbi.py!' + Style.RESET_ALL)
        logwrite('--[*]Error in running fbi.py @ ' + timecheck() + '--')
      wait()
    elif hg == '5':
      try:
        os.chdir('AutoSploit')
        print(Fore.CYAN + '[*]Running autosploit.py...' + Style.RESET_ALL)
        logwrite('--[*]Running autosploit.py @ ' + timecheck() + '--')
        os.system('python autosploit.py')
        print(Fore.GREEN + '[+]Successfully ended autosploit.py!' + Style.RESET_ALL)
        logwrite('--[*]Successfully ended autosploit.py @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error running autosploit.py!' + Style.RESET_ALL)
        logwrite('--[*]Error running autosploit.py @ ' + timecheck() + '--')
      wait()
    elif hg == '6':
      print(Fore.CYAN + '[*]Running net-creds.py packet sniffer...' + Style.RESET_ALL)
      logwrite('--[*]Running net-creds.py @ ' + timecheck() + '--')
      try:
        print(Fore.CYAN + '[*]Enter ^C or ^Z to stop packet sniffer' + Style.RESET_ALL)
        os.system('python net-creds.py')
        print(Fore.GREEN + '[+]Output directed to credentials.txt!' + Style.RESET_ALL)
        logwrite('--[*]Successfully ended net-creds.py @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Packet Sniffer ended prematurely!' + Style.RESET_ALL)
        logwrite('--[*]Error running net-creds.py @ ' + timecheck() + '--')
      wait() 
    elif hg == '7':
      wait()
  elif in_put == '6':
    os.chdir('keyloggers')
    print('[1] Winupdate')
    print('[2] kidlogger(win)')
    print('[3] staffcounter(lin)')
    print('[4] go home')
    keylog = input(os.getcwd() + ': ')
    if keylog == '1':
      try:
        os.system('cp -R Winupdate ~')
        print(Fore.GREEN + '[+]keylogger copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied keylogger @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error copying keylogger @ ' + timecheck() + '--')
        print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
      wait()
    elif keylog == '2':
      try:
        os.system('cp -R KidLogger-setupwin26-11-2017 ~')
        print(Fore.GREEN + '[+]keylogger copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied keylogger @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error copying keylogger @ ' + timecheck() + '--')
        print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
      wait()
    elif keylog == '3':
      try:
        os.system('cp -R staffcounter_install ~')
        print(Fore.GREEN + '[+]keylogger copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied keylogger @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error copying keylogger @ ' + timecheck() + '--')
        print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
      wait()
    elif keylog == '4':
      wait()
  elif in_put == '7':
    os.chdir('digis')
    print(Fore.CYAN + '[*]Running duck2spark converter...' + Style.RESET_ALL)
    logwrite('--[*]Running duck2spark converter @ ' + timecheck() + '--')
    print(Fore.CYAN + '[*[Your current directory: ' + Style.RESET_ALL + os.getcwd())
    try:
      os.system('sudo ./convert.sh')
      print(Fore.GREEN + '[+]Successfully converted ducky script to spark!' + Style.RESET_ALL)
      logwrite('--[+]Successfully converted script @ ' + timecheck() + '--') 
    except:
      print(Fore.RED + '[*]Error running duck2spark...' + Style.RESET_ALL)
      logwrite('--[*]Error runnnig duck2spark @ ' + timecheck() + '--')
    wait()
  elif in_put == '8':
    os.chdir('exploits')
    print('[1] LM_expl0it_WIN.sh')
    print('[2] Unp!ug.sh')
    print('[3] Cisco_E4200_vuln.py')
    print('[4] go home')
    exploit = input(os.getcwd() + ': ')
    if exploit == '1':
      try:
        os.system('cp -R LM_exploit_WIN.sh ~')
        print(Fore.GREEN + '[+]exploit copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied exploit @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error copying exploit @ ' + timecheck() + '--')
        print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
      wait()
    elif exploit == '2':
      try:
        os.system('cp -R unplug.sh ~')
        print(Fore.GREEN + '[+]exploit copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied exploit @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error copying exploit @ ' + timecheck() + '--')
        print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
      wait()
    elif exploit == '3':
      try:
        os.system('cp -R Cisco_E4200_vuln.py ~')
        print(Fore.GREEN + '[+]exploit copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied exploit @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error copying exploit @ ' + timecheck() + '--')
        print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
      wait()
    elif exploit == '4':
      wait()
  elif in_put == '9':
    os.chdir('phishing')
    print('[1] sonar.py - batch email sender')
    print('[2] blackeye - webpage phishing generator')
    print('[3] SET - Social Engineer Toolkit')
    print('[4] go home')
    phish = input(': ')
    if phish == '1':
      try:
        os.system('python3 sonar.py')
        print(Fore.GREEN + '[+]Ended sonar.py!')
        logwrite('--[*]Successfully ended sonar.py @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]sonar.py not found!' + Style.RESET_ALL)
        logwrite('--[*]Error running sonar.py @ ' + timecheck() + '--')
      wait()
    elif phish == '2':
      os.chdir('blackeye')
      try:
        os.system('bash blackeye.sh')
        print(Fore.GREEN + '[+]Ended blackeye.sh!')
        logwrite('--[*]Successfully ended blackeye.sh @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]blackeye.sh not found!' + Style.RESET_ALL)
        logwrite('--[*]Error running blackeye.sh @ ' + timecheck() + '--')
      wait()
    elif phish == '3':
      os.chdir('SET')
      try:
        os.system('python setoolkit')
        print(Fore.GREEN + '[+]Ended SET!')
        logwrite('--[*]Successfully ended SET @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]SET not found!' + Style.RESET_ALL)
        logwrite('--[*]Error running SET @ ' + timecheck() + '--')
      wait()
    elif phish == '4':
      wait()
  elif in_put == '10':
    os.chdir('images')
    print('[1] Ubuntu_18.04 ')
    print('[2] Kali_amd64')
    print('[3] Win10_x64')
    print('[4] Win8_x64')
    print('[5] Win7_Ultimate x64')
    print('[6] go home')
    image = input(': ')
    if image == '1':
      try:
        os.system('cp -R ubuntu-18.04-desktop-amd64.iso ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied image to root @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
        logwrite('--[*]Error copying image @ ' + timecheck() + '--')
      wait()
    if image == '2':
      try:
        os.system('cp -R kali-linux-2019.2-vmware-amd64.7z ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied image to root @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
        logwrite('--[*]Error copying image @ ' + timecheck() + '--')
      wait()
    if image == '3':
      try:
        os.system('cp -R en_windows_10_x64_dvd.iso ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied image to root @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
        logwrite('--[*]Error copying image @ ' + timecheck() + '--')
      wait()
    if image == '4':
      try:
        os.system('cp -R en_windows_8_1_x64_dvd_2707217.iso ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied image to root @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error copying image @ ' + timecheck() + '--')
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
      wait()
    if image == '5':
      try:
        os.system('cp -R en_windows_7_Ult_64Bit.iso ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
        logwrite('--[+]Successfully copied image to root @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error copying image @ ' + timecheck() + '--')
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
      wait()
    if image == '6':
      wait()
  elif in_put == '11':
    try:
      print(Fore.CYAN + '[*]Running backup.sh...' + Style.RESET_ALL)
      os.system('sudo ./backup.sh')
      logwrite('--[*]Successfully ended backup.sh @ ' + timecheck() + '--')
    except:
      logwrite('--[*]Error running backup.sh @ ' + timecheck() + '--')
      print(Fore.RED + '[*]Error running backup.sh' + Style.RESET_ALL)
    wait()
  elif in_put == '12':
    try:
      print(Fore.CYAN + '[*]Running packetdump.sh...' + Style.RESET_ALL)
      os.system('sudo ./packetdump.sh')
      os.system('mv output.pcap ~')
      logwrite('--[+]Packetdump.sh output directed to root @ ' + timecheck() + '--')
      print(Fore.GREEN + '[+]copied packet capture to r00t!' + Style.RESET_ALL)
    except:
      logwrite('--[*]Error writing output to root @ ' + timecheck() + '--')
      print(Fore.RED + '[*]packet capture not found!' + Style.RESET_ALL)
    wait()
  elif in_put == '13':
    os.chdir('hg')
    try:
      print(Fore.CYAN + '[*]Running domain_sticate.py...' + Style.RESET_ALL)
      os.system('python3 domain_sticate.py')
      print(Fore.GREEN + '[+]Successfully ended domain_sticate.py' + Style.RESET_ALL)
      logwrite('--[+]Successfully ended domain_sticate.py @ ' + timecheck() + '--')
    except:
      print(Fore.RED + '[*]Error in file domain_sticate.sh' + Style.RESET_ALL)
      logwrite('--[*]Error running doamin_sticate.py @ ' + timecheck() + '--')
    wait()
  elif in_put == '14':
    try:
      print(Fore.CYAN + '[*]Running irssi...' + Style.RESET_ALL)
      os.system('irssi')
      print(Fore.GREEN + '[+]Successfully ended irssi' + Style.RESET_ALL)
      logwrite('--[+]Successfully ended irssi @ ' + Style.RESET_ALL)
    except:
      logwrite('--[*]Error running irssi @ ' + timecheck() + '--')
      print(Fore.RED + '[*]Error running irssi!' + Style.RESET_ALL)
    wait()
  elif in_put == '15':
    os.chdir('sdefense')
    print('[1] MAC_changer')
    print('[2] ssh_p0Rt_r@andomizer')
    print('[3] ssh rsa_key generator')
    print('[4] pr0xy router')
    print('[5] ssh_encr7tion')
    print('[6] st@tic IP')
    print('[7] SSH Auth IP Check')
    print('[8] go home')
    rdefense = input(': ')
    if rdefense == '1':
      try:
        logwrite('--[*]Running macchanger.sh @ ' + timecheck() + '--')
        print(Fore.CYAN + '[*]Running macchanger.sh...' + Style.RESET_ALL)
        os.system('./macchanger.sh')
        print(Fore.GREEN + '[+]Successfully ended macchanger.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended macchanger @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error in changing mac address!' + Style.RESET_ALL)
        logwrite('--[*]Error running macchanger.sh @ ' + timecheck() + '--')
      wait()
    elif rdefense == '2':
      try:
        logwrite('--[*]Running ssh_randomizer.sh @ ' + timecheck() + '--')
        print(Fore.CYAN + '[*]Running ssh_randomizer.sh...' + Style.RESET_ALL)
        os.system('./ssh_randomizer.sh')
        print(Fore.GREEN + '[+]Successfully ended ssh_randomizer.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended ssh_randomizer.sh @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error in changing ssh port' + Style.RESET_ALL)
        logwrite('--[*]Error running ssh_randomizer.sh @ ' + timecheck() + '--')
      wait()
    elif rdefense == '3':
      try:
        print(Fore.CYAN + '[*]Beginning RSA Key Generation Process...' + Style.RESET_ALL)
        os.system('sudo service ssh start')
        print(Fore.GREEN + '[+]ssh daemon started...' + Style.RESET_ALL)
        os.system('mkdir ~/.ssh')
        print(Fore.GREEN + '[+]key directory generated...' + Style.RESET_ALL)
        uname = input('Enter username for ssh: ')
        port = input('Enter local ssh port: ')
        print('Leave filepath for keys blank for default')
        os.system('ssh-keygen')
        print(Fore.GREEN + '[+]ssh rsa keys generated...' + Style.RESET_ALL)
        os.system('ssh-copy-id -i ~/.ssh/id_rsa ' + uname + '@localhost -p ' + port)
        print(Fore.GREEN + '[+]ssh keys copied to ssh server...' + Style.RESET_ALL)
        os.system('ssh ' + uname + '@localhost -p ' + port)
        os.system('exit')
        print(Fore.GREEN + '[+]ssh connection test successful...' + Style.RESET_ALL)
        os.system('cp ~/.ssh/id_rsa ~/')
        print(Fore.GREEN + '[+]private key copied to root...' + Style.RESET_ALL)
        print(Fore.GREEN + '[+]SSH RSA Key Login Setup Complete!')
        logwrite('--[+]SSH RSA Key Login Setup Complete @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error Running SSH RSA Login Setup!' + Style.RESET_ALL)
        logwrite('--[*]Error running ssh rsa key login setup @ ' + timecheck() + '--')
      wait()
    elif rdefense == '4':
      try:
        print(Fore.CYAN + '[*]Running proxy_config.sh' + Style.RESET_ALL)
        os.system('./proxy_config.sh')
        print(Fore.GREEN + '[+]Successfully ended proxy_config.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended proxy_config.sh @ ' + timecheck() + '--')
      except:
        print(Fore.RED + '[*]Error in running proxy_config.sh!' + Style.RESET_ALL)
        logwrite('--[*]Error running proxy_config.sh @ ' + timecheck() + '--')
      wait()
    elif rdefense == '5':
      try:
        print(Fore.CYAN + '[*]Running ssh_encr7pt.sh...' + Style.RESET_ALL)
        os.system('./ssh_encr7pt.sh')
        print(Fore.GREEN + '[+]Successfully ended ssh_encr7pt.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended ssh_encr7pt.sh @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error running ssh_encr7pt.sh @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error in running ssh_encr7pt.sh!' + Style.RESET_ALL)
      wait()
    elif rdefense == '6':
      try:
        print(Fore.CYAN + '[*]Running static_ip.sh...' + Style.RESET_ALL)
        os.system('./static_ip.sh')
        print(Fore.GREEN + '[+]Successfully ended static_ip.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended static_ip.sh @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error running static_ip.sh @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running static_ip.sh!' + Style.RESET_ALL)
      wait()
    elif rdefense == '7':
      try:
        print(Fore.CYAN + '[*]Running SSHauth_check.sh...' + Style.RESET_ALL)
        os.system('python3 SSHauth_check.py')
        print(Fore.GREEN + '[+]Successfully ended SSHauth_check.sh!' + Style.RESET_ALL)
        logwrite('--[+]Successfully ended SSHauth_check.sh @ ' + timecheck() + '--')
      except:
        logwrite('--[*]Error running SSHauth_check_ip.sh @ ' + timecheck() + '--')
        print(Fore.RED + '[*]Error running SSHauth_check.sh!' + Style.RESET_ALL)
      wait()
    elif rdefense == '8':
      wait()
  elif in_put == '16':
    port = input('Enter port number to listen on: ')
    try:
      logwrite('--[*]Listening on port ' + port + ' @ ' + timecheck() + '--')
      print(Fore.CYAN + '[*]Listening on port ' + port + '!' + Style.RESET_ALL)
      os.system('nc -l -p ' + port )
      print(Fore.GREEN + '[+]Listener Finished!' + Style.RESET_ALL)
      logwrite('--[+]Listener Finished @ ' + timecheck() + '--')
    except:
      logwrite('--[*]Error setting up listener on port ' + port + ' @ ' + timecheck() + '--')
      print(Fore.RED + '[*]Error setting up listener on port ' + port + '!' + Style.RESET_ALL)
    wait()
  elif in_put == '17':
    try:
      print(Fore.CYAN + '[*]Running OWASP-ZSC...' + Style.RESET_ALL)
      os.chdir('OWASP-ZSC')
      os.system('python zsc.py')
      print(Fore.GREEN + '[+]Successfully ended OWASP-ZSC!' + Style.RESET_ALL)
      logwrite('--[+]Successfully ended OWASP-ZSC @ ' + timecheck() + '--')
    except:
      logwrite('--[*]Error Running OWASP-ZSC @ ' + timecheck() + '--')
      print(Fore.RED + '[*]Error Running OWASP-ZSC!' + Style.RESET_ALL)
    wait()
  elif in_put == '18':
    print('[1] gdb')
    print('[2] radare2')
    print('[3] strace')
    print('[4] nano')
    print('[5] sort')
    print('[6] cat & grep')
    print('[7] file')
    print('[8] ls -l')
    print('[9] exiftool')
    print('[10] steghide')
    print('[11] xxd')
    print('[12] go home')
    forensic = input(os.getcwd() + ': ')
    if forensic == '1':
      logwrite('--[*]Running gdb shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]gdb syntax = gdb ./file.ext" + Style.RESET_ALL)
      def recursion():
        gdb = input(os.getcwd() + ': ')
        if gdb == 'q':
          wait()
          home()
        else:
          os.system(gdb)
          recursion()
      recursion()
    elif forensic == '2':
      logwrite('--[*]Running radare2 shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Radare2 syntax = r2 file.ext -d (debugger)" + Style.RESET_ALL)
      def recursion():
        r2 = input(os.getcwd() + ': ')
        if r2 == 'q':
          wait()
          home()
        else:
          os.system(r2)
          recursion()
      recursion()
    elif forensic == '3':
      logwrite('--[*]Running strace shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Strace syntax = strace file.ext" + Style.RESET_ALL)
      def recursion():
        st = input(os.getcwd() + ': ')
        if st == 'q':
          wait()
          home()
        else:
          os.system(st)
          recursion()
      recursion()
    elif forensic == '4':
      logwrite('--[*]Running nano shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Nano syntax = nano file.ext" + Style.RESET_ALL)
      def recursion():
        nano = input(os.getcwd() + ': ')
        if nano == 'q':
          wait()
          home()
        else:
          os.system(nano)
          recursion()
      recursion()
    elif forensic == '5':
      logwrite('--[*]Running sort shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Sort syntax = sort [option] file.ext" + Style.RESET_ALL)
      def recursion():
        sort = input(os.getcwd() + ': ')
        if sort == 'q':
          wait()
          home()
        else:
          os.system(sort)
          recursion()
      recursion()
    elif forensic == '6':
      logwrite('--[*]Running cat & grep shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]cat & grep syntax = cat file.ext | grep keyword" + Style.RESET_ALL)
      def recursion():
        cg = input(os.getcwd() + ': ')
        if cg == 'q':
          wait()
          home()
        else:
          os.system(cg)
          recursion()
      recursion()
    elif forensic == '7':
      logwrite('--[*]Running file shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]File syntax = file file.ext" + Style.RESET_ALL)
      def recursion():
        file = input(os.getcwd() + ': ')
        if file == 'q':
          wait()
          home()
        else:
          os.system(file)
          recursion()
      recursion()
    elif forensic == '8':
      file = input(Fore.CYAN + '[*]Enter filename and filepath here (/fp/fn): ' + Style.RESET_ALL)
      os.system('ls -l ' + file)
      logwrite('--[*]Ran file ls forensic @ ' + timecheck() + '--')
      wait()
      home()
    elif forensic == '9':
      logwrite('--[*]Running exiftool shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Exiftool syntax = exiftool [options] file.ext" + Style.RESET_ALL)
      def recursion():
        et = input(os.getcwd() + ': ')
        if et == 'q':
          wait()
          home()
        else:
          os.system(et)
          recursion()
      recursion()
    elif forensic == '10':
      logwrite('--[*]Running stehide shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Steghide syntax = steghide embed/extract file.ext" + Style.RESET_ALL)
      def recursion():
        sh = input(os.getcwd() + ': ')
        if sh == 'q':
          wait()
          home()
        else:
          os.system(sh)
          recursion()
      recursion()
    elif forensic == '11':
      logwrite('--[*]Running xxd shell @ ' + timecheck() + '--')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]xxd syntax = xxd [options] file.ext outfile.txt" + Style.RESET_ALL)
      def recursion():
        xd = input(os.getcwd() + ': ')
        if xd == 'q':
          wait()
          home()
        else:
          os.system(xd)
          recursion()
      recursion()
    elif forensic == '12':
      wait()
      home()
  elif in_put == '19':
    try:
      print(Fore.CYAN + '[*]Running bluespoof.sh...' + Style.RESET_ALL)
      os.system('./bluespoof.sh')
      print(Fore.GREEN + '[+]Successfully ended bluespoof.sh!' + Style.RESET_ALL)
      logwrite('--[+]Successfully ended bluespoof.sh @ ' + timecheck() + '--')
    except:
      logwrite('--[*]Error running bluespoof.sh @ ' + timecheck() + '--')
      print(Fore.RED + '[*]Error running bluespoof.sh!' + Style.RESET_ALL)
    wait()
  elif in_put == '20':
    try:
      print(Fore.CYAN + '[*]Running shodan_search.py...' + Style.RESET_ALL)
      os.system('python3 shodan_search.py')
      print(Fore.GREEN + '[+]Successfully ended shodan_search.py!' + Style.RESET_ALL)
      logwrite('--[*]Successfully ended shodan_search.py @ ' + timecheck() + '--')
    except:
      logwrite('--[*]Error running shodan_search.py @ ' + timecheck() + '--')
      print(Fore.RED + '[*]Error running shodan_search.py!' + Style.RESET_ALL)
    wait()
  elif in_put == '21':
    try:
      print(Fore.CYAN + '[*]Running btverifier.py...' + Style.RESET_ALL)
      os.system('python3 btverifier.py')
      print(Fore.GREEN + '[+]Successfully ended btverifier.py!' + Style.RESET_ALL)
      logwrite('--[*]Successfully ended btverifier.py @ ' + timecheck() + '--')
    except:
      print(Fore.RED + '[*]Error running btverifier.py!' + Style.RESET_ALL)
      logwrite('--[*]Error running btverifier.py @ ' + timecheck() + '--')
    wait()
  elif in_put == '22':
    try:
      print(Fore.CYAN + '[*]Running network_crack.py...' + Style.RESET_ALL)
      os.system('python3 network_crack.py')
      print(Fore.GREEN + '[*]Successfully ended network_crack.py!' + Style.RESET_ALL)
      logwrite('--[*]Successfully ended network_crack.py @ ' + timecheck() + '--')
    except:
      print(Fore.RED + '[*]Error running network_crack.py!' + Style.RESET_ALL)
      logwrite('--[*]Error running network_crack.py @ ' + timecheck() + '--')
    wait()
  elif in_put == '23':
    os.chdir('escalate')
    try:
      print(Fore.CYAN + '[*]Starting python SimpleHTTPServer on Port 80 to curl payloads...')
      print(Fore.CYAN + '[*]Enter ^C or ^Z To Stop HTTP Server...')
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(("8.8.8.8", 80))
      r = requests.get("http://ifconfig.me").text
      print(Fore.CYAN + '[*]Private IP: ' + Style.RESET_ALL + str(s.getsockname()[0]))
      print(Fore.CYAN + '[*]Public IP: ' + Style.RESET_ALL + str(r))
      os.system("python -m SimpleHTTPServer 80")
      s.close()
      print(Fore.GREEN + '[+]Successfully ended SimpleHTTPServer!' + Style.RESET_ALL)
      logwrite('--[*]Successfully ended SimpleHTTPServer @ ' + timecheck() + '--')
    except:
      print(Fore.RED + '[*]Error running SimpleHTTPServer!' + Style.RESET_ALL)
      logwrite('--[*]Error running SimpleHTTPServer @ ' + timecheck() + '--')
    wait()
  elif in_put == '24':
    os.chdir('pentbox/pentbox-1.8')
    try:
      print(Fore.CYAN + '[*]Running Pentbox1.8...' + Style.RESET_ALL)
      os.system('./pentbox.rb')
      logwrite('--[+]Successfully ended Pentbox1.8 @ ' + timecheck() + '--')
      print(Fore.GREEN + '[+]Successfully ended Pentbox1.8!' + Style.RESET_ALL)
    except:
      logwrite('--[*]Error running Pentbox1.8 @ ' + timecheck() + '--')
      print(Fore.RED + '[*]Error running Pentbox1.8!' + Style.RESET_ALL)
    wait()
  elif in_put == 'R':
    os.chdir(root)
    print(Fore.CYAN + '[*]Reading README.md...' + Style.RESET_ALL)
    logwrite('--[*]Reading README.md @ ' + timecheck() + '--')
    os.system('more README.md')
    wait()
  elif in_put == 'U':
    try:
      print(Fore.CYAN + '[*]Updating System Libs...' + Style.RESET_ALL)
      os.system('sudo apt update')
      print(Fore.GREEN + '[+]Done!' + Style.RESET_ALL)
      print(Fore.CYAN + '[*]Upgrading Packages & Dependencies...' + Style.RESET_ALL)
      os.system('sudo apt upgrade')
      print(Fore.GREEN + '[+]Done!' + Style.RESET_ALL)
      print(Fore.CYAN + '[*]Removing Deprecated Packages...' + Style.RESET_ALL)
      os.system('sudo apt autoremove')
      print(Fore.GREEN + '[+]Done!' + Style.RESET_ALL)
      logwrite('--[*]Successfully Updated Packages @ ' + timecheck() + '--')
    except:
      print(Fore.RED + '[*]Error Updating Packages...' + Style.RESET_ALL)
      logwrite('--[*]Error Updating Packages @ ' + timecheck() + '--')
    wait()
  elif in_put == 'L':
    os.chdir(root)
    print(Fore.CYAN + '[*]Reading CHANGELOG.md...' + Style.RESET_ALL)
    logwrite('--[*]Reading CHANGELOG.md @ ' + timecheck() + Style.RESET_ALL)
    os.system('more CHANGELOG.md')
    wait() 
  elif in_put == 'X':
    print(Fore.CYAN + '[*]Killing KITT...' + Style.RESET_ALL)
    print(Fore.RED + '[*]Bye Bye!' + Style.RESET_ALL)
    logwrite('--[*]Log Closed @ ' + timecheck() + '--')
    exit()
  home()

home()
