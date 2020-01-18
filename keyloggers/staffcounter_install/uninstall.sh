#!/bin/bash

function removeDir() {
    if [ -d "$1" ]; then
		echo "Erasing dir: $1"
		rm -rf $1
	fi
}

function removeUserAppFiles() {
	removeDir "$1/.local/share/Rohs/Staffcounter/"
	removeDir "$1/.local/share/Rohos/Staffcounter/"
	removeDir "$1/.local/share/Rohos/staffcounter/"
	removeDir "$1/.local/share/data/Rohs/Staffcounter/"
	removeDir "$1/.local/share/data/Rohos/staffcounter/"
	
	removeDir "$1/.config/Rohos/"
	removeDir "$1/.config/Rohs/"
}

killall staffcounter

rm -rf "/etc/xdg/autostart/staffcounter.desktop"
rm -rf "/usr/share/applications/staffcounter.desktop"
rm -rf "/usr/share/staffcounter"
rm -rf "/usr/bin/staffcounter"
rm -rf "/usr/bin/staffcounter.bin"
rm -rf "/etc/staffcounter/"
rm -rf "/etc/cron.daily/staffcounter_updater.py"

for d in /home/* ; do
    removeUserAppFiles "$d"
done
