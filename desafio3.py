"""Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada."""

vocales = ['a','e', 'i','o', 'u']
cadena = input('Ingresa una oracion o palabra: ').lower()



def contar_vocales(cadena: str)-> int:    
    contador = 0
    
    for i in cadena:
    
        if i in cadena:
            contador += 1
    
    return contador     

            
numero_vocales = contar_vocales(cadena)
print('Cuenta la cantidad de vocales')
print(cadena)
print(f'La cantidad de vocales es {numero_vocales}')

        
        
    
        

    