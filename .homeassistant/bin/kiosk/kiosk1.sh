#!/bin/bash

COMMAND='/home/pi/isgymlighton.py'
LOGFILE='/home/pi/restart.txt'

writelog() {
  now=`date`
  echo "$now $*" >> $LOGFILE
}

#xset s noblank
#xset s off
#xset -dpms

#unclutter -idle 0.5 -root &

#sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
#sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

#/usr/bin/chromium-browser --process-per-site --noerrdialogs --disable-infobars --kiosk http://192.168.1.235:5050/gym &

writelog "Starting..."
COUNTER=0 

while true; do
   #  poll light status every minute 
   sleep 1m
   # turn display off when gym light is turned off
   $COMMAND
   COUNTER=$((COUNTER+1))
   # refresh  web browswer every 24 hours
   if [ $COUNTER -eq  1440 ]; then
      /usr/bin/xdotool key F5
      writelog "Refreshing browser"
      COUNTER=0
   fi
done
