# Ejercicio: Encontrar el número mayor y menor en una lista

def encontrar_extremos(lista):
    if len(lista) == 0:
        return None, None
    else:
        mayor = menor = lista[0]
        for numero in lista:
            if numero > mayor:
                mayor = numero
            if numero < menor:
                menor = numero
        return mayor, menor



numeros = [12, 5, 23, 8, 19, 3]
mayor, menor = encontrar_extremos(numeros)
print("El número mayor es:", mayor)
print("El número menor es:", menor)
