"""
Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros utilizando cualquier método de ordenamiento 
que prefieras (por ejemplo, burbuja, inserción, selección).
"""
# Utilizando Ordenamiento burbuja
def orden(lista: list) -> list:
    
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n-i-1):
            
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista



numeros = [57, 29, 85, 14, 92, 36, 75, 68, 13, 42]
        
lista_ordenada = orden(numeros)
print(lista_ordenada)