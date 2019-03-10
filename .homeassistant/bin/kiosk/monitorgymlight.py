#!/usr/bin/python

import ISY
import sys
import os, subprocess, time

polling_delay = 60
os.environ['DISPLAY'] = ":0"
NAME = "Weight Room Light"
DISPLAY_ON = '/usr/bin/xset dpms force on'
DISPLAY_OFF = '/usr/bin/xset dpms force off'	
REFRESH_DISPLAY = '/usr/bin/xdotool key F5'

myisy = ISY.Isy(addr="192.168.1.30:442", userl="admin", userp="w1213kie")

gym_light = myisy.get_node(NAME)
light_was_off = True

while True:
  gym_light.update()
  # if gym light is turn on then unblank display
  if int(gym_light.status) > 0 :
    if light_was_off == True:
      subprocess.call(DISPLAY_ON, shell=True)
      subprocess.call(REFRESH_DISPLAY, shell=True)
      light_was_off = False
      #print "{:} On".format(gym_light.name)
  else :
    if light_was_off == False:
      subprocess.call(DISPLAY_OFF, shell=True)
    light_was_off = True
    #print "{:} Off".format(gym_light.name)

  time.sleep(polling_delay)

