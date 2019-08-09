#!/bin/bash

ARCH=`arch`

if [[ $ARCH != "x86_64" ]]; then
	ARCH="i386"
fi

#if [[ -d "bin/$ARCH" ]]; then
#	echo "Wrong architecture: ${ARCH}"
#	exit 1
#fi

killall staffcounter

# setup default config
if [ ! -d "/etc/staffcounter" ]; then
	mkdir /etc/staffcounter/
fi
# default config
cp files/staffcounter.conf /etc/staffcounter/

# copy executable
cp -r "bin/$ARCH/staffcounter" /usr/bin/staffcounter

# autostart
cp files/staffcounter.desktop /usr/share/applications/
cp files/staffcounter.desktop /etc/xdg/autostart/staffcounter.desktop

# resources
if [ -d "/usr/share/staffcounter" ]; then
	rm -rf /usr/share/staffcounter
fi

mkdir /usr/share/staffcounter
cp -r translations /usr/share/staffcounter/

# icon
cp icons/small_logo.png /usr/share/staffcounter/
cp icons/Icon_V4_64x64.png /usr/share/staffcounter/

#VER=`cat /etc/issue | awk '{print $2}'`

#if [[ $VER =~ (12\.04) ]]; then
#	sudo add-apt-repository -y ppa:canonical-qt5-edgers/ubuntu1204-qt5
#	sudo apt-get update
#fi

# install dependencies
apt-get install -y curl xprintidle libqt4-sql-sqlite libqt4-network libqtgui4 rsync libqjson0
