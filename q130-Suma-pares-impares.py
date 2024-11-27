#Redibe tres parámetros: dos números (un rango), una letra P o I y regresa la suma de números pares o impares en el rango de números especificados

import os;os.system('cls')
import q124_Funciones as f

while True:
    print("\nMenú de Suma: ")
    print("1. Sumar números pares. ")
    print("2. Sumar números impares. ")
    print("3. Salir ")
    
    opcion = input("Selecciona una opción: [1] [2] [3] ")

    if opcion == '3':
        print("Saliste del programa ")
        break
    elif opcion in ['1', '2']:
        inicio = int(input("Ingresa el número de inicio: "))
        fin = int(input("Ingresa el número de fin: "))
        tipo = 'P' if opcion == '1' else 'I'
        suma = f.suma_pares_impares(inicio, fin, tipo)
        tipo_str = "pares" if tipo == 'P' else "impares"
        print(f"La suma de los números {tipo_str} en el rango de {inicio} a {fin} es: {suma}")
    else:
        print("Opción inválida ")