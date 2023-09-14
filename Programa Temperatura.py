"""Conversión de Temperatura: Crea un programa en pseudocódigo que permita convertir
entre Celsius y Fahrenheit. Crea dos funciones modulares: una para convertir de Celsius a
Fahrenheit y otra para convertir de Fahrenheit a Celsius. """

#Función para transformar los grados Fahrenheit a Celsius.
def gradosF(grados):  
    resultado=(grados-32)/1.8 
    return resultado

#Función para transformar los grados Celsius a Farehenheit.
def gradosC(grados):
    resultado=(grados*1.8)+32
    return resultado

#Algoritmo Principal.
#Se pide el tipo de grado que se desea convertir.
tipo_grados=int(input("Ingrese el tipo de grados que desea transformar:\n1=Fahrenheit\n2=Celsius\n"))

#Según el tipo de grado que se desea transformar se realizara una función diferente.
if tipo_grados==1:
    grados=int(input("Ingrese cuantos grados Fahrenheit quiere transformar a grados Celsius: "))
    F=gradosF(grados) #F es la variable donde se guarda el resultado de la función.
    print (grados, "F° es igual a", F, "C°.")
elif tipo_grados==2:
    grados=int(input("Ingrese cuantos grados Celsius quiere transformar a grados Fahrenheit: "))
    F=gradosC(grados) #F es la variable donde se guarda el resultado de la función.
    print (grados, "C° es igual a", F, "C°.")
else:
    print ("La opción ingresada es inexistente.")