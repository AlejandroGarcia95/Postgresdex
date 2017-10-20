#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
from config import config

# Finaliza la conexion recibida
def cerrar_conexion(conn):
	conn.close()
	print('Database connection closed.')
 
# Inicializa una conexion con la BDD segun el archivo
# database.ini 
def establecer_conexion():
	conn = None
	try:
		# Lectura de parámetros de configuración
		params = config()
		# Conectarse contra PostgreSQL
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)
		return conn
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

# Realiza una consulta usando la conexion abierta conn			
def realizar_consulta(conn, consulta):
	try:
		print "New query: " + consulta
		# Crea un cursor para realizar consultas
		cur = conn.cursor()	
		# Ejecuta la consulta
		cur.execute(consulta)
		# Muestra el resultado devuelto
		db_answ = cur.fetchall()
		print "Result: ", db_answ
		# Cierra el cursor
		cur.close()
		return db_answ
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
