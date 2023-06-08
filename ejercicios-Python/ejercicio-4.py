# Ejercicio: Contar la frecuencia de palabras en un texto

def contar_palabras(texto):
    palabras = texto.lower().split()  # Convertir el texto a minúsculas y dividirlo en palabras
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme"
resultado = contar_palabras(texto)
for palabra, frecuencia in resultado.items():
    print(f'La palabra "{palabra}" aparece {frecuencia} veces.')
