#!/bin/bash

COMMAND='/usr/bin/python /home/pi/gotgymlight.py'
LOGFILE='/home/pi/restart.txt'

writelog() {
  now=`date`
  echo "$now $*" >> $LOGFILE
}

/usr/bin/xset -display ":0" -dpms s noblank s off

/usr/bin/unclutter -display ":0" -idle 0.5 -root &

/bin/sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
/bin/sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

/usr/bin/chromium-browser --process-per-site --noerrdialogs --disable-infobars --kiosk http://192.168.1.235:5050/gym &

writelog "Starting Kiosk..."
while true; do
   # turn display off when gym light is turned off and vis-a-versa
   $COMMAND
   writelog "Restarting..."
done
