# Script

Vamos a crear un scrip y lo que vamos ha hacer es lo siguiente.

Automatiza la actualización del sistema indicando qué paquetes se desean actualizar y cuales desinstalar, creando una interacción con el usuario.

Comando a utilizar:

- Actualizr solo un paquete:

~~~
sudo apt-get install --only-upgrade oracle-jdk7-installer
~~~

- Paquetes que estan sin actualizar:

~~~
sudo apt list --upgradable | cut -d "/" -f 1
~~~

