#!/usr/bin/python
# -*- coding: utf-8 -*-
from graphics import *
from consultas import *


# Borra la pantalla. Llamar antes de cada win update
def limpiar_pantalla(win):
	for item in win.items[:]:
		item.undraw()

# Funcion auxiliar que devuelve un rectangulo con las
# coordenadas correctas dependiendo el area en el mapa
def generar_rectangulo_area(area):
	rutas = {"101": Rectangle(Point(100, 311), Point(120, 332)),
		"102": Rectangle(Point(60, 288), Point(98, 311)),
		"103": Rectangle(Point(100, 265), Point(179, 287)),
		"104": Rectangle(Point(20, 243), Point(40, 284)),
		"105": Rectangle(Point(20, 284), Point(40, 378)),
		"106": Rectangle(Point(20, 377), Point(79, 400)),
		"107": Rectangle(Point(79, 400), Point(138, 423)),
		"108": Rectangle(Point(138, 400), Point(198, 423)),
		"109": Rectangle(Point(179, 356), Point(198, 400)),
		"110": Rectangle(Point(179, 243), Point(198, 310)),
		"111": Rectangle(Point(179, 85), Point(198, 220)),
		"112": Rectangle(Point(139, 153), Point(179, 175)),
		"113": Rectangle(Point(99, 85), Point(179, 108)),
		"114": Rectangle(Point(38, 85), Point(59, 153)),
		"115": Rectangle(Point(20, 129), Point(40, 197)),
		"116": Rectangle(Point(40, 197), Point(119, 220)),
		"117": Rectangle(Point(119, 220), Point(179, 243)),
		"118": Rectangle(Point(218, 220), Point(240, 243)),
		"119": Rectangle(Point(238, 85), Point(258, 242)),
		"120": Rectangle(Point(279, 85), Point(298, 175)),
		"121": Rectangle(Point(298, 152), Point(378, 175)),
		"122": Rectangle(Point(338, 175), Point(358, 220)),
		"123": Rectangle(Point(240, 220), Point(358, 243)),
		"124": Rectangle(Point(418, 152), Point(497, 222)),
		"125": Rectangle(Point(497, 152), Point(537, 198)),
		"126": Rectangle(Point(418, 222), Point(497, 287)),
		"127": Rectangle(Point(497, 222), Point(537, 287)),
		"128": Rectangle(Point(477, 287), Point(537, 311)),
		"129": Rectangle(Point(477, 311), Point(537, 334)),
		"130": Rectangle(Point(423, 311), Point(477, 334)) }
	return rutas[str(area)]

# Dibuja el mapa y marca las areas en las que aparece el
# pokemon cuya info se habia buscado. Para ello, recibe
# una lista de tuplas (nombre_especie, area) donde el campo
# area indica la ruta del mapa en que aparece el pokemon.
def dibujar_pantalla_mapa(win, pkmn_areas):
	fps = 20
	while True:
		limpiar_pantalla(win)
		# Cargo imagen del mapa en el centro de la pantalla
		img = Image(Point(320,240), "img/map.gif")
		img.draw(win)
		# Si el pokemon no tiene area, muestro "area unknown"
		if(len(pkmn_areas) == 0):
			rct = Rectangle(Point(0, 48), Point(640, 480))
			rct.setFill("black")
			rct.setTransparency()
			rct.draw(win)
			img = Image(Point(320,240), "img/areaUnknown.gif")
			img.draw(win)
		# Resalto las areas donde el pokemon aparece
		for area in pkmn_areas:
			rct = generar_rectangulo_area(area[1])
			rct.setFill("red")
			rct.setTransparency()
			rct.draw(win)
		# Chequeo si se presiono alguna tecla
		tecla = win.checkKey()
		if(tecla == "Escape"):
			return "pokedex"
		elif(tecla.lower() == "left"):
			return "info"
		elif(tecla.lower() == "right"):
			return "evol"
		elif(tecla.lower() == "f1"):
			return "exit"
		update(fps)
		
# Dibuja la pantalla de info del pokemon elegido. La info
# del pokemon debe ser una unica tupla con el sgte formato:
# (nro_pokedex, nombre_pkmn, descripcion, fue_capturado?)		
def dibujar_pantalla_info(win, pkmn_info):
	fps = 20
	while True:
		limpiar_pantalla(win)
		# Cargo imagen de la pantalla en el centro
		img = Image(Point(320,239), "img/infoScreen.gif")
		img.draw(win)
		# Imagen del pokemon actual
		img_centro = "img/" + pkmn_info[1].lower() + ".gif"
		img = Image(Point(120,170), img_centro)
		img.draw(win)
		# Nombre del pokemon actual
		pkmn_txt = format(pkmn_info[0], "03d") + "-" + pkmn_info[1]
		txt = Text(Point(210, 100), pkmn_txt)
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
			img_pkball = Image(Point(588, 100), "img/pokeball.gif")
			img_pkball.draw(win)
		# Chequeo si se presiono alguna tecla
		tecla = win.checkKey()
		if(tecla == "Escape"):
			return ("pokedex", 0)
		elif(tecla.lower() == "right"):
			return ("mapa", pkmn_info[1])
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

# Dibuja la pantalla de evoluciones del pokemon elegido. Se
# debe recibir el nombre de la especie de pokemon.	
def dibujar_pantalla_evol(win, nombre_especie):
	fps = 20
	# Obtengo pre-evolución y evolución del pkmn
	pres = devolver_preevoluciones(nombre_especie)
	evos = devolver_evoluciones(nombre_especie)
	while True:
		limpiar_pantalla(win)
		# Cargo imagen de la pokedex en el centro de la pantalla
		img = Image(Point(320,239), "img/evolScreen.gif")
		img.draw(win)
		# Imagen del pokemon actual
		img_centro = "img/" + nombre_especie.lower() + ".gif"
		img = Image(Point(320,190), img_centro)
		img.draw(win)
		evo_info = []
		# Imagen de pre-evolucion y evolucion
		if(len(pres) > 0):
			img_izqda = "img/" + pres[0][0].lower() + ".gif"
			img = Image(Point(120,190), img_izqda)
			img.draw(win)
			img = Image(Point(220,190), "img/arrow.gif")
			img.draw(win)
			if(pres[0][1].isdigit()):
				evo_info.append(pres[0][0] + " evolves into " + nombre_especie + " at level " + pres[0][1] + ".")
			else:
				evo_info.append(pres[0][0] + " evolves into " + nombre_especie + " by using " + pres[0][1] + ".")
		if(len(evos) > 0):
			img_dcha = "img/" + evos[0][0].lower() + ".gif"
			img = Image(Point(520,190), img_dcha)
			img.draw(win)
			img = Image(Point(420,190), "img/arrow.gif")
			img.draw(win)
			if(evos[0][1].isdigit()):
				evo_info.append(nombre_especie + " evolves into " + evos[0][0] + " at level " + evos[0][1] + ".")
			else:
				evo_info.append(nombre_especie + " evolves into " + evos[0][0] + " by using " + evos[0][1] + ".")
		if(len(pres) == 0 and len(evos) == 0):
				evo_info.append("No evolutions could be found with this pokémon.")
		# Imprimo la evo_info
		n_linea = 0
		for w in evo_info:
			txt = Text(Point(30, n_linea*37 + 308), evo_info[n_linea])
			txt.draw(win)
			txt.setStyle("bold")
			txt.setFace("courier")
			txt.setSize(14)
			n_linea += 1
		# Chequeo si se presiono alguna tecla
		tecla = win.checkKey()
		if(tecla == "Escape"):
			return ("pokedex", 0)
		elif(tecla.lower() == "left"):
			return ("mapa", nombre_especie)
		elif(tecla.lower() == "f1"):
			return ("exit", 0)
		update(fps)	
		
# Dibuja la pokedex usando la lista de pokemon recibida. Las tuplas
# de la lista deben respetar el sgte formato:
# (nro_pokedex, nombre_pkmn, fue_capturado?)		
def dibujar_pokedex(win, pokemon_list, cod_entr):
	# Cant de pokemon vistos y atrapados
	cant_v = format(devolver_cant_pokemon(), "03d")
	cant_a = format(devolver_cant_pokemon_atrapados(cod_entr), "03d")
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
		# Muestro cant de pokemon vistos y atrapados
		txt = Text(Point(58, 102), cant_v)
		txt.setStyle("bold")
		txt.setFace("courier")
		txt.setTextColor("white")
		txt.setSize(21)
		txt.draw(win)
		txt = Text(Point(58, 200), cant_a)
		txt.setStyle("bold")
		txt.setFace("courier")
		txt.setTextColor("white")
		txt.setSize(21)
		txt.draw(win)
		# Muestro textos con opciones
		txt = Text(Point(3, 330), "S:Search")
		txt.setStyle("bold")
		txt.setFace("courier")
		txt.setTextColor("white")
		txt.setSize(19)
		txt.draw(win)
		txt = Text(Point(3, 360), "T:Trainer")
		txt.setStyle("bold")
		txt.setFace("courier")
		txt.setTextColor("white")
		txt.setSize(19)
		txt.draw(win)
		txt = Text(Point(3, 300), "Enter:Info")
		txt.setStyle("bold")
		txt.setFace("courier")
		txt.setTextColor("white")
		txt.setSize(19)
		txt.draw(win)
		txt = Text(Point(415, 450), "Trainer:"+str(cod_entr))
		txt.setStyle("bold")
		txt.setFace("courier")
		txt.setTextColor("white")
		txt.setSize(19)
		txt.draw(win)
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
			txt.setStyle("bold")
			txt.setFace("courier")
			txt.setSize(21)
			txt.draw(win)
			if(pokemon_list[aux][2] > 0):
				img_pkball = Image(Point(365, i*37 + 56), "img/pokeball.gif")
				img_pkball.draw(win)
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
		elif(tecla.lower() == "t"):
			return ("pokedex", 0)
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
			(mode, rc) = dibujar_pokedex(win, rc, trainer)
			if(mode == "pokedex"):
				if(trainer == 125779):
					trainer = 423788
				else:
					trainer = 125779
				rc = devolver_todas_especies(trainer)
		elif(mode == "info"):
			# Modo pantalla info: recibe del modo pokedex el nombre
			# de una especie pokemon, busca su info y la muestra.
			# Si regresa al modo pokedex, le devuelve en rc la info
			# de todos los pokemon como si apenas hubiera iniciado
			rc = devolver_info_pokedex(rc, trainer)
			(mode, rc) = dibujar_pantalla_info(win, rc[0])
			if(mode == "pokedex"):
				rc = devolver_todas_especies(trainer)
		elif(mode == "mapa"):
			# Modo mapa: muestra las areas en las que aparece
			# el pokemon recibido. El mismo está en rc
			mode = dibujar_pantalla_mapa(win, devolver_areas_pokemon(rc))
			if(mode == "pokedex"):
				rc = devolver_todas_especies(trainer)
		elif(mode == "evol"):
			# Modo evol: muestra las evoluciones del
			# pokemon recibido. El mismo está en rc
			(mode, rc) = dibujar_pantalla_evol(win, rc)
			if(mode == "pokedex"):
				rc = devolver_todas_especies(trainer)
		elif(mode == "busqueda"):
			# Modo busqueda: permite buscar pokemon en la pokedex
			# por nombre, tipo o area en la que aparecen. Devuelve
			# en rc los resultados de la busqueda para mostrar en
			# la pokedex (es decir, devuelve tambien mode = "pokedex")
			(mode, rc) = dibujar_pantalla_busqueda(win, trainer)

		
