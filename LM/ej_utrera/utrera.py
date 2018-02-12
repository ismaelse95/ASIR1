from lxml import etree
arbol=etree.parse('utrera.xml')

#Ejercicio 1
def calles(arbol):
	return arbol.xpath('//way/tag[@k="highway"]/../@id')

#Ejercicio 2
def nombre_calles(arbol):
	return arbol.xpath('//way/tag[@k="highway"]/../tag[@k="name"]/@v')

#Ejercicio 3
def nodos(arbol):
	return arbol.xpath('//node[@uid="384182" and count=(tag)>0]/@id')

#Ejercicio 4
def supermercado(arbol):
	return arbol.xpath('count(//way/tag[@k="shop"]/../tag[@v="supermarket"])')


print("Ejercicio 1")
print(calles(arbol))

print("Ejercicio 2")
print(nombre_calles(arbol))

print("Ejercicio 3")
print(nodos(arbol))

print("Ejercicio 4")
print(supermercado(arbol))
