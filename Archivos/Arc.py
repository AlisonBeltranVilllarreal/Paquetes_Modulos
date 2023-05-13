file = open("./Archivos/EjemploArchivo.txt", "w")
file.write("Este es el contenido del archivo \n")
file.close()

lista = ["Fresa", "Kiwi", "Papaya"]

with open("EjemploArchivo.txt", "a") as file:
    for e in lista:
        file.write(e + "\n")

print("Archivo escrito")

lista2 = ["Honda" , "Suzuki", "BMW"]

with open("EjemploArchivo.txt", "a") as file:
    file.writelines(lista2)

print("lista escrita con writelines")

print("Imprimir todo el contenido del archivo. ")
with open("EjemploArchivo.txt", "r") as file:
    print(file.read())

print("Leer archivo linea por linea")
with open("EjemploArchivo.txt", "r") as file:
    print(file.readline())
    print(file.readline()) #lee linea por linea
    print(file.readline())
    print(file.readline(2)) #lee solo los primeros dos caracteres

print("Guardar el contenido del archivo en una lista")
with open("EjemploArchivo.txt", "r") as file:
    contenido= file.readlines() #cada linea la guarda como un elemento de una lista
    print(contenido)