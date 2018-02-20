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

- Socket TCP/IP --> Con un socket a cada lado se establece una conexión entre las dos maquinas mediante un puerto y termina cuando hay un SYN ACK.

- Demonio (daemon) --> Es un proceso que se ejecuta en segundo plano.

- Socket UNIX --> Se conecta un cliente y un servidor mediante un fichero llamado socket. Se suele especificar por ejemplo: ``mysqli:///``. Donde la **i** y la **///** indicaria que es un canal UNIX.