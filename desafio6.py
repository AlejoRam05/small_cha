"""Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora."""

import random

def obtener_eleccion_computadora():
    elecciones = ["piedra", "papel", "tijeras"]
    return random.choice(elecciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def juego_piedra_papel_tijeras():
    usuario = input("Elige piedra, papel o tijeras: ").lower()
    if usuario not in ["piedra", "papel", "tijeras"]:
        print("Elección no válida. Por favor elige piedra, papel o tijeras.")
        return

    computadora = obtener_eleccion_computadora()
    print(f"La computadora eligió: {computadora}")

    resultado = determinar_ganador(usuario, computadora)
    print(resultado)

# Iniciar el juego
juego_piedra_papel_tijeras()
