# NAT

## IPTABLES

Define la tabla --> Vamos a utilizar la tabla nat.

Cada nat tiene cadenas --> PREROUTING = Son las reglas que se aplican en la tabla nat antes de enrutar.
						   POSTROUTING 
						   OUTPUT
						   INPUT

SNAT = Es un proceso de Postrouting

iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o eth0 -j SNAT --to 172.22.x.x (ip que tenemos en la eth0 de la máquina servidor)

- Reglas que estan aplicadas:

	iptables -t nat -L -n -v --line-numbers

- Podemos hacer un flash:
	
	iptables -t nat -F POSTROUTING