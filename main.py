# Diccionario inicial con información ficticia
informacion_personal = {
    "nombre": "Clinton Alvarado",
    "edad": 25,
    "ciudad": "Coca",
    "profesion": "ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"  # Cambiamos la ciudad a una diferente

# Modificar la profesión
informacion_personal["profesion"] = "Desarrollador de software"  # Modificamos la profesión

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0979923493"  # Si no existe, la agregamos con un número ficticio

# Eliminar la clave "edad" del diccionario, ya que no es necesaria
informacion_personal.pop("edad", None)  # Usamos pop para eliminar "edad" si existe, ignorando errores

# Imprimir el diccionario final después de todas las operaciones
print(informacion_personal)