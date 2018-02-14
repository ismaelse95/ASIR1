from funciones import calcular_coste,pasar_a_segundos,convertir_a_euros

with open("comunicaciones.txt","r") as fichero:
	lfichero=fichero.readlines()

lista=[]
tarifa=0
contador1=0
contador2=0

for elem in lfichero:
	lista.append(elem.strip('\n'))

for elem in lista[0]:
	cent = 0
	if elem.isdigit():
		cent += int(elem)
	lista[0] = cent
tarifa = cent

lista.pop(0)

for elem in lista:
	contador2+=1
	hora = int(elem.split(':')[0])
	minu = int(elem.split(':')[1])
	segu = int(elem.split(':')[2])
	segundos=pasar_a_segundos(hora, minu, segu)
	centimos=calcular_coste(segundos,tarifa)
	contador1+=centimos
	euros=convertir_a_euros(centimos)
	print("El coste de la llamada {} es {} €.".format(contador2,euros))

total=convertir_a_euros(contador1)
print("El coste total de todas las llamdas son: {} €.".format(total))