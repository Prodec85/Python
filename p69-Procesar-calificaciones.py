#  Procesa una lista de calificaciones introducidas por el usuario

import os; os.system("cls")

# nums = [9.5,10,7,6,4.5,8.5,10,7,5]
n = suma = promedio = 0
nums = []

while n!=99:
    n = float(input("Número?"))
    if n>=0 and n<=10:
        nums.append(n)
    else:
        print('x')
print('< Fin de captura >')


for n in nums:
    suma+=n
promedio = suma/ len(nums)

mp=[]
for n in nums:
    if n > promedio:
        mp.append(n)
print("\nLas calificaciones son: ", nums, len(nums))
print('La suma es              :', suma)
print('El promedio es          :', promedio)
print('Mayores al promedio es  :', mp, len(mp))
print('Mayor y menor           :', max(nums), min(nums))
nums.sort(reverse=True)
print('Ordenada                :', nums)
nums.reverse()
print('Ordenada                :', nums)