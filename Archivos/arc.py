file = open("EjemploArchivo.txt" , "w")
file.write("Este es el contenido del archivo.")
file.close()

lista =["Fresa", "Mango", "Papaya"]
with open ("EjemploArchivo.txt", "a") as file:
    for e in lista:
        file.write(e + "\n")
print("Lista escrita en el archivo")

lista2 = ["Honda","Sizuki","BMW"]
    file.writelines(lista2, "") as file:
print("Lista escrita con writelines")

with open ("EjemploArchivo.txt". "r")

print("Leer dos lineas y posteriormente 5 caracteres")
with open ("EjmeploArchivo.txt", "r")


print("Almacenar el contenido en una lista")


