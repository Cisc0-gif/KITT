#! /bin/bash
read -p "*RUN AS ROOT*" root
echo "[*]Writing File Perimissions..."
chmod -R 777 *
echo "[*]Done!"
echo "[*]Running lib installer..."
./lib_install.py
echo "[+]Done!"
echo "[*]Moving KITT directory to /opt..."
mkdir /opt
cd ..
mv KITT /opt
echo "[+]Done!"
#echo "[*]Writing KITT directory to PATH..." #old method
#export PATH=$PATH:/opt/KITT
#echo "[*]Appending KITT directory to .bashrc" #old method
#echo "export PATH=$PATH:/opt/KITT" >> /root/.bashrc
echo "[*]Writing KITT2.py to alias..."
echo "alias KITT2='python3 /opt/KITT/KITT2.py'" >> /root/.bashrc
echo "[+]Done!"
echo 'Type "KITT2" to run KITT Framework'

