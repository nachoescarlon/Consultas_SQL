import sqlite3
import pandas as pd

# 1. Nos conectamos a la base que ya existe
conexion = sqlite3.connect('mi_base_corporativa.db')
cursor = conexion.cursor()

# 2. UPDATE: Aumentamos el presupuesto de TechGlobal de 50000 a 85000
cursor.execute("UPDATE clientes_prospectos SET presupuesto = 85000 WHERE empresa = 'TechGlobal'")
conexion.commit()

# 3. Creamos una segunda tabla para agendar a los contactos directos de esas empresas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contactos (
        id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa_ref TEXT NOT NULL,
        nombre TEXT,
        email TEXT
    )
''')

# Limpiamos la tabla de contactos por si ejecutas el script más de una vez
cursor.execute("DELETE FROM contactos")

# Insertamos a las personas de contacto
cursor.execute("INSERT INTO contactos (empresa_ref, nombre, email) VALUES ('TechGlobal', 'Ana Gómez', 'ana@techglobal.com')")
cursor.execute("INSERT INTO contactos (empresa_ref, nombre, email) VALUES ('AgroPlus', 'Luis Pérez', 'lperez@agroplus.com')")
conexion.commit()

# 4. JOIN: Cruzamos la tabla de empresas original con la nueva tabla de contactos
consulta_join = '''
    SELECT 
        clientes.empresa, 
        clientes.presupuesto, 
        contactos.nombre, 
        contactos.email
    FROM clientes_prospectos AS clientes
    INNER JOIN contactos ON clientes.empresa = contactos.empresa_ref
'''

df_cruzado = pd.read_sql_query(consulta_join, conexion)

print("Resultado de las tablas cruzadas con JOIN:")
print(df_cruzado)

conexion.close()