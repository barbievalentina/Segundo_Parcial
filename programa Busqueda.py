"""Búsqueda: Escribe un programa en pseudocódigo que realice una búsqueda de un número dado, en un arreglo.
Crea una función modular para llevar a cabo la búsqueda."""

#Función para buscar el numero ingresado por el usuario dentro de la lista.
def funcion_busqueda(numero, numeros):
      #"len" sirve para determinar cuántos elementos tiene una lista, entonces el numero de elementos dentro de la lista se volverá el contador.
    for i in range(len(numeros)): 
        if numeros[i] == numero:
            #f sirve para concatenar datos str con variables numéricas, por ejemplo.
            return f"El número {numero} se encuentra en el arreglo en el índice {i}"
    return f"El número {numero} no se encuentra en el arreglo"

numero = int(input("Ingrese el número que desea buscar en el arreglo: "))
numeros = [20, 9, 6, 19, 5, 3, 55, 92, 97, 29, 10] #Estos son los valores que se encuentran dentro de la lista.
resultado = funcion_busqueda(numero, numeros)
#mostrará si el numero se encuentra en el arreglo o no.
print(resultado)
