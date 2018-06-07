#!/usr/bin/python2

import os
import getpass
import signal
import commands

def mystop(x,y):
        print "\n Goodbye....."
        exit()

signal.signal(2 , mystop)

os.system("tput setaf 4")
print "\t\t\t\twelcome to my menu !!"
print "\t\t\t\t................."

os.system("tput setaf 1")
while True:
	print"""
	Press 1: display current date & time
	Press 2: to create a file
	Press 3: to create a directory
	Press 4: to logout
        Press 5: to shutdown O.S
        Press 6: to check internet connectivity
        Press 7: to search something on browser
        Press 8: to check all connected ip in network
	

	"""
        os.system("tput setaf 5")
	ch=raw_input("what are you thinking?")

	if int(ch)==1:
           os.system("date")
        
        elif int(ch)==2:
           x=raw_input("enter file name")
           status=commands.getstatusoutput("touch {0}".format(x))
           if(status[0]==0):
                  print "file created"
           else:
                  print "not created try again" 

        elif int(ch)==3:
           y=raw_input("enter directory name")
           status1=commands.getstatusoutput("mkdir /{0}".format(y))
           if(status1[0]==0):
                  print " dir created"
           else:
                  print "not created try again"          
           

        elif int(ch)==4:
           exit()

        elif int(ch)==5:
           os.system("init 0")

        elif int(ch)==6:         
           status2=commands.getstatusoutput("ping google.com")
           if(status2[0]==0):
                  print "internet conn"
           else:
                  print "not created try again" 
  
        elif int(ch)==7:
           commands.getoutput("firefox https://www.google.com")
           

        elif int(ch)==8:
           ip = raw_input("enter ip")
           z=commands.getoutput("nmap -sP {0}-255".format(ip))
           print z
