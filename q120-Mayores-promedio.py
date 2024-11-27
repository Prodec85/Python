#Calcula el promedio de una lista, luego regresa los que son mayores al promedio

def promedio(nums):
    s = 0
    for n in nums:
        s+=n
    return s / len(nums)

def mayoresprom(nums,prom):
    mp = []
    for n in nums:
        if n > prom:
            mp.append(n)
    return mp

def leerdatos():
    datos=[]
    while True:
        d = int(input('Número: '))
        if d==-1: break
        datos.append(d)
    return datos

#Programa principal
import os;os.system('cls')
nums=leerdatos()
print(nums)
prom = promedio(nums)
print('Promedio:', prom)
mayprom= mayoresprom(nums, prom)
print(mayprom, len(mayprom))