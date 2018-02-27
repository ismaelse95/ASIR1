# Automontaje

Para montar un volumen automaticamente tendremos que confirugar mediante unos comandos, pero primero tendremos que instalar el paquete.

~~~
apt-get install autofs
~~~

Para editar el fichero tendremos que tener el daemon apagado y lo apagamos con.

~~~
systemctl stop autofs
~~~

Vamos a imaginar que tenemos un disco con una particion. Y lo primero que tenemos que hacer para hacer el automontaje es crear carpetas donde lo vamos a montar en mi caso crearé el siguiente.

~~~
mkdir -p DATOS/prueba
~~~

Una vez tengamos las carpetas entraremos en el fichero de autofs.

~~~
nano /etc/auto.master
~~~

Una vez dentro podremos poner en el final del fichero opciones para que un disco duro pueda automontarse cada vez que entremos en esa particion este lista para usarla. En el final del fichero introducimos lo siguiente.

~~~
/DATOS		/etc/auto.prueba 		--timeout=2,sync,nodev,nosuid
~~~

A continuación crearemos un el fichero **auto.prueba** en **/etc** y dentro del fichero tendremos que poner lo siguiente.

~~~
prueba  -fstype=ext4		UUID=3ab3f16b-b1d3-4c8c-ad87-ddb37fc62eb2
~~~

Donde prueba seria la carpeta creada dentro de DATOS. El fstype es el tipo de formato que tiene la particion y tambien hay que añadir el UUID que lo podremos ver con **lsblk -f**.

Por último crearemos los enlaces simbólicos para que sea mas fácil acceder al automontaje. Para crear el enlace lo haremos con el siguiente comando.

~~~
ln -s /DATOS/prueba enlaceprueba
~~~

Para finalizar tendremos que iniciar el autofs para que comprobar que todo funciona correctamente.

~~~
systemctl start autofs
~~~
