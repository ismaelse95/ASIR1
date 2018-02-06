from funciones import calcular_coste,pasar_a_segundos,convertir_a_euros

tarifa=int(input("Dame la tarifa por segundos en centimos: "))
comun=int(input("Dame el número de comunicaciones realizadas: "))
duracion=[]
acumulador=0
nllamada=1

for elem in range(comun):
	listallamada=[]
	llamada=input("¿Cuánto duró la comunicación {}? (Indicar en horas:minutos:segundos): ".format(elem + 1))
	horas=int(llamada.split(":")[0])
	minu=int(llamada.split(":")[1])
	segun=int(llamada.split(":")[2])
	listallamada.append(nllamada)
	listallamada.append(pasar_a_segundos(horas,minu,segun))
	duracion.append(listallamada)
	listallamada=[]
	nllamada+=1

for elem in duracion:
	acumulador += elem[1]

for elem in duracion:
	print ("El coste de la llamada {} es {} €.".format(elem[0],convertir_a_euros(int(calcular_coste(elem[1], tarifa)))))

print ("El coste total de todas las llamdas son: {} €.".format(convertir_a_euros(calcular_coste(acumulador,tarifa))))