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
  print('Not a chance pal...')
  exit()

os.system('sudo apt-get update')
os.system('sudo apt-get upgrade')
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
  print('*[X]  Fuck_0ff                                                 *')
  print(Style.RESET_ALL + '================================================================')
  in_put = input(os.getcwd() + ': ')
  nums = ['X', 'R', 'L']
  for i in range(1,24):
    nums.append(str(i))
  if in_put not in nums:
    print('not an option dumbass')
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
      print('Select a dev rooter for use: ')
      dev_rooter = input('')
      os.system('cp ' + dev_rooter + ' ~')
      print('dev_rooter ha$ /bin/ cOpied to r00t!')
    except:
      print('dev_rooter not found!')
    wait()
  elif in_put == '3':
    os.chdir('rootkittens')
    try:
      os.system('ls')
      dev_rooter = input('Select a rootkit for use: ')
      os.system('cp -R ' + dev_rooter + ' ~')
      print('r--tkit has /bin/ cOpied to r00t!')
    except:
      print('rootkit not found!')
      print(os.getcwd())
    wait()
  elif in_put == '4':
    os.chdir('crackers')
    print('[1] hashcat')
    print('[2] append_num')
    print('[3] weB_l0g!n_CR@CKER')
    print('[4] burpsuite')
    print('[5] dec0ders')
    print('[6] crunch')
    print('[7] 7zCracker')
    print('[8] cewl')
    print('[9] B0T_decrypt - :WARNING: Due to extensive wordlist, anon-net may crash under this!')
    print('[10] go home')
    crack = input("So what'll it be?: ")
    if crack == '1':
      os.chdir('hashcat')
      print("run hashcat at your will or type 'q' to exit (can use append_num.py here too")
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
    elif crack == '2':
      os.chdir('hashcat')
      os.system('python3.7 append_num.py')
      wait()
    elif crack == '3':
      os.system('sudo ./weblogin_crack.sh')
      wait()
    elif crack == '4':
      print("Unfortunately we don't support burpsuite...")
      time.sleep(1)
      print("Nah i'm just fuckin with you")
      print("use burpsuite at your will or type 'q' to exit")
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '5':
      with open('decoders.txt', 'r') as f:
        contents = f.read()
      print(contents)
      wait()
    elif crack == '6':
      print("use crunch at your will or type 'q' to exit")
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '7':
      os.chdir('7zip-crack')
      print("To use 7zCracker type ./7zipcrack file.7z wordlist or type 'q' to quit")
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '8':
      print("use cewl at your will or type 'q' to exit")
      def recursion():
        in_put = input(os.getcwd() + ': ')
        if in_put == 'q':
          wait()
          home()
        else:
          os.system(in_put)
        recursion()
      recursion()
    elif crack == '9':
      def recursion():
        message = input("Enter cipher text here or type 'q' to quit: ").lower().split(' ')
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
                print('Decrypted Ciphertext: "' + i + '"')
          wait()
          recursion()

      recursion()
    elif crack == '10':
      wait()
  elif in_put == '5':
    os.chdir('hg')
    print('Welcome to 2/3 of you life...')
    print('[1] JoomlaScan')
    print('[2] theHarvester')
    print('[3] FOCA - Windows')
    print('[4] 0sint_sites')
    print('[5] malteg0')
    print('[6] g00gle dorks')
    print('[7] r#con-ng')
    print('[8] fbi_master')
    print('[9] Aut0Sp!oit')
    print('[10] go home')
    hg = input(os.getcwd() + ': ')
    if hg == '1':
      os.chdir('JoomlaScan')
      print('python2 joomlascan.py --help for help')
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
      print('python3.7 theHarvester.py --help for help')
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
        print('FOCA copied to r00t!')
      except:
        print('FOCA not found!')
      wait()
    elif hg =='4':
      try:
        with open('osint_sites.txt', 'r') as f:
          contents = f.read()
        print(contents)
      except:
        print('osint_sites.txt not found!')
      wait()
    elif hg == '5':
      os.system('maltegoce')
      wait()
    elif hg == '6':
      try:
        with open('dorks.txt', 'r') as f:
          contents = f.read()
        print(contents)
      except:
        print('dorks not found!')
      wait()
    elif hg == '7':
      os.system('recon-ng')
      wait()
    elif hg == '8':
      try:
        os.chdir('fbi-master')
        os.system('python2.7 fbi.py')
      except:
        print('Error in running fbi-master!')
      wait()
    elif hg == '9':
      try:
        os.chdir('AutoSploit')
        os.system('python2 autosploit.py')
      except:
        print('Error running AutoSploit!')
      wait()
    elif hg == '10':
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
        print('keylogger copied to r00t!')
      except:
        print('keylogger not found!')
      wait()
    elif keylog == '2':
      try:
        os.system('cp -R KidLogger-setupwin26-11-2017 ~')
        print('keylogger copied to r00t!')
      except:
        print('keylogger not found!')
      wait()
    elif keylog == '3':
      try:
        os.system('cp -R staffcounter_install ~')
        print('keylogger copied to r00t!')
      except:
        print('keylogger not found!')
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
        print('exploit copied to r00t!')
      except:
        print('exploit not found!')
      wait()
    elif exploit == '2':
      try:
        os.system('cp -R unplug.sh ~')
        print('exploit copied to r00t!')
      except:
        print('exploit not found!')
      wait()
    elif exploit == '3':
      try:
        os.system('cp -R Cisco_E4200_vuln.py ~')
        print('exploit copied to r00t!')
      except:
        print('exploit not found!')
      wait()
    elif exploit == '4':
      wait()
  elif in_put == '9':
    print("Use ssh to your will or type 'q' to exit")
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
    print("Use nmap to your will or type 'q' to exit")
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
      print("use nc to your will or type 'q' to exit")
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
      print("use cryptcat to your will or type 'q' to exit")
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
        os.system('python3.7 sonar.py')
      except:
        print('sonar.py not found!')
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
        print('image copied to r00t!')
      except:
        print('image not found!')
      wait()
    if image == '2':
      try:
        os.system('cp -R kali-linux-2019.2-vmware-amd64.7z ~')
        print('image copied to r00t!')
      except:
        print('image not found!')
      wait()
    if image == '3':
      try:
        os.system('cp -R en_windows_10_x64_dvd.iso ~')
        print('image copied to r00t!')
      except:
        print('image not found!')
      wait()
    if image == '4':
      try:
        os.system('cp -R en_windows_8_1_x64_dvd_2707217.iso ~')
        print('image copied to r00t!')
      except:
        print('image not found!')
      wait()
    if image == '5':
      try:
        os.system('cp -R en_windows_7_Ult_64Bit.iso ~')
        print('image copied to r00t!')
      except:
        print('image not found!')
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
      print('copied packet capture to r00t!')
    except:
      print('packet capture not found!')
    wait()
  elif in_put == '17':
    os.chdir('hg')
    try:
      os.system('sudo ./domain_sticate.sh')
    except:
      print('Error in file domain_sticate.sh')
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
        print('Error in changing mac address!')
      wait()
    elif rdefense == '2':
      try:
        os.system('./ssh_randomizer.sh')
      except:
        print('Error in changing ssh port')
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
        print('Error in generating RSA keys!')
      wait() 
    elif rdefense == '4':
      try:
        os.system('./proxy_config.sh')
      except:
        print('Error in running proxy_config.sh!')
      wait()
    elif rdefense == '5':
      try:
        os.system('./ssh_encr7pt.sh')
      except:
        print('Error in running ssh_encr7pt.sh!')
      wait()
    elif rdefense == '6':
      try:
        os.system('./static_ip.sh')
      except:
        print('Error in running static_ip.sh!')
      wait()
    elif rdefense == '7':
      wait()
  elif in_put == '20':
    port = input('Enter port number to listen on: ')
    try:
      print('Listening on port ' + port + '!')
      os.system('nc -l -p ' + port )
    except:
      print('Error listening on port!')
    wait()
  elif in_put == '21':
    try:
      os.chdir('OWASP-ZSC')
      os.system('python zsc.py')
    except:
      print('Error Running OWASP-ZSC!')
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
    forensic = input(': ')
    if forensic == '1':
      print("Use gdb at will or type 'q' to exit")
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
      print("Use radare2 at will or type 'q' to exit")
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
      print("Use strace at will or type 'q' to exit")
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
      print("Use nano at will or type 'q' to exit")
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
      print("Use sort at will or type 'q' to exit")
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
      print("Use cat & grep at will or type 'q' to exit")
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
      print("Use file at will or type 'q' to exit")
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
      file = input('Enter filename and filepath here (/fp/fn): ')
      os.system('ls -l ' + file)
      wait()
      home()
    elif forensic == '9':
      print("Use exiftool at will or type 'q' to exit")
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
      print("Use steghide at will or type 'q' to exit")
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
      print("Use xxd at will or type 'q' to exit")
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
      print('Error running bluespoof.sh!')
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
