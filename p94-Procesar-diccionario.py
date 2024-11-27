# Crear diccionario de dos listas e iterar..
import os; os.system('cls')
nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
datos=dict(zip(nombres,sueldos))
print(datos)
suma=0
print('\nNombres:')
for n in datos.keys():
    print(f'{n:15}')
   
print('\nSueldos:')
for s in datos.values():
    print(f'${s:,.2f}')

print('\nLlaves y valores al mismo tiempo')
for k in datos.keys():
    print(f'{k:<15} : {datos[k]}')


print('\nNombre y Sueldos:')
for n,s in datos.items():
    suma = suma + s
    print(f'{n:8}  -  ${s:,.2f}')
print(f'\nSuma: ${suma:,.2f}  -  Promedio: ${suma/len(datos):,.2f}')