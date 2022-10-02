VALUE=$(/usr/local/sbin/uh50.py | grep "6.8(" | sed -n "s/6.8(\([0-9][0-9]*\).*/\1/p")
/home/pi/waerme-influx.py $VALUE