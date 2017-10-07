#!/usr/bin/python
import sys
from shutil import copy2
if len(sys.argv) < 1:
   print "Please provide an argument specifying the file containing filenames and target directories!"
   sys.exit(1)
else:
   f = sys.argv[1]
   d = {}
   with open(f) as o:
      for l in o:
         (k, v) = l.split()
         d[k] = v
   for k in d:
      copy2(k, d[k])
   sys.exit(0)


