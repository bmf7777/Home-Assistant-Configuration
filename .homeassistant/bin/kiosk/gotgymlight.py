#!/usr/bin/env python

import PyISY
import threading
import sys
import os, subprocess, time, datetime
import schedule

NODE = '38 41 28 1'
DISPLAYON="/usr/bin/xset -display ':0' dpms force on"
DISPLAYOFF="/usr/bin/xset -display ':0' dpms force off"
DISABLE_ENERGYSTAR="/usr/bin/xset -display ':0' -dpms"
REFRESH="/usr/bin/xdotool key F5"
ONE_AM="01:00"
LOGFILE="/home/pi/restart.txt"

ADDR="192.168.1.30"
PORT="442"
USER="admin"
PASS="w1213kie"

def notify(e):
  logfile.write("Notification Received at {}\n".format(now))
  logfile.flush()
  node.update()
  if int(node.status) > 0 :
     subprocess.call(DISPLAYON, shell=True)
     subprocess.call(DISABLE_ENERGYSTAR, shell=True)
     logfile.write("Node {} is On at {}\n".format(node.name, now))
     logfile.flush()
  else :
     subprocess.call(DISPLAYOFF, shell=True)
     logfile.write("Node {:} is Off at {}\n".format(node.name, now))
     logfile.flush()

def refresh():
  subprocess.call(REFRESH, shell=True)
  logfile.write("Refreshing browser at {}\n".format(now))
  logfile.flush()

now = datetime.datetime.now()

os.environ['DISPLAY'] = ":0"

logfile = open(LOGFILE, "a+") 
logfile.write("Log file open: {} at {}\n".format(logfile, now))
logfile.flush()

myisy = PyISY.ISY(ADDR, PORT, USER, PASS)
logfile.write("Connected to ISY: {} at {}\n".format(myisy.connected, now))
logfile.flush()

# refresh display once a day
schedule.every().day.at(ONE_AM).do(refresh)

# Enable callbacks from ISY
myisy.auto_update = True

node = myisy.nodes[NODE]
logfile.write("Node handle obtained from ISY: {} at {}\n".format(node, now))
logfile.flush()

handler = node.status.subscribe('changed', notify)
logfile.write("Callback established to Node: {} at {}\n".format(handler, now))
logfile.flush()

while True:
  schedule.run_pending()
  time.sleep(5)


