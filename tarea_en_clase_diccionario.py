# Crear una lista vacía para almacenar los libros
libros = []

# Capturar los datos del libro desde el teclado
nombre_libro = input("Un grito desesperado: ")
categoria = input("diamante: ")
año_publicacion = input("2005: ")
numero_paginas = input("300: ")
autor = input("Carlos Cauthemoc Sanches: ")

# Guardar los datos del libro en un diccionario y añadirlo a la lista de libros
libro = {
    "Un grito desesperado": nombre_libro,
    "diamante": categoria,
    "2005": año_publicacion,
    "300": numero_paginas,
    "Carlos Cauthemoc Sanches": autor
}
print(libro)



