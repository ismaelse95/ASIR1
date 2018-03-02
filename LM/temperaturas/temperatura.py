from funciones import poblacion, url, temperatura
from lxml import etree
import time

dia=time.strftime("%Y-%m-%d")
muni=input("Dame una población de Sevilla: 	")
print(" ")
arbol=etree.parse('sevilla.xml')
arbol2=etree.parse(url(poblacion(arbol,muni)))
temperaturas=temperatura(arbol2,dia_hoy)
print("La temperatura máxima de {} es de {}º".format(muni,temperaturas[0]))
print("La temperatura mínima de {} es de {}º".format(muni,temperaturas[1]))