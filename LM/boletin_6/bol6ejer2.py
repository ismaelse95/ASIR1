from crypt import crypt
import getpass

with open("/etc/shadow","r") as elem:
	contra=elem.readlines()

usuario=input("Usuario: ")
contraseña=getpass.getpass("contraseña: ")
operacion=False

for elem in contra:
	if usuario==elem.split(":")[0]:
		if crypt(contraseña, elem.split(":")[1][:12])==elem.split(":")[1]:
			print("Los datos introducidos son correctos")
			operacion=True
			break
		else:
			print("Contraseña incorrecta.")
			operacion=True

if not operacion:
	print("Usuario incorrecto.")