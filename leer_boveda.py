import sqlite3
import pandas as pd

conexion = sqlite3.connect('pipeline_ventas.db')

consulta_sql = "SELECT * FROM prospectos"

tabla_datos = pd.read_sql_query(consulta_sql, conexion)

conexion.close()

print("Bóveda abierta. Estos son los prospectos guardados oficialmente:")
print(tabla_datos)