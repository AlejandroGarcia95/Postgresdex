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
