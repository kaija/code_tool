#!/usr/bin/python

import sys
import shutil

if len(sys.argv) < 2:
    print "file path parameter missing"
    sys.exit(1)

print sys.argv[1]

with open(sys.argv[1]) as file:
    file2 = open(sys.argv[1] + '.bak', 'w+')
    for line in file:
        line = line.rstrip()
        if line:
            file2.write(line + '\n')
        else:
            file2.write('\n')

shutil.move(sys.argv[1] + '.bak', sys.argv[1])
