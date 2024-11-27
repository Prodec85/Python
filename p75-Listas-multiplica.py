# Sumar dos listas de números introducidas por el usuario


import os; os.system("cls")



A = []
B = []
C = []

print('Capturar elementos de liasta A')
for i in range(5):
    n = int(input(f"Elemento {i+1}:  "))
    A.append(n)

print('Capturar elementos de liasta B')
for i in range(5):
    n = int(input(f"Elemento {i+1}:  "))
    B.append(n)
print('\nMultiplicación de listas  A x B = C')
print("A = ", A)
print("B = ", B)



for i in range(5):
    C.append(A[i] * B[i])
print("C = ", C)