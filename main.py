# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:  # Abre (o crea) el archivo 'my_notes.txt' en modo de escritura ('w').
    file.write("tengo clase hoy.\n")  # Escribe la primera línea en el archivo con un salto de línea al final.
    file.write("tengo que hacer deberes.\n")  # Escribe la segunda línea con otro salto de línea.
    file.write("tengo que salir.\n")  # Escribe la tercera línea con un salto de línea al final.
# El archivo se cierra automáticamente al salir del bloque 'with'.

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:  # Abre el archivo 'my_notes.txt' en modo de lectura ('r').
    line = file.readline()  # Lee la primera línea del archivo y la guarda en la variable 'line'.
    while line:  # Mientras la variable 'line' contenga una línea, sigue ejecutando el ciclo.
        print(line.strip())  # Imprime la línea, eliminando los saltos de línea extra con 'strip()'.
        line = file.readline()  # Lee la siguiente línea del archivo y repite el proceso hasta llegar al final.
# El archivo también se cierra automáticamente al salir del bloque 'with'.


