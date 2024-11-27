#Diccionario días de la semana.
import os; os.system('cls')

sem = {1: 'Domingo',2: 'Lunes',3:'Martes',4:'Miercoles',5:'Jueves',6:'Viernes',7:'Sabado'}

print(sem)

print(f'El primer día es: {sem[1]}')
print(f'El último día es: {sem[7]}')
print(f'El quinto día de la semana es  : {sem.get(5)}')
print(f'El séptimo día de la semana es : {sem.get(7)}')

print(sem)