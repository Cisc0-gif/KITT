#! /bin/bash

echo '[*]Starting Library Installation...'
echo '[*]Updating and Upgrading Packages...'
sudo apt-get update && sudo apt-get upgrade
echo '[*]Installing Linux Packages...'
sudo apt-get install figlet
sudo apt-get install metasploit-framework
sudo apt-get install hydra
sudo apt-get install burpsuite
sudo apt-get install tor
sudo apt-get install nmap
sudo apt-get install cryptcat
sudo apt-get install python
sudo apt-get install python-pip
sudo apt-get install maltegoce
sudo apt-get install recon-ng
sudo apt-get install cewl
sudo apt-get install crunch
sudo apt-get install tcpdump
sudo apt-get install irssi
sudo apt-get install telnet
sudo apt-get install ftp
sudo apt-get install git
sudo apt-get install apache2
sudo apt-get install ssh
sudo apt-get install strace
sudo apt-get install gdb
sudo apt-get install radare2
sudo apt-get install xxd
sudo apt-get install coreutils
sudo apt-get install exiftool
sudo apt-get install steghide
sudo apt-get install proxychains
sudo apt-get install p7zip
sudo apt-get install macchanger
sudo apt-get install hddtemp
sudo apt-get install lm-sensors
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install postgresql
sudo apt-get install kali-linux-full
sudo apt-get install btscanner
sudo apt-get install bluelog
sudo apt-get install redfang
sudo apt-get install bluesnarfer
sudo apt-get install spooftooph
sudo apt-get install ntfs-3g
sudo apt-get install cifs.utils
sudo apt-get install mount
sudo apt-get install dsniffer
sudo apt-get install reaver
sudo apt-get install aircrack-ng
sudo apt-get install libcurl4-openssl-dev libpcap0.8-dev zlib1g-dev libssl-dev
sudo apt-get install john
sudo apt-get install snort
echo '[*]Running make and install for hashcat, hcxdumptool, and hcxtools...'
cd crackers/hashcat
make
make install
cd ..
cd hcxdumptool
make
make install
cd ..
cd hcxtools
make
make install
cd ../..
echo '[*]Starting postgresql main cluster...'
pg_ctlcluster 11 main start
echo '[*]Initiating YAML database for metasploit-framework...'
msfdb init
echo '[*]Installing python2.7 and 3.7 libraries...'
pip install bs4
pip install requests
pip install psutil
pip install httplib
pip install scapy
pip install wsgiref
pip3 install shodan
pip3 install datetime
pip3 install pytz
pip3 install colorama
echo '[*]Writing Custom IRC ruby script to /usr/share/metasploit-framework/data/exploits/psnuffle...'
echo "
class SnifferIRC < BaseProtocolParser

  def register_sigs
    self.sigs = {
      :user => /^(NICKs+[^n]+)/si,
      :pass => /b(IDENTIFYs+[^n]+)/si,
    }
  end

  def parse(pkt)
    return unless pkt.is_tcp?
    return if (pkt.tcp_sport != 6667 and pkt.tcp_dport != 6667)
    s = find_session((pkt.tcp_sport == 6667) ? get_session_src(pkt) : get_session_dst(pkt))
    s[:sname] ||= "irc"

    self.sigs.each_key do |k|
      matched = nil
      matches = nil

      if(pkt.payload =~ self.sigs[k])
        matched = k
        matches = $1
      end

      case matched

      when :login_fail
        if(s[:user] and s[:pass])
          report_auth_info(s.merge({:active => false}))
          print_status("Failed IRC Login: #{s[:session]} >> #{s[:user]} / #{s[:pass]}")

          s[:pass] = ""
          return
        end

      when :login_pass
        if(s[:user] and s[:pass])
          report_auth_info(s)
          print_status("Successful IRC Login: #{s[:session]} >> #{s[:user]} / #{s[:pass]}")
          sessions.delete(s[:session])
          return
        end

      when :banner
        if not (s[:info])
          s[:info] = matches
          report_service(s)
        end

      when :bye
        sessions.delete(s[:session])

      when nil
      else
        sessions[s[:session]].merge!({k => matches})
      end

    end
  end
end
" > /usr/share/metasploit-framework/data/exploits/psnuffle/irc.rb
echo '[*]Writing dynamic proxychain to proxychain config...'
echo "
# proxychains.conf  VER 3.1
#
#        HTTP, SOCKS4, SOCKS5 tunneling proxifier with DNS.
#	

# The option below identifies how the ProxyList is treated.
# only one option should be uncommented at time,
# otherwise the last appearing option will be accepted
#
dynamic_chain
#
# Dynamic - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# at least one proxy must be online to play in chain
# (dead proxies are skipped)
# otherwise EINTR is returned to the app
#
#strict_chain
#
# Strict - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# all proxies must be online to play in chain
# otherwise EINTR is returned to the app
#
#random_chain
#
# Random - Each connection will be done via random proxy
# (or proxy chain, see  chain_len) from the list.
# this option is good to test your IDS :)

# Make sense only if random_chain
#chain_len = 2

# Quiet mode (no output from library)
#quiet_mode

# Proxy DNS requests - no leak for DNS data
proxy_dns 

# Some timeouts in milliseconds
tcp_read_time_out 15000
tcp_connect_time_out 8000

# ProxyList format
#       type  host  port [user pass]
#       (values separated by 'tab' or 'blank')
#
#
#        Examples:
#
#            	socks5	192.168.67.78	1080	lamer	secret
#		http	192.168.89.3	8080	justu	hidden
#	 	socks4	192.168.1.49	1080
#	        http	192.168.39.93	8080	
#		
#
#       proxy types: http, socks4, socks5
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
#socks4 	127.0.0.1 9050

http 67.205.171.99 8080
socks4 167.114.79.139 32537
socks4 186.211.185.106 49314
socks4 139.159.47.22 39593
socks4 91.217.96.1 56636
socks4 181.143.214.213 3629
socks4 36.37.214.226 37797
http 51.79.65.157 3128
https 125.165.217.95 8080
https 182.144.141.223 53603
https 202.138.248.123 45229
https 109.86.207.1 46878
https 77.232.186.2 8080
https 171.5.102.251 8080
http  54.180.123.253 8080
http 159.65.168.195 80
socks4 198.50.177.44 44699
socks5 159.203.166.41 1080
" > /etc/proxychains.conf
echo '[*]Installing Sherlock Packages...'
pip3 install beautifulsoup4
pip3 install bs4
pip3 install colorama
pip3 install certifi
pip3 install lxml
pip3 install PySocks
pip3 install requests
pip3 install requests_futures
pip3 install soupsieve
pip3 install stem
pip3 install torrequest
echo '[*]Updating and Upgrading Packages...'
sudo apt-get update && sudo apt-get upgrade
sudo apt autoremove
echo '[+]Library Installation Complete...'
