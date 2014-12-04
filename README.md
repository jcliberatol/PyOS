PyOS
====

A distributed python OS Emulator for adhoc networks

##PROYECTO FINAL SISTEMAS OPERATIVOS
UNIVERSIDAD NACIONAL DE COLOMBIA

####PRESENTADO A:
 Joaquín F. Sánchez

####PRESENTADO POR:
* Juan Camilo Liberato
* Camilo Andres Peña
* Santiago Marquez 

##Descripcion : 
Este proyecto genera un programa que permite realizar funciones de un SO para cualquier función. Para iniciar, se ha creado y configurado una red **adhoc** de n equipos, siendo uno de ellos el servidor, quien tiene el programa principal que crea, vincula y desarrolla diferentes funcionalidades y los demás equipos son los clientes

Se desarrolló un programa principal, el cual, al  ejecutarlo nos conecta con la red del servidor,  al conectar le proveemos el nombre del dispositivo, y la IP. Luego vincula los clientes al servidor. En cada cliente hay un programa que al ejecutarse nos guarda en un archivo la IP del equipo, el nombre del equipo, el usuario y la contraseña, archivo que se le pasa al servidor para poder vincular al cliente.
El servidor revisa si el cliente ya existe, si no lo vincula y realiza una función específica para cada nodo de la red, luego de ello puede ejecutar  en todos los clientes las funciones.

## Uso : 
```
'Posible Arguments : '
'start devicename IP : starts the server with this devicename and IP'
'addnode : Add a new node with a .info file'
'exec : executes a tast or command in a nod or all the nodes or in the server'
'allprocs : watches all the proceses ever executed'
'nodePrint : list all the nodes'
```
## Configurar un nodo

```
nodo.py deviceName IP user
```

Los nodos generan archivos .info que deben ser proveidos en una carpeta nodes/ para el servidor. Luego se deben añadir al servidor con el comando addnode

## Ejemplos : 

```
./server.py start wlan0 192.168.0.1  #Comienza un nuevo servidor con la ip seleccionada
./server.py addnode nodosecundario.info #Añade el nodo que genero el archivo .info
./server.py exec node 1 ls #Ejecuta un comando ls en el nodo 1
./server.py exec all apt-get update # Actualizar todos los repositorios de todos los nodos
./server.py nodePrint #Ver los nodos actuales
./nodo.py wlan0 192.168.0.14 pancho  #Inicia un nodo en el computador de pancho, genera nodopancho.info




```
