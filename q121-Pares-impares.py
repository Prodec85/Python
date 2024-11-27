#Dada una lista de números, devolver los pares, devolver impares
import os

def pares_impares(nums):
    p=[]
    i=[]
    for n in nums:
        if n%2==0:
            p.append(n)
        else:
            i.append(n)
    return p, i


#Programa principal
os.system('cls')
nums = [9,8,60,6,90,7,10,6,7]
pares, impares = pares_impares(nums)
print('Números:',nums, len(nums))
print('Los pares son: ', pares, len(pares))
print('Los impares son: ', impares, len(impares))