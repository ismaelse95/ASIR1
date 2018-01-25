# Sistemas de Ficheros.

Para poder ver los discos que tenemos conectado a nuestro dispositivos desde la terminal tecleamos el comando. Todo esto tendremos que hacerlo como root.

~~~
``$ lsblk -f``
~~~

``ola``

Para formatear lo podremos hacer con el comando mkfs, podemos ver los sistemas de archivo que tenemos si en la terminal ponemos mkfs. y tabulamos. En mi caso tengo los siguientes.

~~~
root@debian:/dev/disk# mkfs.
mkfs.bfs     mkfs.ext2    mkfs.ext4    mkfs.ntfs    
mkfs.cramfs  mkfs.ext3    mkfs.minix   mkfs.xfs 
~~~

Si no tenemos instalado algún sistema de archivo estos son algunos paquetes de sistemas de archivo.

~~~
vfat: mkfs.vfat
Instalar paquete dosfstools --> apt-get install dosfstools

ntfs: mkfs.ntfs 	
Instalar paquete ntfs-3g --> apt-get install ntfs-3g

xfs: mkfs.xfs 		
Instalar paquete xfsprogs --> apt-get install xfsprogs
~~~

Para poder dar formato a un dispositivo tendremos que ejecutar el comando.

~~~
mkfs.ext4 /dev/sdb1
~~~

También podemos añadir una etiqueta a nuestro dispositivo cuando le vayamos a dar formato.

~~~
mkfs.ntfs -L PRUEBA /dev/sdb1
~~~

Y con lsblk -f veriamos que tendremos el nombre que hemos seleccionado.

~~~
root@debian:/dev/disk# lsblk -f
NAME   FSTYPE LABEL  UUID                                 MOUNTPOINT
sda                                                       
├─sda1 ext4          e38da17e-18f8-4328-b6d5-cfb141fac35a /
├─sda2                                                    
└─sda5 swap          929c7136-2757-40da-9c1e-1f461be8ce54 [SWAP]
sdb                                                       
├─sdb1 ntfs   PRUEBA 3F754DBF1EC4F41D                     /mnt
└─sdb2 ntfs          5AAC3D434551E37F                     
sr0                                            
~~~

Podemos montar mediante el nombre de etiqueta que ya hemos seleccionado. En mi caso lo he etiquetado con PRUEBA, por lo tanto lo montaria de la siguiente manera.

~~~
root@debian:/dev/disk# mount -L PRUEBA /mnt
~~~

Para montar nuestro disco cuando iniciamos nuestro ordenador tendremos que entrar con un editor de texto en el fichero /etc/fstab.

~~~
root@debian:/# nano /etc/fstab
~~~

Y a continuación en el fichero al final del todo añadiremos el dispositivo que queramos que se inicie en el arranque. El fichero quedaria de la siguiente manera.

~~~
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>

# / was on /dev/sda1 during installation
UUID=e38da17e-18f8-4328-b6d5-cfb141fac35a /               ext4    errors=remount-ro 0       1
# swap was on /dev/sda5 during installation
UUID=929c7136-2757-40da-9c1e-1f461be8ce54 none            swap    sw              0       0
/dev/sr0        /media/cdrom0   udf,iso9660 user,noauto     0       0

/dev/sdb1       /mnt 			 ntfs 		defaults		0		2 		
~~~

