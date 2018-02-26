# Servidor DHCP

Aquí podemos ver el proceso en el que una máquina pide una ip a un servidor DHCP.

**DCHP DISCOVERY**

- Difusion enlace
- Difusion IP
- Puerto 67/udp

**DCHP OFFER**

- MAC Cliente
- Difusión IP
- Puerto orig: 67, Puerto dest: 68

**DHCP REQUEST**

- MAC servidor
- IP servidor
- Puerto 67/udp

**DHCP ACK**

***

- Socket TCP/IP --> Con un socket a cada lado se establece una conexión entre las dos máquinas mediante un puerto y termina cuando hay un SYN ACK.

- Demonio (daemon) --> Es un proceso que se ejecuta en segundo plano.

- Socket UNIX --> Se conecta un cliente y un servidor mediante un fichero llamado socket. Se suele especificar por ejemplo: ``mysqli:///``. Donde la **i** y la **///** indicaria que es un canal UNIX.

***

## Configurar el DHCP en KVM

Creamos 3 tap.

~~~
ip tuntap add mode tap user ismael
~~~

~~~
ip l add name br1 type bridge
~~~

~~~
ip l set br1 up
~~~

~~~
ip l set dev tap1 master br1
~~~

~~~
ip l set dev tap2 master br1
~~~

~~~
ip l set dev tap3 master br1
~~~

Creamos las 3 mac.

~~~
$ MAC0=$(echo "02:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)
~~~

~~~
$ MAC1=$(echo "02:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)
~~~

~~~
$ MAC2=$(echo "02:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)
~~~

Dentro de la maquina virtual.

~~~
apt-get install isc-dhcp-server
~~~

~~~
ip l set dev eth0 down
~~~

Dentro del fichero ``nano /etc/default/isc-fhcp-sever`` vamos a configurar lo siguiente.

Nos iremos a **INTERFACES** y entre las comillas ponemos **eth1**.

Ahora nos vamos a ``cd /etc/dhcp`` y configuramos la siguientes directivas del fichero ``nano dhcp.conf`` .

En **option domain-name servers** pondremos nuestra ip **192.168.1.1;**.

Ahora añadimos al fichero una subnet, para repatir un rango de ip.

~~~
subnet 192.168.1.0 netmask 255.255.255.0 (
	range 192.168.1.2 192.168.1.10;
)
~~~

Reiniciamos el servicio con systemctl.

~~~
systemctl restart isc-dhcp-server.service
~~~

Para ver el puerto.

~~~
ss -lnup |grep 67
~~~

