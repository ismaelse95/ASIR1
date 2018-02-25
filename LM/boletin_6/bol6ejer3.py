from crypt import crypt
import getpass

with open("100.txt", "r") as elem1:
	contra1=elem1.readlines()

with open("/etc/shadow", "r") as elem2:
	contra2=elem2.readlines()

craqueo=[]
for elem in contra1:
	craqueo.append(elem.strip("\n"))

fichero=[]
for elem in contra2:
	fichero.append(elem.split(":"))

usuario=input("Dame el usuario: ")
descifrado=False

for elem1 in fichero:
	if usuario==elem1[0]:
		for elem2 in craqueo:
			if elem1[1]==crypt(elem2, elem1[1][:12]):
				print("Contraseña descifrada: {}".format(elem2))
				descifrado=True
				break

if not descifrado:
	print("No se puede averiguar la contraseña.")