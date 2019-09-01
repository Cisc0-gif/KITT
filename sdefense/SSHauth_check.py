import os
import re
from colorama import Fore, Style

def wait():
  wait = input('PRESS ENTER TO CONTINUE')


ssh = input(Fore.CYAN + '[*]Do you have ssh installed?[y/N]: ')
print(Fore.CYAN + '[*]Current Directory: ' + Style.RESET_ALL + os.getcwd())
lst = input(Fore.CYAN + '[*]Enter name of whitelist for good IPs: ' + Style.RESET_ALL)
with open(lst, 'r') as w:
  wips = w.read().splitlines()
if ssh == 'y' or ssh == 'Y':
  os.chdir('/var/log')
  with open('auth.log', 'r') as a:
    contents = a.read()
    ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", contents)
    fips = list(dict.fromkeys(ips))
    for i in wips:
      if i in fips:
        fips.remove(i)
    print(Fore.RED + '[*]Unknown or malicious IPs: ')
    print(fips)
