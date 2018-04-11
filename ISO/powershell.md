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

Get-Childitem -Recurse -Inlcude zoomit.exe