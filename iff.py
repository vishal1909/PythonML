#!/usr/bin/python2

import os
import webbrowser
import commands

x='''
Press 1:to show the searching on google
Press 2:to show connected ips
  '''

print x
ch=raw_input("enter the choice")
if int(ch)==1:
	
	print  "searching on Google   ..... "
	msg=raw_input("type to search ")
	webbrowser.open_new_tab('https://www.google.com/search?q='+msg)
elif int(ch)==2:
	print "to find the connnected devices"
	z=commands.getoutput("ifconfig enp0s3")
	y=z.split()
	p=y[5]
	ip = raw_input("enter range")
        z=commands.getoutput("nmap -F {0}-255".format(p,ip))
        print z
	
