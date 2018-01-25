# Montaje de discos en Linux y distintos .

Para poder ver los discos que tenemos conectado a nuestro dispositivos desde la terminal tecleamos el comando. Todo esto tendremos que hacerlo como root.

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

Para poder dar formato