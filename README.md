# SawNG AKA Sherlock and Watson Next Gen
A python script to filter the output from [Windows Exploit Suggester Next Gen (WesNG)](https://github.com/bitsadmin/wesng) to show only the Windows PrivEsc CVEs that [Sherlock](https://github.com/rasta-mouse/Sherlock) and [Watson](https://github.com/rasta-mouse/Watson) look for.

# Rationale
This script was made because Sherlock requires Python 2 which Kali dropped support for in 2020 and Watson can only be used against specific Windows builds.
This meant that I was no able to use Sherlock or Watson in my hunt for Windows PrivEsc vectors for the following reasons:
  - I using Kali 2020+ 
  - I was pentesting an unsupported build of Windows Server R2 2012
  
Additionally using Windows Exploit Suggester alone gave me way too much output for it to be of any use so this script pretty much saved the day.

# Usage
The files in this repo should be placed in the root directory of Windows Exploit Suggester NG

1) First clone/download the windows exploit suggester ng from https://github.com/bitsadmin/wesng

2) Next run WesNG and pipe the output to wesOutput.txt like so:

&nbsp;&nbsp;&nbsp;&nbsp;For Linux:

&nbsp;&nbsp;&nbsp;&nbsp;`python3 wes.py YourSystemInfoFile > wesOutput.txt`

&nbsp;&nbsp;&nbsp;&nbsp;For Windows:
  
&nbsp;&nbsp;&nbsp;&nbsp;TODO

3) Finally run this script like so: 
`python3 SawNG.py` 

# WARNING
This project may become outdated as the Watson codebase is updated with new CVEs. Therefore the privEscVulns.txt file will need updating with any new CVEs. The CVEs can be found at https://github.com/rasta-mouse/Watson/blob/master/Watson/VulnerabilityCollection.cs
