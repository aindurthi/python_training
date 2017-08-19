#!usr/bin/pyhton
import sys
a = {"First Name": "AcharyaTejaswi" ,"Last Name": "Indurthy" , "Phone": "7794029809" ,"First Name": "Acharya" ,"Last Name": "Indu" , "Phone": "77940298908"}
if sys.argv[1] in a["First Name"]:
  print a
if sys.argv[1] in a["Last Name"]:
  print a
if sys.argv[1] in a["Phone"]:
  print a
