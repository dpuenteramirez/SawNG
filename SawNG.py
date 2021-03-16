#!/usr/bin/python3.9

#SawNG AKA Sherlock and Watson Next Gen
#This file (along with privEscVulns.txt) should be placed in the root directory of windows exploit suggester NG
#This script simply filters the output from WESNG to show the privilege escalation CVEs which sherlock and watson look for. 
#This script was made becuase sherlock required python 2 which kali has dropped support for and becuase watson can only be used against certain windows builds.
#This meant that I was unable to use both tools in my hunt for PrivEsc vectors. 
#Using windows exploit suggestor alone gave me way too much output (I was using an unpatched windows server r2 2012)

#WARNING: As the watson codebase is updated with new CVEs that also means that privEscVulns.txt will need updating too

#Useage
#First clone/download the windows exploit suggester ng from https://github.com/bitsadmin/wesng

#Next run windows exploit suggester and pipe the output to wesOutput like so:
#For Linux
#python3 wes.py /home/kali/HTB/Optimum/sysinfo.txt > wesOutput.txt
#For Windows
## TODO  ##

#Next run this script like so: 
#python3 SawNG.py 

import re 

cves = open('./privEscVulns.txt', 'r')
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
ifile = open("wesOutput.txt",'r')

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
