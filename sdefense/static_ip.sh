#! /bin/bash
figlet -f slant ' ST@TIC IP '
echo '=================================================================='
read -p 'Enter desired IP here: ' ip
read -p 'Enter router (gateway) IP here: ' gw
echo "auto eth0
iface eth0 inet static
address $ip/24
gateway $gw" >> /etc/network/interfaces
echo ':SYSTEM: Static IP Set!'
