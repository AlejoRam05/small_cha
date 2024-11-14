"""Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable (entre 8 y 16 caracteres) 
que incluya letras mayúsculas, minúsculas, números y símbolos."""

import random
import string

def generar_contraseña(longitud):
    # Asegúrate de que la longitud esté entre 8 y 16 caracteres
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres.")
    
    # Define los caracteres que vamos a usar
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Crear una lista de todos los posibles caracteres
    todos_los_caracteres = letras_mayusculas + letras_minusculas + numeros + simbolos
    
    # Generar la contraseña asegurando que tenga al menos un carácter de cada tipo
    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Rellenar el resto de la contraseña con caracteres aleatorios
    for _ in range(longitud - 4):
        contraseña.append(random.choice(todos_los_caracteres))
    
    # Mezclar la contraseña para que no siga un patrón
    random.shuffle(contraseña)
    
    # Convertir la lista en una cadena
    return ''.join(contraseña)

# Ejemplo de uso:
try:
    longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16 caracteres): "))
    contraseña = generar_contraseña(longitud)
    print(f"Contraseña generada: {contraseña}")
except ValueError as e:
    print(e)
