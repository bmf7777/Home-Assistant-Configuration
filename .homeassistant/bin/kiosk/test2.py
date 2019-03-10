#!/usr/bin/python

import PyISY
import threading
import sys
import os, subprocess, time

NODE = '38 41 28 1'

ADDR="192.168.1.30"
PORT="442"
USER="admin"
PASS="w1213kie"

def notify(e):
  print "Notification Received"
  if node.status :
     print "*Node {:} is On".format(node.name)
  else :
     print "*Node {:} is Off".format(node.name)

myisy = PyISY.ISY(ADDR, PORT, USER, PASS)
print(myisy.connected)

myisy.auto_update = True
node = myisy.nodes[NODE]
handler = node.status.subscribe('changed', notify)

while True:
  time.sleep(1)

