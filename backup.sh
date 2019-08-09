#! /bin/bash

figlet -f slant 'dir backup'
echo '=================================================================='=
read -p 'Enter filepath of directory to backup: ' fp
read -p 'Enter destination of backup: ' dest
read -p 'Enter directory name: ' name
tar -zcvf backup.tar.gz $fp$name
mv backup.tar.gz $dest
echo 'Directory backed up and stored in' $dest
read -p 'PRESS ENTER TO CONTINUE' u
