# Pokédex basada en PostgreSQL

## Pasos previos

- Tener en Postgres una BDD llamada *MyDB*, con usuario y contraseña *postgres*. También se pueden elegir otras opciones, pero debe modificarse de forma acorde el archivo *database.ini*.
- Correr sobre la BDD el script *script_creacion.sql* para inicializar todas las tablas.
- Instalar para Python **Psycopg 2**, paquete que hace de adaptador de Python a PostgreSQL: `pip install psycopg2`. También es posible que tengan que descargar **Tkinter** si no lo bajaron antes.

## Comprobar la conexión con PostgreSQL

Una vez realizados los pasos previos, se puede probar que la conexión con PostgreSQL esté bien configurada. Para ello, abrir una terminal de Python en el directorio donde está el código e intentar importar *psycopg 2*: `import psycopg2`. Si el import sale bien, se puede probar directamente la conexión con PostgreSQL usando el módulo *conexion.py*:

```python
>>> from conexion import *
>>> conn = establecer_conexion()
Connecting to the PostgreSQL database...
```

El objeto recibido *conn* debería poder utilizarse directamente para resolver consultas sobre la BDD:

```python
>>> realizar_consulta(conn, "SELECT * FROM tipo")
New query: SELECT * FROM tipo
Result:  [('Normal',), ('Electric',), ('Psychic',), ('Dark',), ('Fire',), ('Grass',), ('Water',)]
```

Es importante cerrar siempre la conexión. De lo contrario, la BDD podría quedar lockeada y futuras conexiones podrían fallar:

```python
>>> cerrar_conexion(conn)
Database connection closed.
```

## Correr la aplicación

Para correr la aplicación, simplemente ejecutar `python ./main.py`. La aplicación por el momento muestra una lista de unos pocos pokémon con algunos capturados. Se puede navegar la lista con las flechas arriba y abajo. La tecla ESC finaliza la aplicación.


