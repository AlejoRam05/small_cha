'''Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.'''
print('Tablas de multiplicar del numero que quieras')
n = int(input('Ingresa el numero que quieras: '))
for i in range(1,11): #itera del 1 al 10
    # Usamos f (format) para estirar las variables que estamos necesitando
    print(f'{n}x{i} = {n*i}') 
    #Imprime los numeros y resultados
    
