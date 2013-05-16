#!/usr/bin/python

import sys
import subprocess
import re

p = subprocess.Popen(["whois", sys.argv[1]], stdout=subprocess.PIPE)
output, err = p.communicate()
output = output.splitlines(True)

whoisfields = {}

for line in output:
	match = re.search(r':', line)
	if match:
		k, v = line.split(':', 1)
		v = v.strip()
		whoisfields[k.lower()] = v

print "Country code is " + whoisfields["country"]

