"""Crear un Diccionario
Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores."""


def crear_diccionario(claves, valores):
    if len(claves) != len(valores):
        raise ValueError("Las listas de claves y valores deben tener la misma longitud.")
    
    diccionario = {}
    for i in range(len(claves)):
        diccionario[claves[i]] = valores[i]
    
    return diccionario

# Ejemplo de uso:
claves = ["a", "b", "c"]
valores = [1, 2, 3]

diccionario = crear_diccionario(claves, valores)
print(diccionario)

"""Conversión de Temperatura:
Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit."""
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Ejemplo de uso:
celsius = float(input("Ingrese el valor de la temperatura en grados celsius (0º a 100º: " ))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
