#!/usr/bin/env python
import os , sys , getopt, subprocess , paramiko , csv

#Things to do
SOROOT = "/home/SOROOT"
if len(sys.argv)>1 :
  #start network of server (args are : start)
  if str(sys.argv[1])== 'start':
    print 'starting the server'
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
    host = ''
    user = ''
    passw = ''
    with open('nodes/nodeexample.info', 'rb') as f:
      reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
      for row in reader:
        host = row[0]
        user = row[1]
        passw = row[2]
    print 'user is : ' , user
    print 'host is : ' , host
    #check if nodes file exists if not create it.
    if not os.path.isfile(SOROOT+'/nodes.list') :
      open((SOROOT+'/nodes.list'),'w').close()
      print 'nodes file didnt existed, creating empty file'
    #Now write the node to the nodes.list
    lastID = 0
    repeatedNode = False
    with open((SOROOT+'/nodes.list'), 'rb') as f:
      reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
      for row in reader:
        lastID = int(row[0])
        if host == row[1] :
          print 'Repeated host , not registering node'
          repeatedNode = True
    
    #If node is not repeated then register it as a new node
    if not repeatedNode:  
      with open(SOROOT+'/nodes.list', 'a') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow([lastID+1,host,user,passw])
        print 'Registered a new node, nodeID : ', lastID+1
    else :
      print 'Node already registered as a node, nodeID : ' , lastID
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
  print 'Posible Arguments : '
  print 'start devicename IP : starts the server with this devicename and IP'
  print 'addnode  : Add a new node with a .info file'
  print 'exec : executes a tast or command in a nod or all the nodes or in the server'
  print 'allprocs : watches all the proceses'
  print 'nodePrint : list all the nodes'