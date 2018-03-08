# KVM

Configurar tarjeta de red.

Entramos en la configuración de la tarjeta de red y tendremos que cambiar nuestra eth0 por br0 dejando el fichero ``/etc/network/interfaces`` tal y como lo muestro ahora.

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

Tendremos que instalar el KVM, para instalar tendremos que poner el siguiente paquete.

~~~
# sudo apt-get install qemu-kvm
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
# brctl addif br0 tap0
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
$ kvm -m 512 -hda jessie-1.qcow2 \
-device virtio-net,netdev=n0,mac=$MAC0 \
-netdev tap,id=n0,ifname=tap0,script=no,downscript=no
~~~

## Creación de bond

Para crear una interface bond tendremos que ejecutar el siguiente comando añadiendo el nombre que queramos a la interfaz.

~~~
# ip link add name "name" type bond
~~~

Ahora creamos los dos tap para ello tendremos que ejecutar dos veces el siguiente comando.

~~~
# ip tuntap add mode tap user user
~~~

A continuación tendremos que poner tap0 y tap1 como master de bond0 con estos dos comandos.

~~~
# ip link set dev tap0 master bond0
~~~

~~~
# ip link set dev tap1 master bond0
~~~

**Si tuvieramos un bridge llamado br0 podremos asociar el bond0 a br0 para ello lo tendremos que hacer con el siguiente comando.**

~~~
# ip link set dev bond0 master br0
~~~

Creamos las MAC correspondientes con los siguientes comandos.

~~~
$ MAC0=$(echo "02:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)
~~~

~~~
$ MAC1=$(echo "02:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)
~~~

Ahora tendremos que iniciar la máquina virtual con las dos interfaces de red, para ello tendremos que ejecutar el siguiente comando.

~~~
$ kvm -m 512 -hda jessie-1.qcow2 -device virtio-net,netdev=n0,mac=$MAC0 -device virtio-net,netdev=n1,mac=$MAC1 -netdev tap,id=n0,ifname=tap0,script=no,downscript=no -netdev tap,id=n1,ifname=tap1,script=no,downscript=no
~~~

Para finalizar tendremos que hacer eth0 y eth1 master de bond0 con los mismo comandos anteriores.

~~~
# ip link set dev eth0 master bond0
~~~

~~~
# ip link set dev eth1 master bond0
~~~

Ahora subimos el bond0 con el comando.

~~~
# ip l set dev bond0 up
~~~

Y le configuramos una ip en mi caso es la siguiente.

~~~
# ip a add 192.168.0.1/24 dev bond0
~~~

Por último en el otro lado del bond0 tendremos que configurar una ip para que puedan hacer ping entre ellas para ello le ponemos una ip del mismo rango que la red anterior.

~~~
# ip a add 192.168.0.2/24 dev bond0
~~~

Para ver las redes que tenemos en nuestro bond podremos verlas abriendo el siguiente fichero.

~~~
$ cat /proc/net/bonding/bond0
~~~

~~~
Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)

Bonding Mode: load balancing (round-robin)
MII Status: up
MII Polling Interval (ms): 0
Up Delay (ms): 0
Down Delay (ms): 0

Slave Interface: tap0
MII Status: up
Speed: 10 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: c6:6d:a8:98:fb:cd
Slave queue ID: 0

Slave Interface: tap1
MII Status: up
Speed: 10 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: be:06:a1:85:66:33
Slave queue ID: 0
~~~

## Tráfico etiquetado entre máquinas virtuales

Lo primero que tenemos que hacer para que podamos tener trafico etiquetado es crear una interfaz de red en mi caso crearé eth0.1 con id 1 y asociando a eth0, todo esto lo haremos con el siguiente comando.

~~~
# ip link add link eth0 name eth0.1 type vlan id 1
~~~

A continuacion podremos ver si el comando se ha ejecutado correctamente con el comando.

~~~
# ip -d link show
~~~

En la parte inferior de eth0.1 podremos ver que pone vlan 802.1q y a que vlan pertenece.

Ahora pasamos a levantar eth0.1.

~~~
# ip l set dev eth0.1 up
~~~

Una vez levantada eth0.1 creamos tap con el comando tuntap.

~~~
# ip tuntap add mode tap user user
~~~

A continuación podremos añadir un bridge y conectar a ese bridge tanto eth0.1 como tap0, esto lo haremos con los siguientes comandos.

~~~
# brctl addbr br1  			//		ip link add name br0 type bridge
~~~

~~~
# brctl addif br1 eth0.1	//		ip link set dev eth0.1 master br1
~~~

~~~
# brctl addif br1 tap0		//		ip link set dev tap0 master br1
~~~	

Para finalizar levantaremos tanto tap0 como br1.

~~~
# ip l set dev tap0 up
~~~

~~~
# ip l set dev br1 up
~~~

Crearemos la MAC sin root y iniciaremos la máquina con kvm.

~~~
$ MAC0=$(echo "02:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)
~~~

~~~
$ kvm -m 512 -hda jessie-1.qcow2 \
-device virtio-net,netdev=n0,mac=$MAC0 \
-netdev tap,id=n0,ifname=tap0,script=no,downscript=no
~~~

Copia de máquinas mediante terminal.

~~~
$ qemu-img create -b jessie-1.qcow2 -f qcow2 jessie-2.qcow2
~~~
