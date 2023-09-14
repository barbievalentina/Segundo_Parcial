#"primo" es una función que recibe un número del for en la línea 13 como argumento y devuelve true si es primo o false si no es primo.
def primo(numero): 
    if numero < 2: # Si el número es menor que 2, devuelve false porque los números primos lo son a partir del 2 en adelante.
        return False
    for i in range(2, numero): # Si el número es mayor a 2 entonces comprueba si es divisible por algún número entre 2 y el mismo numero.
        if numero % i == 0:
            return False
    return True

# Solicita al usuario que ingrese el rango para determinar que números son primos dentro de éste.
rango_inicio = int(input("Ingrese el rango inicial para determinar los numeros primos: ")) 
rango_final = int(input("Ingrese el rango final para determinar los numeros primos: "))

#Imprime los números primos encontrados dentro del rango.
print("Los números primos en el rango dado son: ")
for numero in range(rango_inicio, rango_final + 1):
    if primo(numero): # Si el número es primo, lo imprime
        print(numero)