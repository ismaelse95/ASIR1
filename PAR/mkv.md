# MKV

Configurar tarjeta de red.

Entramos en la configuración de la trjeta de red y tendremos que cambiar nuestra eth0 por br0 dejanlo el fichero ``/etc/network/interfaces`` tal y como lo miestro ahora.

~~~
auto lo
iface lo inet loopback

allow-hotplug br0
iface br0 inet dhcp
  bridge_ports eth0

#allow-hotplug eth0
#iface eth0 inet dhcp
~~~

Ahora levantamos br0 con el comando(Como root).

~~~
# ifup br0
~~~

Tendremos que isntalar el KVM, para instalar tendremos que poner el siguiente paquete.

~~~
# sudo apt-get install qemu-kvmc
~~~

Ahora añadiremos una nueva interfaz de red virtual(Como root).

~~~
# ip tuntap add mode tap user user
~~~

Podemos ver esa nueva interfaz con el comando.

~~~
# ip tuntap list
~~~

Ahora lo conectamos al dispositivo br0(Como root).

~~~
# brtcl addif br0 tap0
~~~

Por último levantamos la tarjeta de red(como root).

~~~
# ip l set dev tap0 up
~~~

Ahora nos salimos y nos metemos en nuestro usuario y tendremos que generar una MAC.

~~~
$ MAC0=$(echo "02:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)
~~~

Podremos ver que la hemos creado correctamente.

~~~
$ echo $MAC0
~~~

Por último podremos levantar la máquina desde el usuario normal con el comando.

~~~
kvm -m 512 -hda jessie-1.qcow2 \
-device virtio-net,netdev=n0,mac=$MAC0 \
-netdev tap,id=n0,ifname=tap0,script=no,downscript=no
~~~

