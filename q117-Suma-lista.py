#Suma una lista de números usando una función
import os;
os.system('cls')
def suma_lista(lista):
    s =0 
    for n in lista:
        s += n
    return s
#Programa principal
nums = [10,20,30,40,50]
res = suma_lista (nums)
print( f'La suma de la lista es {res}')