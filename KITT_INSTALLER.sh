#! /bin/bash
read -p "*RUN AS ROOT*" root
echo "[*]Running lib installer..."
./lib_install.sh
echo "[+]Done!"
echo "[*]Moving KITT directory to /opt..."
mkdir /opt
cd ..
mv KITT /opt
echo "[+]Done!"
echo "[*]Writing KITT directory to PATH..."
export PATH=$PATH:/opt/KITT
echo "[+]Done!"
echo "[*]Appending KITT directory to .bashrc"
echo "export PATH=$PATH:/opt/KITT" >> /root/.bashrc
echo "[+]Done!"
echo 'Execute "KITTexe.sh" to run KITT'

