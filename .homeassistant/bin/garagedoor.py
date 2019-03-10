#!/usr/bin/python

import ISY
import sys

garagedoor_isy = 'Garage_Entry'
myisy = ISY.Isy(addr="192.168.1.30:442", userl="admin", userp="w1213kie")

if len(sys.argv) == 2:
  if sys.argv[1] == 'On':
    myisy.var_set_value(garagedoor_isy, '1')
  elif sys.argv[1] == 'Off':
    myisy.var_set_value(garagedoor_isy, '0')
  else:
    print "Error: incorrect argument value: ", str(sys.argv[1])
else:
  print "Error: incorrect number of arguments: ",  str(sys.argv)

#print myisy.var_get_value(garagedoor_isy)



