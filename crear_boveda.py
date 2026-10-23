import sqlite3

conexion = sqlite3.connect('pipeline_ventas.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS prospectos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        email TEXT,
        fecha_captura DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

conexion.commit()
conexion.close()

print("Bóveda 'pipeline_ventas.db' y tabla 'prospectos' creadas con éxito.")