#Dada una lista de números, regresa los pares
import os

def pares(lista):
    p = []
    for n in  lista:
        if n % 2 == 0:
            p.append(n)
    return(p)
# Programa principal
os.system('cls')
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print (nums)
res = pares(nums)
print(type(res))
print(res)