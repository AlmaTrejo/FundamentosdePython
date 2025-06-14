def nuevoTema (tema): #crear una funcion
    print(f"\n ----- {tema}-----\n") 
    
if __name__ == "__main__":

    nuevoTema("Operadores Aritmeticos")
    print("Operador suma, 5+6=", 5 + 6 )    #
    print("Operador resta, 9-8=", 9 - 8 )
    print("Operador multiplicacion, 5*6=", 5 * 6 )  
    print("Operador division, 5+6=", 20 / 6 )
    print("Operador division entera, 30//4=", 30 //4)
    print("Operador potencia, 3**6=", 3**6 )
    print("Operador identidad, +6=", +6 )
    print("Operador cambio de signo, 6=", -6 )
    print("Operador modulo, 10%3=", 10%3 )
    #comentario de una linea
    '''comentario de 
    varias lineas'''

    nuevoTema("Operadores Logicos")
    print("True and True", True and True)
    print("True and False", True and False)
    print("False and True", False and True)
    print("False and False", False and False)
    print("not True", not True)
    print("not False", not False)
    print("True or True", True or True)
    print("True or False", True or False)
    print("False or True", False or True)
    print("False or False", False or False)
    
    nuevoTema("Operadores de Comparación")
    print(" 5 == 6:", 5==6 )
    print(" 5 != 6:", 5!=6 )
    print(" 5 > 6:", 5>6 )
    print(" 5 < 6:", 5<6 )
    print(" 5 >= 6:", 5>=6 )
    print(" 5 <= 6:", 5<=6 )

    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 6.2547
    Variable3 = "Pepe"
    nombreVariable = 0
    nombre_variable = 34.2
    print(variable1,_variable2, Variable3, nombreVariable, nombre_variable)
    
    a, b, c=5, 10.8, "Hola"
    print(a)
    print(b)
    print(c)
# ejemplo de variable dinamica
    nombre_variable ="Adios"
    print(nombre_variable)
    
    nuevoTema ("Enteros")
    w=185
    x = 49580938470387
    y = -254
    z = 0b00110011
    h = 0xFF
    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevoTema("Flotantes")
    x= 1297.5
    print(x, type(x))
    y= 0.50594
    print(y, type(y))
    
    nuevoTema ("Complejos")
    x=-45j
    y=12+45j
    z= 2j
    c= y + z
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(c, type(c))

    nuevoTema("Booleanos")
    x = True
    print(x, type(x))
    
    nuevoTema ("Listas") # similar al arreglo pero no es arreglo
    lista = [10, 20.5, "Lista de Python"] # las listas van en corchetes
    print(lista)  # las listas son iterables y ordenadas
    print(lista [1]) # imprime lo de la posicion 1 la lista
    lista [0]= "Hola"
    lista.append(34) #append permite crecer la lista al final
    print(lista)
    lista.insert(0, 1.1) # insert permite insertar en una posicion especifica
    print(lista)
    lista.append([3, 4, 5, 6, 7, 8])
    print(lista)
    print(lista[5])
    print(lista [5][4]) # de la lista 5 imprime el elemento 4
    print(lista [3][4]) # de la lista 3 imprime el elemento 4
     
    nuevoTema ("Tuplas") # lista de constantes
    tupla = (25, "Tupla", 1+10) # una vez creada no se puede modofocar
    print(tupla) #estan indexadas u ordenadas
    print(tupla[1]) # no soporta asignacion de objetos porque es inmutable
    tupla = (25, "Tupla", 1+10, "Otro") #nos e modifica solo se crea otro espacio de memoria
    print(tupla)

    nuevoTema("Conjuntos")
    conjunto=[10,20,30,40,50,20]
    print(conjunto) #utiles para cuando no quieres repetir vLORES
    #no es iterable u ordenado no se puede imprimri una posición del conjunto no estan indizados
    #conjunto.add(80)
    #print (conjunto)
    print(50 in conjunto)
    nuevoTema ("Diccionarios")
    diccionario = {"Nombre": "Alma",
                   "edad": 40,
                   "Telefono":1236576}
    print(diccionario)
    print(diccionario["Nombre"])


