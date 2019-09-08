#! /bin/bash

figlet -f slant 'dir backup'
echo '=================================================================='=
read -p 'Enter filepath of directory to backup(Ex. fp/): ' fp
read -p 'Enter destination of backup(Ex. fp/): ' dest
read -p 'Enter directory name(Ex. name/): ' name
tar -zcvf backup.tar.gz $fp$name
mv backup.tar.gz $dest
echo 'Directory backed up and stored in' $dest
read -p 'PRESS ENTER TO CONTINUE' u
