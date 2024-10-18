#SawNG AKA Sherlock and Watson Next Gen

#!/usr/bin/python3.9

import re
import sys

cves = open('/opt/wesng/SawNG/privEscVulns.txt', 'r')
Lines = cves.readlines()
output = []
cveList = ""
for cve in Lines:
	cveList = cveList + cve
cveList = cveList.replace("-", "\\-")
cveList = cveList.replace("_", "\\-")

#remove new lines
cveList = cveList.replace('\n','|')

if cveList.endswith("|"):
	cveList = cveList.removesuffix("|")

# Open file as file object and read to string
ifile = open(sys.argv[1], 'r')

# Read file object to string
text = ifile.read()

# Close file object
ifile.close()

#cveList = "CVE-2017-0109"
# Create regex string
reg = r"Date:.*\s.*(?:" + cveList + r")[\s\S.]*?Exploit.*"
# Regex pattern
matches = re.findall(reg, text, re.MULTILINE)

# Add to output if not a duplicate
cvesInOutput = []
for match in matches:
	reg1 = "CVE-\\d*-\\d*"
	cve = re.findall(reg1, match)[0]
	if len(cvesInOutput) > 0 and len(output) > 0:
		if cve not in cvesInOutput and match not in output:
			output.append(match)
			cvesInOutput.append(cve)
	else:
		output = [match]
		cvesInOutput.append(cve)

for item in output:
	print(item + "\n")
