# Comandos Powershell

Para instalar paquetes.

~~~
install-module -Name (nombremodulo) -Repository PSGallery
~~~

Para ver los modulos de la sesión actual.

~~~
Get-Module
~~~

Obtener modulos disponibles en la sesión que sea.

~~~
Get-Module -ListAvaliable
~~~

Para ver donde esta el paquete.

~~~
install-module 
~~~

Para ver de que tipo es ese modulo.

~~~
Get-Command (nombremodulo)
~~~

Comandos que tienen ese modulo.

~~~
Get-Command -Module SshSessions 
~~~

Conexion ssh

~~~
New-SshSession -ComputerName x.x.x.x (ip donde nos queremos conectar) -username debian (Nombre de la máquina a la que nos conectaremos)
~~~

Para ver la conexion.

~~~
Get-SshSession
~~~

Para entrar en la conexion ssh

~~~
Enter-SshSession x.x.x.x (ip donde nos conectamos)
~~~

Instalar un rol.

~~~
install-windowsfeature -name AD-Service-Controller
~~~

Para ver los repositorios.

~~~
Get-PSRepository
~~~

Para encontrar paquetes.

~~~
Find-Package -Name putty -Provider Chocolatey
~~~

Instalar paquete con repositorio que no tenemos.

~~~
Install-Package -Name putty -Provider chocolatey
~~~

Para ver los directorios y los permisos.

~~~
Get-Childitem
~~~

Instalar sysinternals

~~~
Install-Package -Name sysinternals -Provider chocolatey
~~~

Importar un modulo, creando una sesión con active directory.

~~~
import-module -pssession $S -name Activedirectory
~~~

Contar cuantos cmdlet hay en el sistema.

~~~
Get-Command | where-object {$_.commandtype -eq "Cmdlet"} | measure
~~~

Conectar a la carpeta creada y compartida.

~~~
net use M: \\Ise22016\prueba /user:SANTIAGO\usuario2
~~~

Crear fichero para las politicas que tienes ya en tu equipo.

~~~
gpresult.exe -h politcas.html
~~~

Para ver todos los roles instalados y no instalados en nuesro servidor:

~~~
Get-windowsfeature 
~~~

Para ver todos los miembros de los roles.

~~~
Get-windowsfeature | get-member
~~~

Para ver una propiedad del rol solo y ver lo que tenemos instalado y no instalados.

~~~
Get-windowsfeature | where-object {$_.featuretype -eq "Role"}
~~~

Para ver los roles que están instalados.

~~~
Get-windowsfeature | where-object {($_.featuretype -eq "Role") -and ($_.installstate -eq "installed")}
~~~

Para ver un rol en concreto si está instalado.

~~~
Get-WindowsFeature -name NFS-client
~~~

Desinstalar un rol o caracteristica.

~~~
remove-WindowsFeature nfs-client
~~~

Mostrar roles instalados.

~~~
Get-WindowsFeature | where-object {$_.Installed -eq $True} | format-list DisplayName
~~~

Para ver todos los cmdlet que tenemos en el sistema.

~~~
Get-Command | where-object {$_.commandtype -eq "Cmdlet"}
~~~

Muestra todos los cmdlet instalados y por grupo.

~~~
Get-Command -Type Cmdlet | Sort-Object -Property Noun | Format-Table -GroupBy Noun
~~~

Desactivar firewall

~~~
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
~~~

o

~~~
netsh advfirewall set allprofiles state off
~~~

***

Crear una nueva session.

~~~
New-Pssession -computername ise2012.SANTIAGO.local -credential SANTIAGO\Administrator
~~~

Conectar a una session.

~~~
enter-pssession -computername ise2012.SANTIAGO.local -credential SANTIAGO\Administrator
~~~

Cambiar el nombre a la maquina mediante powershell.

~~~
rename-computer -newname nombre -restart
~~~

Para iniciar sesion en cliente al administrador servidor desde remmina.

~~~
Administrator@SANTIAGO.local
~~~

**Requisitos para conectar una máquina a un dominio.**

- DNS: La ip del servidor.
- Firewall.
- La hora tiene que ser la misma.
- Activar el escritorio remoto.

***

## Relación de confianza

Para crear una relacion de confianza tendremos que tener el dns configurado para ello entramos en el administrador del sevidor --> herramientas --> DNS --> ahora daremos click derecho en el nombre del servidor --> propiedades --> pestaña de reenviadores --> añadimos la ip del servidor al que nos queremos conectar.

Ahora nos dirigimos a herramientas de nuevo --> dominio y confiazna de directorio activo --> dentro pulsamos con click derecho en el dominio y pulsamos en propiedades --> y en la pestaña confianza. 

## NFS

Necesitamos en la máquina servidora tener instalado el nfs server:

~~~
apt-get install nfs-kernel-server
~~~

Máquina servidora entrando al fichero /etc/exports, creamos la carpeta antes en mi caso he creado **mkdir -p /comparitda/debian**:

~~~
/compartida/debian 10.0.0.0/24(rw,sync,no_root_squash)
~~~

Necesitamos en la maquina cleinte tener instalado el nfs:

~~~
apt-get install nfs-common
~~~

En la máquina cliente **linux**, tendremos que poner la ip del servidor junto con el siguiente comando:

~~~
showmount -e 10.0.0.11
~~~

Para conectarse desde el cliente:

~~~
mount -t nfs 10.0.0.11:/compartida/debian /mnt/
~~~

***

Ahora pasamos a tener nfs cliente en una máquina windows, para iniciarlo.

~~~
showmount -e 10.0.0.11
~~~

~~~
nfsadmin.exe client start
~~~

Otra manera de iniciar el nfs.

~~~
runas /user:ise2012\Administrator "nfsadmin.exe client start"
~~~

Para conectarse con mount.

~~~
mount 10.0.0.11:/compartida/debian Z:
~~~

Otra forma de conectarnos.

~~~
net use Z: 10.0.0.9:/compartida/debian
~~~

Borrar una unidad de red.

~~~
net use * /delete
~~~

## SAMBA

Paquetes para configurar el servidor samba:

samba, samba-common, cifs-utils, smbclient.

Fichero de configuración:

~~~
nano /etc/samba/smb.conf
~~~

Compartir carpeta dentro de el fichero smb.conf:

~~~
[samba]
  coment = directorio samba
  path = /samba
  guest ok = yes
  #Public = no
  valid users = debian o %S
  browseable = yes 
  read only = no
  create mask = 0775
  directory mask = 0775
~~~

Hay dos servicios de samba que son los siguientes y tienen las siguientes funcionalidades.

~~~
servicio smbd --> servidor smb/cifs
				  automaticación y atenticación
				  fichero e impresion compatibles

servicio nmbd --> Servidor de nombre NetBios
				  Recorrido de recursos
~~~

Para meter un usuario en el grupo samba en debian:

~~~
smbpasswd -a [usuario]
~~~

***

En windows para ver los grupos de trabajo.

~~~
net view /DOMAIN:WORKGROUP
~~~

Para ver medieante la ip:

~~~
net view \\10.0.0.12
~~~

Para conectarse a la carpeta compartida de debian.

~~~
net use m: \\10.0.0.12\samba /user:debian
~~~

***

## Samba

POWERSHELL 

Creacion de usuarios

~~~
new-localuser empleado1
~~~

Para ver los usuarios

~~~
get-localuser
~~~
