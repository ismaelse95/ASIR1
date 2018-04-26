#OSPFv2

Para configurar mediante ospfv2 tendremos que instalar el paquete quagga.

~~~
apt-get install quagga
~~~

Despues entramos en /etc/quagga/daemons y tendremos que dejar el fichero de la siguiente manera.

~~~
zebra=yes
bgpd=no
ospfd=yes
ospf6d=no
ripd=no
ripngd=no
isisd=no
babeld=no
~~~


Ahora pasamos a compiar los dos fichero de configuración tanto zebra.conf como ospfd.conf.

~~~
cp /usr/share/doc/quagga/examples/zebra.conf.sample /etc/quagga/zebra.conf
~~~

~~~
cp /usr/share/doc/quagga/examples/ospfd.conf.sample /etc/quagga/ospfd.conf
~~~

Ahora entramos en el fichero zebra y añadimos lo siguiente al final del fichero.

~~~
interface eth0
 ip address 172.22.2.23/16
interface eth1
 ip address 10.0.214.1/24

log file /var/log/quagga/zebra.log
~~~

Pasamos al fichero ospfd y configuramos lo siguiente.

~~~
interface eth0
interface eth1

router ospf
! ospf router-id 172.22.2.23
  network 172.22.0.0/16 area 0
  network 10.0.214.0/24 area 0

log file /var/log/quagga/ospfd.log
~~~

Por último reiniciamos el servicio.

~~~
systemctl restart quagga.service
~~~

## Microtik

Añadimos la ip.

~~~
 [admin@MikroTikR1]/ip address add address=10.0.100.2/24 interface=ether1
 [admin@MikroTikR1]/ip address add address=10.0.120.5/24 interface=ether2
 [admin@MikroTikR1]/ip address add address=10.0.130.6/24 interface=ether3
~~~

Creamos el fichero default.

~~~
[admin@MikroTikR1] /routing ospf instance> add name=default
~~~

Creamos el puente y lo configuramos.

~~~
[admin@MikroTikR1] /interface bridge> add name=loopback
~~~

~~~
[admin@MikroTikR1] > ip address add address=0.0.0.1/32 interface=loopback 
~~~

~~~
[admin@MikroTikR1] /routing ospf instance> set 0 router-id=0.0.0.1
~~~

Introducimos el area de ospf.

~~~
[admin@MikroTikR1] /routing ospf network> add network=10.0.100.0/24 area=backbone
[admin@MikroTikR1] /routing ospf network> add network=10.0.120.0/24 area=backbone
[admin@MikroTikR1] /routing ospf network> add network=10.0.130.0/24 area=backbone
~~~
