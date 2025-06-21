import pickle

info=[35, 56, 3.14, 16]

with open ("./Archivos/ArchivoSerial", "wb") as binFile: # . indica la raiz de donde se ejecuta
    pickle.dump (info, binFile)

    print("Archivo binario escrito")

    with open("./Archivos/ArchivoSerial", "rb") as binFile:
        lista = pickle.load(binFile)
        print(lista)
    print("Archivo binario leido y reconstuido")