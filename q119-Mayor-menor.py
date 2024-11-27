# Dada una lista de números introducida por el usuario, regresa el mayor y menor
def leerdatos():
    datos=[]
    while True:
        d = str(input('Número: '))
        if d=='*': break
        datos.append(d)
    return datos

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

#Programa principal
import os;os.system('cls')
nums = leerdatos()
print (nums)
may = mayor(nums)
print ('El mayor res: ', may)
men = menor(nums)
print ('El menor res: ', men)