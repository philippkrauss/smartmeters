COUNTER=$(cat /home/pi/counter.txt)
TIMESTAMP=$(date +%s)
echo "$TIMESTAMP;$COUNTER"