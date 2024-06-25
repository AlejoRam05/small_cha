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
