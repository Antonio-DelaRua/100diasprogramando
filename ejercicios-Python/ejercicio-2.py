# Ejercicio: Verificar si una palabra es un palíndromo

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas
    palabra = palabra.replace(" ", "")  # Eliminar espacios en blanco

    # Verificar si la palabra es igual a su inversa
    if palabra == palabra[::-1]:
        return True
    else:
        return False


palabra = input("Ingresa una palabra: ")
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
