# Se hablilita el trabajo con el sistema operativo
import os

# Obtener la ruta de trabajo actual
# (Current Working Directory)
ruta=os.getcwd()
print(ruta)

# Obtiene el valor absoluto de la ruta
ruta_absoluta=os.path.abspath(ruta)
print(ruta_absoluta)

# Se asume que el archivo colores.txt no existe en el
# directorio de trabajo.
archivo="colores.txt"

# Informa si el archivo existe o no existe.
if os.path.exists(archivo):
    print("\nEl archivo ya existe")
else:
    print("\nEl archivo no existe")

# Si el archivo existe, lo borra
archivo="colores.txt"

# Si el archivo existe, lo elimina.
# Informa qué se hizo.
if os.path.exists(archivo):
    os.remove(archivo)
    print("\nEl archivo se eliminó")
else:
    print("\nEl archivo no existe. No se eliminó nada.")

# Se abre un archivo en modo Append Extended (a+). Si el archivo no
# existe, lo crea, con capacidad de lectura y escrituta. El
# apuntador de escritura se coloca al final del archivo.
archivo="colores.txt"

f = open(archivo,"a+")
# Verificación de que ya se creo.
if os.path.exists(archivo):
    print("\nEl archivo ya existe")
else:
    print("\nEl archivo no existe")
# Se cierra el archivo.
f.close()

# Abro el archivo en modo Write Extended.
# Si el archivo no existe, lo genera. Si existe, lo remplaza.
# Los contenidos van en secuencia.
archivo="colores.txt"
f = open(archivo,"w+")

# Escribo 4 contenidos en secuencia.
f.write("Azul")
f.write("Amarillo")
f.write("Rojo")

# Cierro el archivo.
f.close()

# Para saltos de línea, se utiliza \n
# Abro el archivo en modo Write Extended
archivo="colores.txt"
f = open(archivo,"w+")

# Escribo 4 líneas adicionales.
f.write("Rojo\n")
f.write("Amarillo\n")
f.write("Verde\n")

# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)

# Cierro el archivo.
f.close()

# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")

# Leo el contenido y se lo asigno a la variable
# contenido.
contenido=f.read()

# Muestro el contenido. Debe ser todo el archivo.
print(contenido)

# Cierro el archivo.
f.close()

# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")

# Leo únicamente los primeros 5 caracteres del archivo.
contenido=f.read(5)

# Muestro el contenido
print(contenido)

# Leo otros 5 caracteres del archivo.
contenido=f.read(5)

# Muestro el contenido
print(contenido)

# Cierro el archivo.
f.close()

# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")

# Leo únicamente la primer línea del archivo.
contenido=f.readline()

# Muestro el contenido
print(contenido)

# Leo siguiente línea
contenido=f.readline()

# Muestro el contenido
print(contenido)

# Cierro el archivo.
f.close()

# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")

# Leo únicamente los primeros 5 caracteres del arvhivo.
for linea in f:
    print(">", linea)

# Cierro el archivo.
f.close()

with open("colores.txt","r") as f:
    contenido=f.read()
    print(contenido)

# Datos iniciales. Entradas es una lista que contiene listas.
Entradas=[
    ['correo','nombre','telefono'],
    ['juan@gmail.com','Juan','8123232323'],
    ['maria@gmail.com','Maria','5545454545'],
    ['diana@homail.com','Diana','4490909090']
]
for e in Entradas:
    print(f'{e[0]}|{e[1]}|{e[2]}')

# Se imprime el contenido de la lista, para cotejar.
print(">> Contenido de la lista.\n")
print(Entradas)

# Revisa si existe el CSV, en cuyo caso, si existe el BAK lo elimina
# y renombra el CSV como BAK
if os.path.exists("agenda.csv"):
    if (os.path.exists("agenda.bak")):
        os.remove("agenda.bak")
        os.rename("agenda.csv","agenda.bak")
    else:
        os.rename("agenda.csv","agenda.bak")

# Se escribe el contenido de la lista, usando with y F-String
with open("agenda.csv","w+") as f:
    for e in Entradas:
        f.write(f"{e[0]}|{e[1]}|{e[2]}\n")

# Se revisa el contenido del archivo.
print("\n>> Contenido del archivo.\n")
with open("agenda.csv") as f:
    print(f.read())