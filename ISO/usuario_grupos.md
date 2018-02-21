# Usuario y Grupos

Todo usuario o grupo tiene una contraseña que están cifradas en MD5, DES.

Con el comando whois podremos ver el cifrado soportado.

Podremos ver los metodos disponibles de cifrado con el siguiente comando.

~~~
ismael@Ismael:~$ mkpasswd -m help
Métodos disponibles:
des	standard 56 bit DES-based crypt(3)
md5	MD5
sha-256	SHA-256
sha-512	SHA-512
~~~

- Fichero de usuario y grupos.

``cat /etc/passwd``--> Para ver los usuarios que tenemos creados.

``cat /etc/group`` --> En este fichero vemos los grupos que tenemos en nuestro sistema.

``cat /etc/shadow`` --> Por último en este fichero estan las contraseñas de los usuarios que tenemos en el sistema.

## Generación de contraseñas

Para generar contraseñas con apg primero lo tendremos que instalar.

~~~
usuario@debian:~$ apt-get install apg
~~~

Ahora para generar contraseñas tendremos que ejecutar el comando:

~~~
usuario@debian:~$ apg -x 4 -m 25
~~~

Donde la opción **x** es las contraseñas que queremos crear y la opción **m** es la longitud de la contraseña.

Podremos generar contraseñas encriptadas con el comando mkpasswd para poder crear constraseñas tendremos que ejectuar el siguiente comando con los siguientes parametros.

~~~
usuario@debian:~$ mkpasswd -m sha-512 -S asdfghjk
~~~

A continuación nos pedirá que escogamos nuestra constraseña para encriptar, la introduciremos y ya tendremos nuestra contraseña encriptada creada.

~~~
usuario@debian:~$ mkpasswd -m sha-512 -S asdfghjk
Contraseña: 
$6$asdfghjk$sKnR1xODLmNscbWOYoLPr1p1caSRjWVLFHeAkVIY8rqkcH5kS2VJIlIcpL9PXVsmTyhNau..ES9Qe69zjQuS60
~~~

## Creación de usuarios

Para crear un usuario lo haremos con el comando useradd.

~~~
usuario@debian:~$ useradd ismael
~~~

También tendremos distintas opciones para el comando como las siguientes:

- -m: Crea el directorio personal
- -u: especifica el UID numérico del usuario, se cambia en función del fichero login.defs y los UID existentes.
- -g: especifica el grupo principal del usuario.
- -G: especifica los grupos secundarios, separado por comas.
- -d: ruta del directorio personal.
- -c: comentario de la cuenta.
- -s: shell por defecto del usuario.
- -p: contraseña, deberá estar ya cifrada.

## Ejercicio

**Creación de cuentas de usuario en modo batch, para ello emplea los comandos newusers, chpasswd, pwgen y sentencia de iteración for.**

**Sube los ficheros empleados, así como la sintaxis de los comandos empleados.**

Creamos los usuarios con el for.

~~~
for i in {1..10}; do `echo usuario$i:x:1000$i:1500::/home/usuario$i:/bin/bash >> usuario.txt`;done
~~~

Con esto tendriamos creado el fichero con los usuarios.

Ahora generamos contraseña y lo guardamos en el fichero pass.txt. 

~~~
for i in {1..10};do `echo usuario$i:$(pwgen 12 10) >> pass.txt`
~~~

A continuación cambiamos los permisos para que solo los pueda leer root el fichero.

~~~
chmod 400 pass.txt
~~~

Por último cambiamos la contraseña a todos los usuarios.

~~~
chpasswd < pass.txt
~~~

