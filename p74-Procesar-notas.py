#  Procesa una lista de notas introducidas por el usuario y calcula suma de notas, promedio, menores al promedio, máxima y mínima
import os; os.system("cls")
n = 1
suma = promedio = 0
nums = []
while n!=0:
    n = float(input("Captura la nota entre 1 y 100. (0 para terminar captura)  "))
    if n>=1 and n<=100:
        nums.append(n)
    else:
        print(f" {"< Nota fuera de rango >" if n != 0 else ""} ")
print('< Fin de captura >')
for n in nums:
    suma+=n
promedio = suma/ len(nums)
mp=[]
for n in nums:
    if n < promedio:
        mp.append(n)
print(f"\nCapturaste {len(nums)} notas, que son             : {nums}" )
print('La suma de las notas es                 :', suma)
print('El promedio es                          :', promedio)
print(f'Hay {len(mp)} notas menores al promedio, y son  :', mp, )
print('Mayor y menor                           :', max(nums), min(nums))