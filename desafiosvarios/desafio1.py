"""Invertir una cadena de caracteres"""

#utilizamos recursividad
def invertir_caracteres(caracter):
    if len(caracter) == 0: return ""
    else: return caracter[-1]+ invertir_caracteres(caracter[:-1])
    
caracter = input("Ingrese una palabra: ")
print(caracter)
print(invertir_caracteres(caracter))




"""Otra manera de hacer usando listas"""
caracter = list(input('Ingresa una palabra: '))

print(caracter)
caracter.reverse()
print(caracter)
