#!/usr/bin/env python3.9

import time
import datetime
import cgi, cgitb 

# Find code directory relative to our directory in directory 'lib'
from os.path import dirname, abspath, join
import sys
sys.path.append(abspath(join(dirname(__file__), 'lib')))

import mypi


print("Content-type: text/html")
print("\n")
print("<html><pre>")

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
counter_str = form.getvalue('counter')
if counter_str == None:
    counter=100000
else:
    counter=int(counter_str)

#timing=mypi.calcpi(counter)
time_start=time.time_ns()
distribution=mypi.calcpi(counter)
time_end=time.time_ns()

print("Total time: %s to %s = %s seconds\n" %(datetime.datetime.fromtimestamp(time_start/1e9).strftime('%Y-%m-%dT%H:%M:%S.%f'),
                                              datetime.datetime.fromtimestamp(time_end/1e9).strftime('%Y-%m-%dT%H:%M:%S.%f'),
                                              (time_end-time_start)/1e9))

print("Loop timing distribution in MICRO-seconds:")
print("microsec\ttimes")
for key,value in sorted(distribution.items()):
    print("%i\t%s" %(key, value))
print("</pre></html>")
