#! /bin/bash

figlet -f slant 'domain_sticate'
echo '========================================================================='
read -p 'Enter domain to investigate: ' domain
ping -c 4 $domain > outputs/ping.txt
echo 'Output of Ping directed to ping.txt!'
nmap -sV -A $domain > outputs/nmap.txt
echo 'Output of nmap scan directed to nmap.txt'
dig $domain ns > outputs/dig.txt
echo 'Output of dig scan directed to dig.txt!'
cd theHarvester
echo ':WARNING: Once you run this, google will read your pings as a DDoS attack and block your IP temporarily!'
read -p 'PRESS ENTER TO CONTINUE' enter
python3.7 theHarvester.py -d lootcrate.com -l 200 -b google -s -g -p -f ../outputs/output.html > ../outputs/harvest.txt
echo 'Output of theHarvester directed to harvest.txt!'
cewl -w ../outputs/domain_wordlist.lst -d 7 -m 5 https://www.$domain
echo 'Output of Cewl directed to domain_wordlist.lst!'
cd ../JoomlaScan
python2.7 joomlascan.py -u https://www.$domain > ../outputs/joomla.txt
echo 'Output of JoomlaScan directed to joomla.txt!'
cd ..
./goog-mail.py $domain > outputs/domain_emails.txt
echo 'Output of goog-mail scan directed to domain_emails.txt!'
echo '='=======================================================================
read -p 'Domain Investigation complete...' enter


