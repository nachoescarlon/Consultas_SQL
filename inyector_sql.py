import requests
import sqlite3

conexion = sqlite3.connect('pipeline_ventas.db')
cursor = conexion.cursor()

print("Iniciando extracción e inyección directa a la base de datos...")

for viaje in range(5):
    respuesta = requests.get("https://randomuser.me/api/")
    paquete = respuesta.json()
    
    nombre = paquete["results"][0]["name"]["first"]
    apellido = paquete["results"][0]["name"]["last"]
    email = paquete["results"][0]["email"]
    
    cursor.execute('''
        INSERT INTO prospectos (nombre, apellido, email) 
        VALUES (?, ?, ?)
    ''', (nombre, apellido, email))
    
    print("Prospecto inyectado en SQL:", nombre, apellido)

conexion.commit()
conexion.close()

print("\nPipeline ETL completado. 5 prospectos nuevos asegurados en la bóveda.")