#!/usr/bin/env python   

import os
import socket
import getpass
import sys

#get the device name
deviceName = str(sys.argv[1])
#get the IP
nodeIP = str(sys.argv[2])
#subprocess.call(["./netdummy.sh",deviceName,serverIP])
#Ingresar host
host = str(sys.argv[3])
#Ingresar password

print 'Iniciando el nodo'
#check if node file exists if not create it.
if not os.path.isfile('/home/SOROOT/nodo'+'.info') :
     open(('/home/SOROOT/nodo'+host+'.info'),'w').close()
     print 'node file didnt existed, creating empty file'
infile = open('/home/SOROOT/nodo'+host+'.info','a')
print (host,' Ingrese su contrasena')
passw = getpass.getpass()
infile.write(nodeIP)
infile.write(" ")
infile.write(host)
infile.write(" ")
infile.write(passw)
infile.write('\n')

infile.close()

