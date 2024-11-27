# Cuenta los caracteres y devuelve un diccionario con la catidad de apariciones.

import os; os.system("cls")


oracion = input("Introduce una oracion: ")


num_car = {}


for caracter in oracion:
    if caracter in num_car:
        num_car[caracter] += 1  
    else:
        num_car[caracter] = 1   


print('Conteo de caracteres:', num_car)