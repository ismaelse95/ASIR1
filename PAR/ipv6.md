# IPV6

MAC0=$(echo "00:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)

MAC1=$(echo "00:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)

MAC2=$(echo "00:"`openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//'`)

brctl addbr br0

brctl addbr br1

ip tuntap add mode tap user ismael

ip tuntap add mode tap user ismael

ip tuntap add mode tap user ismael

ip l set master br0 dev tap0

ip l set master br0 dev eth0

ip l set eth0 up

ip l set master br1 dev tap1

ip l set master br1 dev tap2

ip l set dev tap0 up

ip l set dev tap1 up

ip l set dev tap2 up

ip l set dev br0

ip l set dev br1

EN LA MÁQUINA SERVIDOR:

ip l set dev eth0 up

++++++dhclient -6 eth0

ip -6 r add default via 2001:470:ccba::1

ip l set eth1 up

dhclient -6 -r eth0

rm /var/lib/dhcp/dhclient6.leases

dhclient -P eth0

less /var/lib/dhcp/dhclient6.leases

--Servidor estatico

ip -6 a add ipprefijo::1/64 dev eth1

echo 1 > /proc/sys/net/ipv6/conf/all/forwanding

EN LA MÁQUINA CLIENTE:

ip l set eth0 up

--Cliente estatico

ip -6 a add ipprefijo::2/64 dev eth0

ip -6 r add default via ipprefijo::1

configurar dns:
	nameserver 2001:470:ccba:2::2

Tarjeta de red cambiadas:

echo "" > /etc/udev/rules.d/70-persutent-net.rules