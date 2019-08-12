import os
import time
import sys
import pytz
import time
import calendar
import datetime
import random
from datetime import date
from colorama import Fore, Back, Style

then = datetime.datetime.now(pytz.utc)
local = then.astimezone(pytz.timezone('America/Los_Angeles'))
my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]

if sys.platform != 'linux':
  print(Fore.RED + "[*]User OS Doesn't Register as Debian/Linux!" + Style.RESET_ALL)
  wait()
else:
  print(Fore.GREEN + '[+]User OS Registers as Debian/Linux!' + Style.RESET_ALL)

os.system('sudo apt-get update')
os.system('sudo apt-get upgrade')
os.system('sudo apt autoremove')
root = os.getcwd()

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

def home():
  global root
  os.chdir(root)
  os.system("figlet -f slant '   K I T T 1.0'")
  print('================================================================')
  print(' [R] README   | ' + local.strftime("%a, %b %d, %Y") + ' - ' + local.strftime("%I:%M %p") + ' |   [L] CHANGELOG')
  print('================================================================')
  print(Fore.RED + '*[1]  Metaspl0!it - metasploit-framework                       *')
  print('*[2]  dev_r00ters - device rootkits for apk and iphone         *')
  print('*[3]  Rootkit_tens - remote rookits for injection              *')
  print('*[4]  The Cr@ckin - hash/login crackers                        *')
  print('*[5]  Hunter/Gatherer - OSINT gatherers                        *')
  print('*[6]  Key!0ggers - keyloggers                                  *')
  print('*[7]  Ruba_digi_spark - Digispark rubberducky tool             *')
  print('*[8]  Xspl0!ts - viruses, exploits, trojans, misc. (WARNING)   *')
  print('*[9]  SSHit - ssh client                                       *')
  print('*[10] TOR_tilinni - tor connection startup                     *')
  print('*[11] nmaPPer - nmap client                                    *')
  print('*[12] NC - nc/cryptcat client                                  *')
  print('*[13] little_phishy - phshing tools                            *')
  print('*[14] i_m_a_g_e_s - VMware images                              *')
  print('*[15] b@cker_upper - file backup tool                          *')
  print('*[16] packetdump - packet capture tool                         *')
  print('*[17] domainsticate - doamin recon tool                        *')
  print('*[18] IRCssi - IRC client                                      *')
  print('*[19] self-DeFENSE - track wipers                              *')
  print('*[20] port jack - port listener                                *')
  print('*[21] OWASP-ZSC - payload encoder                              *')
  print('*[22] Investig@te - forensics tools                            *')
  print('*[23] Spooftooph - bluetooth device spoofer                    *')
  print('*[24] ShodanSearch - Shodan Lookup Tool                        *')
  print('*[X]  Fuck_0ff                                                 *')
  print(Style.RESET_ALL + '================================================================')
  in_put = input(Fore.CYAN + os.getcwd() + ': ' + Style.RESET_ALL)
  nums = ['X', 'R', 'L']
  for i in range(1,25):
    nums.append(str(i))
  if in_put not in nums:
    print(Fore.RED + '[*]Invalid Option' + Style.RESET_ALL)
    wait()
    home()
  elif in_put == '1':
    os.system('service postgresql start')
    os.system('msfconsole')
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
    except:
      print(Fore.RED + '[*]dev_rooter not found!' + Style.RESET_ALL)
    wait()
  elif in_put == '3':
    os.chdir('rootkittens')
    try:
      os.system('ls')
      dev_rooter = input(Fore.CYAN + '[*]Select a rootkit for use: ' + Style.RESET_ALL)
      os.system('cp -R ' + dev_rooter + ' ~')
      print(Fore.GREEN + '[+]r--tkit has /bin/ cOpied to r00t!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]rootkit not found!' + Style.RESET_ALL)
      print(os.getcwd())
    wait()
  elif in_put == '4':
    os.chdir('crackers')
    print('[1] hashcat')
    print('[2] append_num')
    print('[3] hydr@')
    print('[4] burpsuite')
    print('[5] dec0ders')
    print('[6] crunch')
    print('[7] 7zCracker')
    print('[8] cewl')
    print('[9] R0T_decrypt - :WARNING: Due to extensive wordlist, KITT may crash under this!')
    print('[10] go home' + Style.RESET_ALL)
    crack = input(Fore.CYAN + "[*]So what'll it be?: " + Style.RESET_ALL)
    if crack == '1':
      os.chdir('hashcat')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Hashcat syntax = hashcat -a # -m # hash/hashlist.txt wordlist.txt bruteforce mask ?#?#?#?#?#" + Style.RESET_ALL)
      def recursion():
        in_put = input(Fore.CYAN + os.getcwd() + ': ' + Style.RESET_ALL)
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '2':
      os.chdir('hashcat')
      os.system('python3 append_num.py')
      wait()
    elif crack == '3':
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Hydra syntax = hydra -l/-L uname/uname.lst -p/-P pass/pass.lst url type" + Style.RESET_ALL)
      def recursion():
        in_put = input(Fore.CYAN + os.getcwd() + ': ' + Style.RESET_ALL)
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '4':
      print(Fore.CYAN + "[*]Running Burpsuite..." + Style.RESET_ALL)
      os.system("burpsuite")
      wait()
    elif crack == '5':
      with open('decoders.txt', 'r') as f:
        contents = f.read()
      print(contents)
      wait()
    elif crack == '6':
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Crunch syntax = crunch min-max -t @,%^(chars to insert) -f charset.lst -i (inverts output) -q readfile.lst -o output.lst" + Style.RESET_ALL)
      def recursion():
        in_put = input(os.getcwd() + ': ' + Style.RESET_ALL)
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '7':
      os.chdir('7zip-crack')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("7zipcrack syntax = ./7zipcrack file.7z wordlist.lst" + Style.RESET_ALL)
      def recursion():
        in_put = input(os.getcwd() + ': ' + Style.RESET_ALL)
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '8':
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Cewl syntax = cewl -d #(site depth) -m #(min len) -o (offsite) -ua ###(user agent) --with-numbers --meta_file file.txt --email_file file.txt -w output.txt" + Style.RESET_ALL)
      def recursion():
        in_put = input(os.getcwd() + ': ' + Style.RESET_ALL)
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '9':
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
                print(Fore.CYAN + '[*]Decrypted Ciphertext: "' + i + '"' + Style.RESET_ALL)
          wait()
          recursion()

      recursion()
    elif crack == '10':
      wait()
  elif in_put == '5':
    os.chdir('hg')
    print(Fore.RED + 'Welcome to 2/3 of you life...')
    print('[1] JoomlaScan')
    print('[2] theHarvester')
    print('[3] FOCA - Windows')
    print('[4] google email index')
    print('[5] g00gle dorks')
    print('[6] r#con-ng')
    print('[7] fbi_master')
    print('[8] Aut0Sp!oit')
    print('[9] go home' + Style.RESET_ALL)
    hg = input(Fore.CYAN + os.getcwd() + ': ' + Style.RESET_ALL)
    if hg == '1':
      os.chdir('JoomlaScan')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print('[*]JoomlaScan syntax = python joomlascan.py -u url -t #(threads)' + Style.RESET_ALL)
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif hg == '2':
      os.chdir('theHarvester')
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]theHarvester syntax = python3 theHarvester.py -d domain -b source(google,twitter) -l #(limit) -s (start)" + Style.RESET_ALL)
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif hg == '3':
      try:
        os.system('cp -R FOCA ~')
        print(Fore.CYAN + '[+]FOCA copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]FOCA not found!' + Style.RESET_ALL)
      wait()
    elif hg =='4':
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print('[*]goog-mail.py syntax = python goog-mail.py -d domain' + Style.RESET_ALL)
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif hg == '5':
      try:
        with open('dorks.md', 'r') as f:
          contents = f.read()
        print(contents)
      except:
        print(Fore.RED + '[*]dorks not found!' + Style.RESET_ALL)
      wait()
    elif hg == '6':
      os.system('recon-ng')
      wait()
    elif hg == '7':
      try:
        os.chdir('fbi-master')
        os.system('python fbi.py')
      except:
        print(Fore.RED + '[*]Error in running fbi-master!' + Style.RESET_ALL)
      wait()
    elif hg == '8':
      try:
        os.chdir('AutoSploit')
        os.system('python autosploit.py')
      except:
        print(Fore.RED + '[*]Error running AutoSploit!' + Style.RESET_ALL)
      wait()
    elif hg == '9':
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
      except:
        print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
      wait()
    elif keylog == '2':
      try:
        os.system('cp -R KidLogger-setupwin26-11-2017 ~')
        print(Fore.GREEN + '[+]keylogger copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
      wait()
    elif keylog == '3':
      try:
        os.system('cp -R staffcounter_install ~')
        print(Fore.GREEN + '[+]keylogger copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]keylogger not found!' + Style.RESET_ALL)
      wait()
    elif keylog == '4':
      wait()
  elif in_put == '7':
    os.chdir('digis')
    print(os.getcwd())
    os.system('sudo ./convert.sh')
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
      except:
        print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
      wait()
    elif exploit == '2':
      try:
        os.system('cp -R unplug.sh ~')
        print(Fore.GREEN + '[+]exploit copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
      wait()
    elif exploit == '3':
      try:
        os.system('cp -R Cisco_E4200_vuln.py ~')
        print(Fore.GREEN + '[+]exploit copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]exploit not found!' + Style.RESET_ALL)
      wait()
    elif exploit == '4':
      wait()
  elif in_put == '9':
    print(Fore.CYAN + "[*]Enter 'q' to exit")
    print("[*]SSH syntax = ssh -i RSA_KEY uname@ip -p port" + Style.RESET_ALL)
    def recursion():
      in_put = input(os.getcwd() + ': ')
      if in_put == 'q':
        wait()
        home()
      else:
        os.system(in_put)
        recursion()
    recursion()
  elif in_put == '10':
    os.system('tor')
    wait()
  elif in_put == '11':
    print(Fore.CYAN + "[*]Enter 'q' to exit")
    print("[*]Nmap syntax = nmap [options] rhost" + Style.RESET_ALL)
    def recursion():
      in_put = input(os.getcwd() + ': ')
      if in_put == 'q':
        wait()
        home()
      else:
        os.system(in_put)
      recursion()
    recursion()
  elif in_put == '12':
    print('[1] netcat')
    print('[2] cryptcat (more secure but requires cryptcat on other end)')
    noc = input(': ')
    if noc == '1':
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Netcat syntax = nc rhost -l (listener) -v (verbose) -p (port to connect to or listen on)" + Style.RESET_ALL)
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
          recursion()
      recursion()
    elif noc == '2':
      print(Fore.CYAN + "[*]Enter 'q' to exit")
      print("[*]Cryptcat syntax = cryptcat rhost -l (listener) -v (verbose) -p (port to connect to or listen on)" + Style.RESET_ALL)
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
          recursion()
      recursion()
  elif in_put == '13':
    os.chdir('phishing')
    print('[1] sonar.py - batch email sender')
    print('[2] go home')
    phish = input(': ')
    if phish == '1':
      try:
        os.system('python3 sonar.py')
      except:
        print(Fore.RED + '[*]sonar.py not found!' + Style.RESET_ALL)
      wait()
    elif phish == '2':
      wait()
  elif in_put == '14':
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
      except:
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
      wait()
    if image == '2':
      try:
        os.system('cp -R kali-linux-2019.2-vmware-amd64.7z ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
      wait()
    if image == '3':
      try:
        os.system('cp -R en_windows_10_x64_dvd.iso ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
      wait()
    if image == '4':
      try:
        os.system('cp -R en_windows_8_1_x64_dvd_2707217.iso ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
      wait()
    if image == '5':
      try:
        os.system('cp -R en_windows_7_Ult_64Bit.iso ~')
        print(Fore.GREEN + '[+]image copied to r00t!' + Style.RESET_ALL)
      except:
        print(Fore.RED + '[*]image not found!' + Style.RESET_ALL)
      wait()
    if image == '6':
      wait()
  elif in_put == '15':
    os.system('sudo ./backup.sh')
    wait()
  elif in_put == '16':
    try:
      os.system('sudo ./packetdump.sh')
      os.system('mv output.pcap ~')
      print(Fore.GREEN + '[+]copied packet capture to r00t!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]packet capture not found!' + Style.RESET_ALL)
    wait()
  elif in_put == '17':
    os.chdir('hg')
    try:
      os.system('python3 domain_sticate.py')
    except:
      print(Fore.RED + '[*]Error in file domain_sticate.sh' + Style.RESET_ALL)
    wait()
  elif in_put == '18':
    os.system('irssi')
    wait()
  elif in_put == '19':
    os.chdir('sdefense')
    print('[1] MAC_changer')
    print('[2] ssh_p0Rt_r@andomizer')
    print('[3] ssh rsa_key generator')
    print('[4] pr0xy router')
    print('[5] ssh_encr7tion')
    print('[6] st@tic IP')
    print('[7] go home')
    rdefense = input(': ')
    if rdefense == '1':
      try:
        os.system('./macchanger.sh')
      except:
        print(Fore.RED + '[*]Error in changing mac address!' + Style.RESET_ALL)
      wait()
    elif rdefense == '2':
      try:
        os.system('./ssh_randomizer.sh')
      except:
        print(Fore.RED + '[*]Error in changing ssh port' + Style.RESET_ALL)
      wait()
    elif rdefense == '3':
      try:
        os.system('sudo service ssh start')
        os.system('mkdir /root/.ssh')
        uname = input('Enter username for ssh: ')
        port = input('Enter local ssh port: ')
        print('Leave filepath for keys blank for default')
        os.system('ssh-keygen')
        os.system('ssh-copy-id ' + uname + '@localhost -p ' + port)
        os.system('ssh ' + uname + '@localhost -p ' + port)
        os.system('exit')
        os.system('cp /root/.ssh/id_rsa /root')
        print('RSA Keys Generated and Private Key copied to r00t!')
      except:
        print(Fore.RED + '[*]Error in generating RSA keys!' + Style.RESET_ALL)
      wait() 
    elif rdefense == '4':
      try:
        os.system('./proxy_config.sh')
      except:
        print(Fore.RED + '[*]Error in running proxy_config.sh!' + Style.RESET_ALL)
      wait()
    elif rdefense == '5':
      try:
        os.system('./ssh_encr7pt.sh')
      except:
        print(Fore.RED + '[*]Error in running ssh_encr7pt.sh!' + Style.RESET_ALL)
      wait()
    elif rdefense == '6':
      try:
        os.system('./static_ip.sh')
      except:
        print(Fore.RED + '[*]Error in running static_ip.sh!' + Style.RESET_ALL)
      wait()
    elif rdefense == '7':
      wait()
  elif in_put == '20':
    port = input('Enter port number to listen on: ')
    try:
      print(Fore.GREEN + '[+]Listening on port ' + port + '!' + Style.RESET_ALL)
      os.system('nc -l -p ' + port )
    except:
      print(Fore.RED + '[*]Error listening on port!' + Style.RESET_ALL)
    wait()
  elif in_put == '21':
    try:
      os.chdir('OWASP-ZSC')
      os.system('python zsc.py')
    except:
      print(Fore.RED + '[*]Error Running OWASP-ZSC!' + Style.RESET_ALL)
    wait()
  elif in_put == '22':
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
      wait()
      home()
    elif forensic == '9':
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
  elif in_put == '23':
    try:
      os.system('./bluespoof.sh')
      wait()
    except:
      print(Fore.RED + '[*]Error running bluespoof.sh!' + Style.RESET_ALL)
  elif in_put == '24':
    try:
      os.system('python3 shodan_search.py')
      wait()
    except:
      print(Fore.RED + '[*]Error running shodan_search.py!' + Style.RESET_ALL)
  elif in_put == 'R':
    os.chdir(root)
    os.system('more README.md')
    wait()
  elif in_put == 'L':
    os.chdir(root)
    os.system('more CHANGELOG.md')
    wait() 
  elif in_put == 'X':
    print('Bye Bye')
    exit()
  home()

home()
