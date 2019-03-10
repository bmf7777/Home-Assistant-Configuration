#!/usr/bin/python

# isysetvar VARIABLE VALUE[On|Off]

import ISY
import sys

myisy = ISY.Isy(addr="192.168.1.30:442", userl="admin", userp="w1213kie")

#print str(sys.argv)

if len(sys.argv) == 3:
  isyvar = str(sys.argv[1])
  if sys.argv[2] == 'On':
    myisy.var_set_value(isyvar, '1')
  elif sys.argv[2] == 'Off':
    myisy.var_set_value(isyvar, '0')
  else:
    print "Error: incorrect argument value: ", str(sys.argv[2])
else:
  print "Error: incorrect number of arguments: ",  str(sys.argv)

#print myisy.var_get_value(isyvar)



