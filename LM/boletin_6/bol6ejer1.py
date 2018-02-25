def calcula_dc(lista):
	pesos=[1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
	aux = []
	for i in range(10):
		aux.append(lista[i]*pesos[i])
		resto = 11 - sum(aux) %11
	if resto == 10:
		return 1
	elif resto == 11:
		return 0
	else:
		return resto

with open("bancos.txt","r") as elem:
	bancos=elem.readlines()

#--------------------------------------------------

cuenta=input("Dame un número de cuenta: ")

if len(cuenta) != 20:
	print("Este número de cuenta no es válido")
else: 
	primero="0"+"0"+cuenta[:8]
	segudno=cuenta[10:]
	primero=list(map(int,primero))
	segudno=list(map(int,segudno))
	c1=calcula_dc(primero)
	c2=calcula_dc(segudno)
	if int(cuenta[8]) == c1 and c2 == int(cuenta[9]):
		for elem in bancos:
			if cuenta[0:3] == elem[0:3]:
				print("El número de cuenta pertenece a",elem[5:])
				break

