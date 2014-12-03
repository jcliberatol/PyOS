#!/usr/bin/env python
import os , sys , getopt, subprocess , paramiko , csv
#executes a remote process in a node
def execute(channel, command):
    command = 'echo $$; exec ' + command
    stdin, stdout, stderr = channel.exec_command(command)
    pid = int(stdout.readline())
    return pid, stdin, stdout, stderr
def getNode(nodeID):
    ip=''
    usr=''
    psw=''
    with open(SOROOT+nodelist, 'rb') as f:
      reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
      for row in reader:
        nid = row[0]
        if int(nid) == nodeID :  
          ip = row[1]
          usr = row[2]
          psw = row[3]
    return ip , usr , psw
#Things to do
SOROOT = "/home/SOROOT"
nodelist = "/nodes.list"
loglist = "/processes.log"
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
    #check if log file exists if not create it.
    if not os.path.isfile(SOROOT+loglist) :
      open((SOROOT+loglist),'w').close()
      print 'process log file didnt existed, creating empty file'
    print 'executing a command'
    #execute a command in a node (args are : exec nodeID commands)
    if str(sys.argv[2])== 'node':
      print 'executing a command in a node'
      
      #we have to do this for a specific node in the network
      nodeID = sys.argv[3]
      #get the node essentials
      nodeIP , user , pwd = getNode(nodeID)
      #Print the node IP
      print "node IP : ", nodeIP , "user : " , user
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(nodeIP,username=user,password=pwd)
      cmd = str(sys.argv[4:len(sys.argv)])
      cmd2 = ''
      for argument in sys.argv[4:len(sys.argv)]:
        cmd2+=' '
        cmd2+=str(argument)
      print cmd2
      cpid , stdin, stdout, stderr = execute(ssh,cmd2)
      for line in stdout.readlines():
        print line,
      ssh.close()
      #Register in the log
      with open(SOROOT+loglist, 'a') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow([cpid,str(sys.argv[4:len(sys.argv)]),nodeIP])
      
    #execute a command in all nodes (args are : exec all commands)
    elif str(sys.argv[2])== 'all':
      print 'executing a command in all nodes'
      
      #Number of nodes
      num_nodes = sum(1 for line in open(SOROOT+nodelist))
      print num_nodes , "nodes"
      for  i in range (num_nodes) :
        nodeID = i+1
        #get the node essentials
        nodeIP , user , pwd = getNode(nodeID)
        #Print the node IP
        print "node IP : ", nodeIP , "user : " , user
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(nodeIP,username=user,password=pwd)
        cmd = str(sys.argv[3:len(sys.argv)])
        cmd2 = ''
        for argument in sys.argv[3:len(sys.argv)]:
          cmd2+=' '
          cmd2+=str(argument)
        cpid , stdin, stdout, stderr = execute(ssh,cmd2)
        for line in stdout.readlines():
          print line,
        ssh.close()
        #Register in the log
        with open(SOROOT+loglist, 'a') as f:
          writer = csv.writer(f, delimiter=' ')
          writer.writerow([cpid,str(sys.argv[3:len(sys.argv)]),nodeIP])
    #execute a command in the server (args are : exec commands)
    else :
      print 'command : ' , str(sys.argv[2])
      #executes a command
      process = subprocess.Popen(sys.argv[2:len(sys.argv)])
      #Now add the pid and command to the server log
      with open(SOROOT+loglist, 'a') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow([process.pid,str(sys.argv[2:len(sys.argv)]),"server"])
  
  #show server processes (args are : allprocs this)
  if str(sys.argv[1])== 'allprocs':
    print 'Processes mode'
    with open(SOROOT+loglist, 'rb') as f:
      reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
      for row in reader:
        print row
#Non correct usage or help
else:
  print 'No arguments given, please give an argument'
  print 'Posible Arguments : '
  print 'start devicename IP : starts the server with this devicename and IP'
  print 'addnode  : Add a new node with a .info file'
  print 'exec : executes a tast or command in a nod or all the nodes or in the server'
  print 'allprocs : watches all the proceses ever executed'
  print 'nodePrint : list all the nodes'