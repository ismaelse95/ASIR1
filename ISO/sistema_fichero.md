# Sistemas de Ficheros.

Para poder ver los discos que tenemos conectado a nuestro dispositivos desde la terminal tecleamos el comando (Todo esto tendremos que hacerlo como root).

~~~
$ lsblk -f
~~~

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

Y con ``lsblk -f`` veriamos que tendremos el nombre que hemos seleccionado.

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

Para montar nuestro disco cuando iniciamos nuestro ordenador tendremos que entrar con un editor de texto en el fichero ``/etc/fstab``.

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

## Creación de SWAP

Para crear una partición swap lo primero que tendremos que hacer es entrar con fdisk en el disco que queramos hacer la partición con el comando ``fdisk /dev/sdc`` Una vez dentro hacemos una partición y cuando acabemos de hacer un partición ejecutamos la opción **t** y en **Next code** introducimos **82**. Esta opción lo que hace es decir a la partición que será de tipo swap. Para finalizar y guardar los cambios ejecutamos la particion **w**.

A continuación instalamos el paquete partprobe con el comando.

~~~
sudo apt-get install partprobe
~~~

Una vez instalado lo particionamos con la herramienta partprobe.

~~~
mkswap -L swap1 /dev/sdc1
~~~

Para habilitar la swap tan solo tendremos que utilizar el comando:

~~~
swapon /dev/sdc1
~~~

Podremos desactivar la swap con.

~~~
swapoff /dev/sdc1
~~~

Para comprobar si la swap esta funcionando correctamente podremos comprobarlo con:

~~~
swapon -s
~~~

### Creación de fichero swap

Vamos a crear un fichero swap de 64 MB. Para ello tendremos que utilizar el comando dd.

~~~
dd if=/dev/zero of=/swap bs=1024 count=65536
~~~

~~~
65536+0 registros leídos
65536+0 registros escritos
67108864 bytes (67 MB, 64 MiB) copied, 0,633984 s, 106 MB/s
~~~

Una vez creado tendremos que preparar la zona /swap con el comando:

~~~
mkfswap /swap
~~~

~~~
mkswap: /swap: permisos 0644 no seguros; se sugiere 0600.
Configurando espacio de intercambio versión 1, tamaño = 64 MiB (67104768 bytes)
sin etiqueta, UUID=7a50bedc-40bc-4029-9eb3-afac782ea23b
~~~

Ahora tendremos que cambiar los permisos para que el fichero swap este seguro como nos dice al ejecutar el anterior comando. Para ello tendremos que utilizar el comando chmod.

~~~
chmod 600 /swap
~~~

Ahora la tendremos que encender con el comando.

~~~
swapon -v /swap
~~~

~~~
swapon: /swap: firma encontrada [tamaño de página=4096, firma=swap]
swapon: /swap: tamaño de página=4096, tamaño de intercambio=67108864, tamaño de dispositivo=67108864
swapon /swap
~~~

Con la opción -v podremos ver en pantalla lo todo lo que hace el comando como me lo ha mostrado a mi anteriormente.

Por último vamos al fichero ``/etc/fstap`` e introducimos la siguiente linea para que se inicie.

~~~
/swap		swap	swap	defaults	0	0	
~~~
