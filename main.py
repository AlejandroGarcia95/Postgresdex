#!/usr/bin/python
# -*- coding: utf-8 -*-
from graphics import *
from consultas import *


# Borra la pantalla. Llamar antes de cada win update
def limpiar_pantalla(win):
	for item in win.items[:]:
		item.undraw()
		
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
		elif(tecla == "Escape"):
			return "exit"
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
			mode = dibujar_pokedex(win, rc)
		#elif(mode == "busqueda"):
		#	(mode, rc) = dibujar_pantalla_busqueda(win, trainer)
		
