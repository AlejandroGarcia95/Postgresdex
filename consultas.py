from conexion import *

# Devuelve todas las especies de pokemon, en una lista con el formato
# (nro_pokedex, nombre_pkmn, fue_capturado?) donde el ultimo campo
# indica si el pokemon fue atrapado por el entrenador recibido
def devolver_todas_especies(cod_entrenador): 
	conn = establecer_conexion()
	q = ("SELECT e.numero_pokedex, e.nombre, COUNT(t.id) "
		"FROM especie_pokemon e LEFT OUTER JOIN "
		"(SELECT p.nombre_especie, p.id FROM "
		"pokemon_capturado pc INNER JOIN pokemon p "
		"ON p.id = pc.pokemon_id "
		"WHERE pc.codigo_entrenador = " + str(cod_entrenador) + ") AS t "
		"ON t.nombre_especie = e.nombre "
		"GROUP BY e.numero_pokedex, e.nombre " 
		"ORDER BY e.numero_pokedex"
		)
	print q
	rc = realizar_consulta(conn, q)
	cerrar_conexion(conn)
	return rc

# Devuelve la info de la pokedex del pokemon en el formato
# (nro_pokedex, nombre_pkmn, descripcion, fue_capturado?)
# donde el ult campo indica si la especie fue atrapada
# por el entrenador recibido como parametro
def devolver_info_pokedex(nombre_especie, cod_entrenador): 
	conn = establecer_conexion()
	q = ("SELECT e.numero_pokedex, e.nombre, e.descripcion, COUNT(t.id) "
		"FROM especie_pokemon e LEFT OUTER JOIN "
		"(SELECT p.nombre_especie, p.id FROM "
		"pokemon_capturado pc INNER JOIN pokemon p "
		"ON p.id = pc.pokemon_id "
		"WHERE pc.codigo_entrenador = " + str(cod_entrenador) + ") AS t "
		"ON t.nombre_especie = e.nombre "
		"WHERE e.nombre = \'" + nombre_especie + "\' "
		"GROUP BY e.numero_pokedex, e.nombre " 
		"ORDER BY e.numero_pokedex"
		)
	print q
	rc = realizar_consulta(conn, q)
	cerrar_conexion(conn)
	return rc

# Devuelve todas las especies del tipo recibido, que se encuentren
# en la ruta recibida, y cuyo nombre es el pasado como parametro. 
# Debido a que la consulta interna usa el operador ILIKE, si alguno
# de estos argumentos se pasa con el valor "%", la busqueda no filtrara
# por ese campo (por ej. si ruta="%" solo se buscara por nombre y tipo)
# El resultado es una lista cuyas tuplas cumplen con el sgte formato: 
# (nro_pokedex, nombre_pkmn, fue_capturado?) donde el ultimo campo 
# indica si el pokemon fue atrapado por el entrenador recibido
def buscar_especies(nombre, tipo, ruta, cod_entrenador): 
	conn = establecer_conexion()
	q = ("SELECT t1.numero_pokedex, t1.nombre, COUNT(t2.id) "
		"FROM (especie_pokemon e INNER JOIN tipo_especie t "
		"ON e.nombre = t.nombre_especie) AS t1 "
		"LEFT OUTER JOIN (SELECT p.nombre_especie, p.id "
		"FROM pokemon_capturado pc INNER JOIN pokemon p "
		"ON p.id = pc.pokemon_id INNER JOIN pokemon_salvaje ps "
		"ON ps.nombre_especie = p.nombre_especie "
		"WHERE (pc.codigo_entrenador = " + str(cod_entrenador) + " AND "
		" CAST(ps.numero_ruta AS TEXT) ILIKE \'" + str(ruta) + "\')) AS t2 "
		"ON t1.nombre = t2.nombre_especie "
		"WHERE (t1.nombre_tipo ILIKE \'" + tipo + "\' AND "
		"t1.nombre ILIKE \'" + nombre + "\') "
		"GROUP BY t1.numero_pokedex, t1.nombre " 
		"ORDER BY t1.numero_pokedex"
		)
	print q
	rc = realizar_consulta(conn, q)
	cerrar_conexion(conn)
	return rc
