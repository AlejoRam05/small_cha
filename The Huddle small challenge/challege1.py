"""Búsqueda en lista ordenada: 
Implementa una función de búsqueda binaria que determine si un número está en una lista ordenada de 10 elementos."""


# DEFINIMOS UNA FUNCION DE BUSQUEDA
def binary_search_parameter(LOW, HIGHT, A:list, x:int) -> int:
    """Busca en una lista ordenada el obejtivo -> "x" """
    # caso base, si no existe el elemento en la lista retorna -1
    if LOW > HIGHT: return -1
    
    #CALCULAMOS EL PUNTO MEDIO DE LA LSITA
    mid = (LOW + HIGHT) // 2
    
    if A[mid] == x: #En caso que se encuentre en el medio 
        return mid
    # Si el elemento medio es mayor que x, buscar en la mitad inferior
    elif A[mid] > x:
        return binary_search_parameter(LOW,mid -1 , A, x) #cambiamos la entrada "HIGHT"
    
    else:
        return binary_search_parameter(mid +1, HIGHT, A, x) #cambiamos la entrada "LOW"
    

def call_search(A:list, x: int):
    return binary_search_parameter(0, len(A) -1 , A, x)


A = [3, 11, 18, 27, 34, 45, 58, 72, 89]
x = int(input("Ingrese el número que estas buscando: "))
result = call_search(A, x)

print(f"El número {x}, se encuentra en el indice {result}" if result != -1 else f"El elemento no pertenece a la lista {A}")