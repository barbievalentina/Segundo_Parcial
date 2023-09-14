"""Calculadora Modular: Crea un programa que permita realizar operaciones matemáticas
básicas (suma, resta, multiplicación y división) utilizando funciones modulares para cada
operación."""

#Función para suma
def suma(numero1, numero2):
    numero1 = float(numero1)
    numero2 = float(numero2)
    return f"El resultado de la suma es: {numero1 + numero2}"

#Función para resta.
def resta(numero1, numero2):
    numero1 = float(numero1)
    numero2 = float(numero2)
    return f"El resultado de la resta es: {numero1 - numero2}"

#Función para multiplicación.
def multiplicacion(numero1, numero2):
    numero1 = float(numero1)
    numero2 = float(numero2)
    return f"El resultado de la multiplicación es: {numero1 * numero2}"

#Función para división.
def division(numero1, numero2):
    numero1 = float(numero1)
    numero2 = float(numero2)
    return f"El resultado de la división es: {numero1 / numero2}"


#Se pide al usuario que ingrese el tipo de operación que desea realizar.
operaciones = int(input("Por favor ingrese el tipo de operación que desea realizar: 1=Suma 2=Resta 3=Multiplicación 4=División "))
if operaciones<1:
    print("El número ingresado no es válido.") 
elif operaciones>4:
    print("El número ingresado no es válido.")
#Se pide al usuario los dos números con los que se va a realizar la operación.
else: 
    numero1 = float(input("Ingrese el 1° número: "))
    numero2 = float(input("Ingrese el 2° número: "))

#Dependiendo del tipo de operación que desea realizar el usuario la condición será diferente.
if operaciones == 1:
    print(suma(numero1, numero2))
elif operaciones == 2:
    print (resta(numero1, numero2))
elif operaciones == 3:
    print (multiplicacion(numero1, numero2))
elif operaciones == 4:
    print(division(numero1, numero2))