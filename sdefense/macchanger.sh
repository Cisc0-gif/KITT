#! /bin/bash

figlet -f slant 'MAChanger'
echo ================================================================
read -p 'Enter interface to spoof MAC address: ' interface
macchanger -r $interface
echo 'MAC Address spoofed!'
read -p 'PRESS ENTER TO CONTINUE' e

