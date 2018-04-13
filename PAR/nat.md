# NAT

## IPTABLES

Define la tabla --> Vamos a utilizar la tabla nat.

Cada nat tiene cadenas --> PREROUTING = Son las reglas que se aplican en la tabla nat antes de enrutar.
						   POSTROUTING 
						   OUTPUT
						   INPUT

SNAT = Es un proceso de Postrouting

~~~
iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o eth0 -j SNAT --to 172.22.x.x (ip que tenemos en la eth0 de la máquina servidor)
~~~

- Reglas que estan aplicadas:

	iptables -t nat -L -n -v --line-numbers

- Podemos hacer un flash:
	
	iptables -t nat -F POSTROUTING

~~~
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -d 172.22.x.x -j DNAT --to 10.0.0.2
~~~

~~~
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -d 172.22.x.x -j DNAT --to 10.0.0.2:22
~~~

**Para dejar estatico NAT:**

~~~
iptables-save > rules.v4
~~~

~~~
apt install iptables-persistent
~~~

~~~
mv /root/rules.v4 /etc/iptables/
~~~

Reiniciamos la máquina.

Activar el forward y configurar la máquina.