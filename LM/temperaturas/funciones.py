def poblacion(texto, municipio):
	nombres=texto.xpath("//municipio/text()")
	buscar=False
	for elem in nombres:
		if elem==municipio:
			codigo=texto.xpath('//municipio[text()="{}"]/@value'.format(municipio))
			buscar=True
			return codigo[0][-5:]
	if not buscar:
		return "Error"

def url(codigo):
	if codigo.startswith("Error"):
		return "La población no se ha encontrado."
	else:
		return ('http://www.aemet.es/xml/municipios/localidad_{}.xml'.format(codigo))

def temperatura(texto, tempe):
	maxima=texto.xpath('//prediccion/dia[@fecha="{}"]/temperatura/maxima/text()'.format(tempe))
	minima=texto.xpath('//prediccion/dia[@fecha="{}"]/temperatura/minima/text()'.format(tempe))
	return maxima[0],minima[0]