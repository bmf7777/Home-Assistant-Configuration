#!/usr/bin/python

import ISY
import sys
import os, subprocess, time

os.environ['DISPLAY'] = ":0"

myisy = ISY.Isy(addr="192.168.1.30:442", userl="admin", userp="w1213kie")

gym_light = myisy.get_node("Weight Room Light")
gym_light.update()

if gym_light.formatted == "On"  or int(gym_light.status) > 0 :
  subprocess.call('/usr/bin/xset dpms force on', shell=True)
  #print "{:} On".format(gym_light.name)
else :
  subprocess.call('/usr/bin/xset dpms force off', shell=True)
  #print "{:} Off".format(gym_light.name)



