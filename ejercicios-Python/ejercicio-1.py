# Ejercicio: Calcular el promedio de una lista de números

def calcular_promedio(lista):
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

numeros = [4, 7, 2, 9, 12, 5]
promedio = calcular_promedio(numeros)
print("El promedio de la lista es:", promedio)
