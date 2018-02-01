def pasar_a_segundos(hora,minu,segun):
	if hora > 24 or minu > 59 or segun > 59:
		return 0
	else:
		return (hora*3600)+(minu*60)+segun

def calcular_coste(tarifa, segun):
	return int(tarifa) * segun

def convertir_a_euros:

