#!/bin/bash

COMMAND='/home/pi/monitorgymlight.py'
LOGFILE='/home/pi/restart.txt'

writelog() {
  now=`date`
  echo "$now $*" >> $LOGFILE
}

/usr/bin/xset s noblank
/usr/bin/xset s off
/usr/bin/xset -dpms

/usr/bin/unclutter -idle 0.5 -root &

/bin/sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
/bin/sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

/usr/bin/chromium-browser --process-per-site --noerrdialogs --disable-infobars --kiosk http://192.168.1.235:5050/gym &

writelog "Starting"
while true ; do
  $COMMAND
  writelog "Exited with status $?"
  writelog "Restarting"
done


