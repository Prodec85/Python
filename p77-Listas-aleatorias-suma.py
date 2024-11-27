# Suma los elementos impares de dos listas
import os, random; os.system("cls")
A = []
B = []
C = []
while True:
    A.clear()
    B.clear()
    C.clear()    
    for x in range(10):
        A.append(random.randint(1,10))
        B.append(random.randint(1,10))
    print('A = ', A)
    print('B = ', B)
    for x in range(10):
        if A[x]%2!=0 and B[x]%2!=0:
            C.append(A[x]+B[x])
        else:
            C.append(0)
    print('C = ', C)
    if input("Deseas continuar (S/N)").upper().startswith("N"):break