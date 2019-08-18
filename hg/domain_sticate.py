#! python3
import os
from colorama import Fore, Back, Style

def wait():
  wait = input("PRESS ENTER TO CONTINUE")

def main():
  os.system("figlet -f slant 'domain_sticate'")
  print('=========================================================================')
  domain = input(Fore.CYAN + '[*]Enter domain to investigate(domain.ext): ' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Pinging domain...' + Style.RESET_ALL)
  try:
    os.system('ping -c 4 ' + domain + ' > outputs/ping.txt')
    print(Fore.GREEN + '[+]Domain reached!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Domain not responding!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of Ping directed to ping.txt!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running full nmap scan of domain...' + Style.RESET_ALL)
  try:
    os.system('nmap -sV -A -p 0-65535 ' + domain + ' > outputs/nmap.txt')
    print(Fore.GREEN + '[+]Scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + "[*]Scan incomplete!" + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of nmap scan directed to nmap.txt!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running dig nameserver scan on domain...' + Style.RESET_ALL)
  try:
    os.system('dig ' + domain + ' ns > outputs/dig.txt')
    print(Fore.GREEN + '[+]Nameserver scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Nameserver scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of dig scan directed to dig.txt!' + Style.RESET_ALL)
  os.system('cd theHarvester')
  print(Fore.RED +'[*]:WARNING: Once you run this, google will read your pings as a DDoS attack and block your IP temporarily!' + Style.RESET_ALL)
  wait()
  print(Fore.CYAN + "[*]Running harvester scan..." + Style.RESET_ALL)
  try:
    os.system('python3.7 theHarvester.py -d ' + domain + ' -l 200 -b google -s -g -p -f ../outputs/output.html > ../outputs/harvest.txt')
    print(Fore.GREEN + '[+]Harvester scan complete!')
  except:
    print(Fore.RED + '[*]Harvester scan incomplete!')
  print(Fore.CYAN + '[*]Output of theHarvester directed to harvest.txt!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running cewl wordlist scan...' + Style.RESET_ALL)
  try:
    os.system('cewl -w ../outputs/domain_wordlist.lst -d 7 -m 5 https://www.' + domain)
    print(Fore.GREEN + '[+]Cewl wordlist scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Cewl wordlist scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of Cewl directed to domain_wordlist.lst!' + Style.RESET_ALL)
  os.system('cd ../JoomlaScan')
  print(Fore.CYAN + '[*]Running joomlascan...' + Style.RESET_ALL)
  try:
    os.system('python joomlascan.py -u https://www.' + domain + ' > ../outputs/joomla.txt')
    print(Fore.GREEN + '[+]Joomla Scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Joomla Scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of JoomlaScan directed to joomla.txt!' + Style.RESET_ALL)
  os.system('cd ..')
  print(Fore.CYAN + '[*]Running email index on domain...' + Style.RESET_ALL)
  try:
    os.system('./goog-mail.py ' + domain + ' > outputs/domain_emails.txt')
    print(Fore.GREEN + '[+]Email index complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Email index incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of goog-mail scan directed to domain_emails.txt!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running shodan search on domain...' + Style.RESET_ALL)
  try:
    os.system('shodan search --fields ip_str,port,org,hostnames ' + domain  + ' > shodan.txt')
    print(Fore.GREEN + '[+]Shodan search complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Shodan search incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of shodan scan directed to shodan.txt!' + Style.RESET_ALL)
  print('=========================================================================')
  print(Fore.GREEN + '[+]Domainstication Complete!' + Style.RESET_ALL)
  wait()

ins = input(Fore.CYAN + '[*]Did you run lib_install.sh?[y/N]: ' + Style.RESET_ALL)
if ins == 'y' or ins == 'Y':
  wait()
  main()
else:
  print(Fore.RED + '[*]Please run lib_install.sh or KITT_INSTALLER.sh first...' + Style.RESET_ALL)
  wait()
  exit()
