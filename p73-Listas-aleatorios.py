# Generar dos listas de números aleatrorios, elevarlos al cuadrado y sumarlas en una tercera
import os, random; os.system("cls")

A = []
B = []
C = []

n = int(input('Cuantos elementes por lista? '))
print('Generando aleatrorios...')
for x in range(n):
    A.append(random.randint(1,10))
    B.append(random.randint(1,10))
print('A = ', A)
print('B = ', B)

print()


for x in range(n):
    A[x]=A[x]*A[x]
    B[x]=B[x]*B[x]
    C.append(A[x]+B[x])

    
print('A = ', A)
print('B = ', B)
print('C = ', C)