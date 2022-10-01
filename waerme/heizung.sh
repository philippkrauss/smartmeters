DATUM=$(date +%s)
/usr/local/sbin/uh50.py | grep "6.8(" | sed -n "s/6.8(\([0-9][0-9]*\).*/$DATUM;\1/p" >> /home/pi/heizung.csv