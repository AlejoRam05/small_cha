"""Ordenar lista: Escribe un programa que ordene una lista de números dada por el usuario en orden acendente"""
def ordenar():
    
    lista = []
    
    while True:
        print("Si ya no desea ingresar datos presiona (enter)")
        entrada = input("ingrese un número: ")  
        
        if entrada == "":
            break  
        
        try:
            numero = float(entrada)
            lista.append(numero)
            
        
        except ValueError:
            print("El dato no es valido, Por favor ingrese un número.")
    
    lista_ordenada = sorted(lista)  
    return lista_ordenada     
        

lista_ordenada = ordenar()

print("La lista ordenada de forma acendente: ", lista_ordenada)


