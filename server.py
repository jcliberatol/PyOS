#!/usr/bin/env python
import os , sys , getopt, subprocess , paramiko

#Things to do
#Print the arguments
print 'Number of arguments:', len(sys.argv), 'arguments.'

if len(sys.argv)>1 :
  #start network of server (args are : start)
  if str(sys.argv[1])== 'start':
    print 'starting the server'
    SOROOT = "/home/SOROOT"
    if not os.path.isdir(SOROOT):
      os.makedirs(SOROOT)
      print "Nuevo servidor en  : " , SOROOT
    else :
      print 'restaurando un servidor viejo en ' , SOROOT
    #Connect to the network
    if len(sys.argv)==4:
      #get the device name
      deviceName = str(sys.argv[2])
      #get the IP
      serverIP = str(sys.argv[3])
      subprocess.call(["./netdummy.sh",deviceName,serverIP])
    else:
      print 'incorrect amount of arguments to start server'
      sys.exit()
  #add a node to the server (args are : addnode node.info)
  if str(sys.argv[1])== 'addnode':
    print 'Adding a new node'
    
  #executing commands
  if str(sys.argv[1])== 'exec':
    print 'executing a command'
    #execute a command in a node (args are : exec nodeID commands)
    if str(sys.argv[2])== 'node':
      print 'executing a command in a node'
    #execute a command in all nodes (args are : exec all commands)
    if str(sys.argv[2])== 'all':
      print 'executing a command'
    #execute a command in the server (args are : exec commands)
    if str(sys.argv[2])== 'command':
      print 'command : '
  
  #show server processes (args are : allprocs this)
  if str(sys.argv[1])== 'allprocs':
    print 'Processes mode'
else:
  print 'No arguments given, please give an argument'