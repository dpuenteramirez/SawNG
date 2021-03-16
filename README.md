# SawNG AKA Sherlock and Watson Next Gen
Sherlock and Watson exploit check again Windows exploit suggester (wes) NG
This project is a simple python script that filters the output from wesNG to show only privilege escalation CVEs which sherlock and watson look for. 

# Rationale
This script was made becuase sherlock required python 2 which kali dropped support for in 2020 and becuase watson can only be used against specific windows builds.
This meant that I was no able to use Sherlock or Watson in my hunt for Windows PrivEsc vectors since I was pen testing an unpatched windows server r2 2012 using 2020 Kali Linux.
Additionally using windows exploit suggestor alone gave me way too much output for it to be of any use so this script pretty much saved the day.

# Useage
The files in this repo should be placed in the root directory of windows exploit suggester NG

1) First clone/download the windows exploit suggester ng from https://github.com/bitsadmin/wesng

Next run windows exploit suggester and pipe the output to wesOutput like so:
For Linux
`python3 wes.py /home/kali/HTB/Optimum/sysinfo.txt > wesOutput.txt`
For Windows
TODO

2) Next run this script like so: 
`python3 SawNG.py` 
