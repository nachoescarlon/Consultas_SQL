import sqlite3
import pandas as pd

conexion = sqlite3.connect('mi_base_corporativa.db')
cursor = conexion.cursor()

# Actualización de presupuesto operativo
cursor.execute("UPDATE clientes_prospectos SET presupuesto = 85000 WHERE empresa = 'TechGlobal'")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contactos (
        id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa_ref TEXT NOT NULL,
        nombre TEXT,
        email TEXT
    )
''')
cursor.execute("DELETE FROM contactos")

# Inserción de ejecutivos de cuenta y cruce relacional
cursor.execute("INSERT INTO contactos (empresa_ref, nombre, email) VALUES ('TechGlobal', 'Ana Gómez', 'ana@techglobal.com')")
cursor.execute("INSERT INTO contactos (empresa_ref, nombre, email) VALUES ('AgroPlus', 'Luis Pérez', 'lperez@agroplus.com')")
conexion.commit()

consulta_join = '''
    SELECT clientes.empresa, clientes.presupuesto, contactos.nombre, contactos.email
    FROM clientes_prospectos AS clientes
    INNER JOIN contactos ON clientes.empresa = contactos.empresa_ref
'''
df_cruzado = pd.read_sql_query(consulta_join, conexion)
conexion.close()