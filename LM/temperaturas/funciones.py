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