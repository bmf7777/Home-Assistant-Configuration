#!/usr/bin/python

import ISY
import sys
import os, subprocess, time

polling_delay = 5
os.environ['DISPLAY'] = ":0"
NAME = "Weight Room Light"
DISPLAY_ON = 'echo /usr/bin/xset dpms force on'
DISPLAY_OFF = 'echo /usr/bin/xset dpms force off'	
REFRESH_DISPLAY = '/usr/bin/xdotool key F5'

def callback(*args):
  print "call back"

myisy = ISY.Isy(addr="192.168.1.30:442", userl="admin", userp="w1213kie", eventupdates=1)
myisy.callback_set(NAME, callback, "foo")

gym_light = myisy.get_node(NAME)

while True:
  gym_light.update()
  # if gym light is turn on then unblank display
  if int(gym_light.status) > 0 :
     #subprocess.call(DISPLAY_ON, shell=True)
     print "Node {:} is {:}".format(gym_light.name, gym_light.formatted)
  else :
     #subprocess.call(DISPLAY_OFF, shell=True)
     print "Node {:} is {:}".format(gym_light.name, gym_light.formatted)

  time.sleep(polling_delay)

