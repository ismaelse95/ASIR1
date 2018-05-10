# Comandos Powershell

Para instalar paquetes.

~~~
install-module -Name (nombremodulo) -Repository PSGallery
~~~

Para ver los modulos.

~~~
Get-Module
~~~

Ver modulos disponibles en el sistema.

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
Get-Chliditem
~~~

Instalar sysinternals

~~~
Install-Package -Name sysinternals -Provider chocolatey
~~~

Importar un modulo, creando una sesión con active directory.

~~~
import-module -pssession $S -name Activedirectory
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

Conectar a la carpeta creada y compartida.

~~~
M:\>net use M: \\Ise22016\prueba /user:SANTIAGO\usuario2
~~~

Crear fichero para las politicas que tienes ya en tu equipo.

~~~
gpresult.exe -h politcas.html
~~~

## NFS Y SAMBA

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

En la máquina cliente, tendremos que poner la ip del servidor junto con el siguiente comando:

~~~
showmount -e 10.0.0.11
~~~

Para conectarse desde el cliente:

~~~
mount -t nfs 10.0.0.11:/compartida/debian /mnt/
~~~


