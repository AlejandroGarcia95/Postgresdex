#!/usr/bin/python
# -*- coding: utf-8 -*-
from graphics import *
from consultas import *


# Borra la pantalla. Llamar antes de cada win update
def limpiar_pantalla(win):
	for item in win.items[:]:
		item.undraw()
		
# Dibuja la pantalla de info del pokemon elegido. La info
# del pokemon debe ser una unica tupla con el sgte formato:
# (nro_pokedex, nombre_pkmn, descripcion, fue_capturado?)		
def dibujar_pantalla_info(win, pkmn_info):
	fps = 20
	while True:
		limpiar_pantalla(win)
		# Cargo imagen de la pokedex en el centro de la pantalla
		img = Image(Point(320,240), "img/infoScreen.gif")
		img.draw(win)
		# Imagen del pokemon actual
		img_centro = "img/" + pkmn_info[1].lower() + ".gif"
		img = Image(Point(120,110), img_centro)
		img.draw(win)
		# Nombre del pokemon actual
		pkmn_txt = format(pkmn_info[0], "03d") + "-" + pkmn_info[1]
		txt = Text(Point(210, 80), pkmn_txt)
		txt.draw(win)
		txt.setStyle("bold")
		txt.setFace("courier")
		txt.setSize(32)
		# Imprimo la info del pokemon... Para eso la parseo
		# en lineas de longitud largo_linea
		texto_linea = ""
		n_linea = 0
		largo_linea = 40
		for w in pkmn_info[2].split():
			if((len(texto_linea) + 1 + len(w)) < largo_linea):
				texto_linea = texto_linea + w + " "
			else:
				# Si me paso de la long. de la linea, la imprimo
				txt = Text(Point(30, n_linea*37 + 275), texto_linea)
				txt.draw(win)
				txt.setStyle("bold")
				txt.setFace("courier")
				txt.setSize(18)
				n_linea += 1
				texto_linea = w + " "
		# Falta imprimir la ultima linea
		txt = Text(Point(30, n_linea*37 + 270), texto_linea)
		txt.draw(win)
		txt.setStyle("bold")
		txt.setFace("courier")
		txt.setSize(20)
		# Si fue capturado, imprimo pokeball
		if(pkmn_info[3] > 0):
			img_pkball = Image(Point(588, 30), "img/pokeball.gif")
			img_pkball.draw(win)
		# Chequeo si se presiono alguna tecla
		tecla = win.checkKey()
		if(tecla == "Escape"):
			return ("pokedex", 0)
		elif(tecla.lower() == "f1"):
			return ("exit", 0)
		update(fps)

# Dibuja la pokedex usando la lista de pokemon recibida. Las tuplas
# de la lista deben respetar el sgte formato:
# (nro_pokedex, nombre_pkmn, fue_capturado?)		
def dibujar_pantalla_busqueda(win, cod_entrenador):
	limpiar_pantalla(win)
	fps = 10
	# inputBoxes para cada opcion
	inputBoxTipo = Entry(Point(235, 134), 13)
	inputBoxTipo.setStyle("bold")
	inputBoxTipo.setFace("courier")
	inputBoxTipo.setSize(21)
	inputBoxTipo.setFill("white")
	inputBoxNombre = Entry(Point(235, 80), 13)
	inputBoxNombre.setStyle("bold")
	inputBoxNombre.setFace("courier")
	inputBoxNombre.setSize(21)
	inputBoxNombre.setFill("white")
	inputBoxArea = Entry(Point(235, 187), 13)
	inputBoxArea.setStyle("bold")
	inputBoxArea.setFace("courier")
	inputBoxArea.setSize(21)
	inputBoxArea.setFill("white")
	# Dibujo todo
	img = Image(Point(320,240), "img/searchScreen.gif")
	img.draw(win)
	inputBoxTipo.draw(win)
	inputBoxNombre.draw(win)
	inputBoxArea.draw(win)
	txt = Text(Point(20, 335), "Fill in some of the fields and press enter!")
	txt.setStyle("bold")
	txt.setFace("courier")
	txt.setSize(17)
	txt.draw(win)
	while True:
		# Chequeo si se presiono alguna tecla
		tecla = win.getKey()
		if(tecla == "Escape"):
			return ("pokedex", devolver_todas_especies(trainer))
		elif(tecla == "Return"):
			tipoBusq = inputBoxTipo.getText() + "%"
			areaBusq = inputBoxArea.getText() + "%"
			nombreBusq = inputBoxNombre.getText() + "%"
			rc = buscar_especies(nombreBusq, tipoBusq, areaBusq, cod_entrenador)
			if(len(rc) == 0):
				txt.setText("Sorry, no matches found")
			else:
				return ("pokedex", rc)
		elif(tecla.lower() == "f1"):
			return ("exit", 0)
		update(fps)
	
		
# Dibuja la pokedex usando la lista de pokemon recibida. Las tuplas
# de la lista deben respetar el sgte formato:
# (nro_pokedex, nombre_pkmn, fue_capturado?)		
def dibujar_pokedex(win, pokemon_list):
	# La view de la lista de la pokedex tiene tamaño para mostrar 11
	# nombres de pokemon, siendo el sexto el "central". Para ir
	# mostrandolos, voy indexando la pokemon_list 
	pkdx_size = 5	# Desde el centro, puedo ver 5 para arriba y 5 para abajo
	p_centro = 0	# Índice del pkmn que va en el centro
	fps = 20
	while True:
		limpiar_pantalla(win)
		# Cargo imagen de la pokedex en el centro de la pantalla
		img = Image(Point(320,240), "img/pokedex.gif")
		img.draw(win)
		# Imagen del pokemon actual
		img_centro = "img/" + pokemon_list[p_centro][1].lower() + ".gif"
		img = Image(Point(252,240), img_centro)
		img.draw(win)
		aux = p_centro - pkdx_size #Auxiliar para iterar la lista 
		for i in range(0, 2*pkdx_size+1):
			if(aux < 0 or aux >= len(pokemon_list)):
				aux += 1
				continue
			# Entrada de la lista para el pokemon aux-esimo
			list_txt = format(pokemon_list[aux][0], "03d") + "-" + pokemon_list[aux][1]
			txt = Text(Point(376, i*37 + 40), list_txt)
			txt.draw(win)
			if(pokemon_list[aux][2] > 0):
				img_pkball = Image(Point(365, i*37 + 56), "img/pokeball.gif")
				img_pkball.draw(win)
			txt.setStyle("bold")
			txt.setFace("courier")
			txt.setSize(21)
			aux += 1
		# Chequeo si se presiono alguna tecla
		tecla = win.checkKey()
		if(tecla == "Up" and p_centro > 0):
			p_centro -= 1
		elif(tecla == "Down" and p_centro < len(pokemon_list)-1):
			p_centro += 1
		elif(tecla.lower() == "return"):
			return ("info", pokemon_list[p_centro][1])
		elif(tecla.lower() == "s"):
			return ("busqueda", 0)
		elif(tecla.lower() == "f1"):
			return ("exit", 0)
		update(fps)
			


if __name__ == '__main__':
	
	# Obtener inicialmente todos los pokemon
	trainer = 125779
	rc = devolver_todas_especies(trainer)
	win = GraphWin("Pokedex", 640, 480, autoflush = False)
	# Inicialmente voy a la pantalla de la pokedex
	mode = "pokedex"
	while(mode != "exit"):
		if(mode == "pokedex"):
			# Modo pokedex: recibe en rc una lista de especies
			# pokemon y las dibuja dentro de la pokedex
			(mode, rc) = dibujar_pokedex(win, rc)
		elif(mode == "info"):
			# Modo pantalla info: recibe del modo pokedex el nombre
			# de una especie pokemon, busca su info y la muestra.
			# Si regresa al modo pokedex, le devuelve en rc la info
			# de todos los pokemon como si apenas hubiera iniciado
			rc = devolver_info_pokedex(rc, trainer)
			(mode, rc) = dibujar_pantalla_info(win, rc[0])
			if(mode == "pokedex"):
				rc = devolver_todas_especies(trainer)
		elif(mode == "busqueda"):
			(mode, rc) = dibujar_pantalla_busqueda(win, trainer)

		
