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
ip=raw_input ("\t\tEnter ip address")
while True:
	print"""
	Press 1: Apache httpd webserver
	Press 2: NFS server
	Press 3: FTP server
	Press 4: SAMBA server
	

	"""
        os.system("tput setaf 5")
	ch=raw_input("what are you thinking?")

	if int(ch)==1:
         os.system("tput setaf 2")
         commands.getoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root systemctl stop firewalld".format(ip))
	 status=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root rpm -q httpd".format(ip))
         if(status[0]==0):
           print "httpd is already installed"
         else:
           yumstatus=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root yum install httpd -y".format(ip))
           if (yumstatus[0]==0):
    	     print "httpd installed"
           else:
              print "Something goes wrong with installation....."
         servicestatus=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root systemctl restart httpd".format(ip))
         if(servicestatus[0]==0):
            print "Apache service activated"
         else:
            print "Service yet not started"
         
         scpstatus=commands.getstatusoutput("sshpass -p redhat sudo scp -o stricthostkeychecking=no  /root/welcome.html {}:/var/www/html/".format(ip))
         if(scpstatus[0]==0):
            print "httpd webserver is deployed"
         else:
            print "Error while deploying webpages......"
         
        


	elif int(ch)==2:
         os.system("tput setaf 5")
         commands.getoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root systemctl stop firewalld".format(ip))
	 status=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root rpm -q nfs-utils".format(ip))
         if(status[0]==0):
           print "nfs-utils is already installed"
         else:
           yumstatus=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root yum install nfs-utils -y".format(ip))
           if (yumstatus[0]==0):
    	     print "nfs-utils get installed"
           else:
              print "Package not installed"
	 dir=raw_input("enter directory name")
         dirstatus=commands.getstatusoutput("sshpass -p redhat ssh {0} -o stricthostkeychecking=no -l root mkdir /{1}".format(ip,dir))
         if (dirstatus[0]==0):
    	      print "directory created"
         else:
              print "directory not created"
         sip=raw_input("enter ip where you want to share")
         f=open("/etc/exports",'w')
         f.write("/{0}\t\t\t\t{1}(sync,rw)".format(dir,sip))
         f.close()
	 configuredstatus=commands.getstatusoutput("sshpass -p redhat sudo scp -o stricthostkeychecking=no  /etc/exports  {}:/etc/".format(ip))
         if (configuredstatus[0]==0):
    	      print "NFS configured"
         else:
              print "NFS is not configured"
         
        
         servicestatus=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root systemctl restart nfs".format(ip))
         if(servicestatus[0]==0):
            print "nfs service Activated"
         else:
            print "service yet not started"
         
         servicestatus=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root mount {}:/{} /var/www/html".format(sip,ip,dir))
         if(servicestatus[0]==0):
            print "NFS server is ready to use"
         else:
            print "Mount operation failed...."
         
 	 		
 	 
	elif int(ch)==3:
         os.system("tput setaf 6")
	 commands.getoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root systemctl stop firewalld".format(ip))
	 status=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root rpm -q vsftpd".format(ip))
         if(status[0]==0):
           print "vsftpd is already installed"
         else:
           yumstatus=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root yum install vsftpd -y".format(ip))
           if (yumstatus[0]==0):
    	     print "vsftpd get installed"
           else:
              print "vsftpd is not installed"
	 servicestatus=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root systemctl restart vsftpd".format(ip))
         if(servicestatus[0]==0):
            print "vsftpd service activated"
         else:
            print "service yet not started"
         print "Press 1: Want to operate via known-users"
         print "Press 2: Want to operate via Root"
         ch1=raw_input()
         if int(ch1)==1:
          configuredstatus=commands.getstatusoutput("sshpass -p redhat sudo scp -o stricthostkeychecking=no  /temp/vsftpd.conf  {}:/etc/vsftpd/".format(ip))
          if (configuredstatus[0]==0):
    	      print "FTP files are configured"
          else:
              print "error while configuring"
         elif int(ch1)==2:
          configuredstatus1=commands.getstatusoutput("sshpass -p redhat sudo scp -o stricthostkeychecking=no  /temp/ftpusers  {}:/etc/vsftpd/".format(ip))
          if (configuredstatus1[0]==0):
    	      print "FTP files are configured"
          else:
              print "error while configuring"
          configuredstatus2=commands.getstatusoutput("sshpass -p redhat sudo scp -o stricthostkeychecking=no  /temp/user_list  {}:/etc/vsftpd/".format(ip))
          if (configuredstatus2[0]==0):
    	      print "FTP files are configured"
          else:
              print "error while configuring"
         else:
          print "wrong choice"  

	elif int(ch)==4:
         os.system("tput setaf 3")
	 commands.getoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root systemctl stop firewalld".format(ip))
	 status=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root rpm -q samba".format(ip))
         if(status[0]==0):
           print "samba is already installed"
         else:
           yumstatus=commands.getstatusoutput("sshpass -p redhat ssh {} -o stricthostkeychecking=no -l root yum install samba -y".format(ip))
           if (yumstatus[0]==0):
    	     print "samba get installed"
           else:
              print "samba package not installed"
         user=raw_input("enter userName")
         Dir=raw_input("enter directory Name")
         dirstatus=commands.getstatusoutput("sshpass -p redhat ssh {0} -o stricthostkeychecking=no -l root mkdir /{1}".format(ip,Dir))
         if (dirstatus[0]==0):
    	      print "directory created"
         else:
              print "directory not created"
         Userstatus=commands.getstatusoutput("sshpass -p redhat ssh {0} -o stricthostkeychecking=no -l root useradd {1}".format(ip,user))
         if (dirstatus[0]==0):
    	      print "usercreated "
         else:
              print "User not created"
         perstatus=commands.getstatusoutput("sshpass -p redhat ssh {0} -o stricthostkeychecking=no -l root chmod 777 /{1}".format(ip,Dir))
         if (perstatus[0]==0):
    	      print "Permission Granted "
         else:
              print "Permission Denied"
         f=open("/etc/samba/smb.conf",'a')
         f.write("\n[sharename]\nPath=/{0}\nHosts\tallow=192.168.0.0/24\nValid\tusers={1}\nPublic=no\nWritable=no".format(Dir,user))
         f.close()
         configuredstatus3=commands.getstatusoutput("sshpass -p redhat sudo scp -o stricthostkeychecking=no  /etc/samba/smb.conf  {}:/etc/samba/".format(ip))
         if (configuredstatus3[0]==0):
    	      print "samba is configured"
         else:
              print "not configured"
         print("Enter password two times")
         sambauser=commands.getstatusoutput("sshpass -p redhat ssh {0} -o stricthostkeychecking=no  -l root smbpasswd -s -a {1}".format(ip,user))
         if (sambauser[0]==0):
    	      print "user added successfully into samba"
         else:
              print "no user added"
         
         servicestatus=commands.getstatusoutput("sshpass -p redhat ssh {0} -o stricthostkeychecking=no  -l root service smb restart".format(ip))
         if (servicestatus[0]==0):
    	      print "samba service activated"
         else:
              print "service failed"
        else:
         exit()
 
          

         




