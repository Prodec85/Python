#Funciones para otros programas

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

def promedio(nums):
    s = 0
    for n in nums:
        s+=n
    return s / len(nums)

pi = 3.1416
gt = 9.7242343

def leerdatos():
    datos=[]
    while True:
        d = int(input('Número: '))
        if d==-1: break
        datos.append(d)
    return datos

def leerdatos2():
    datos=[]
    while True:
        d = int(input('Dame un número entre 1 y 7:  '))
        if d < 1 or d > 7:
            print('< Número fuera de rango >')
        datos = d
        return datos
    
def inchtocc():
    inch = int(input('Cuantas pulgadas? '))
    cc=inch*2.54
    return (f'{inch} pulgadas equivalen a {cc} centrímetros')

def metft():
    mt = int(input('Cuantos metros? '))
    ft=mt*3.281
    return (f'{mt} metros equivalen a {ft} pies.')

def suma_pares_impares(inicio, fin, tipo):
    suma = 0
    for num in range(inicio, fin + 1):
        if tipo.upper() == 'P' and num % 2 == 0:
            suma += num
        elif tipo.upper() == 'I' and num % 2 != 0:
            suma += num
    return suma

def leer_arreglo():
    entrada = input("Dame los números separados por espacio: ")
    lista_numeros = list(map(int, entrada.split()))
    return lista_numeros

def suma_digitos(numero):
    return sum(int(digit) for digit in str(numero))

def suma_digitos_lista(lista):
    return [suma_digitos(num) for num in lista]

def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return factorial

def factoriales_lista(lista):
    return [calcular_factorial(num) for num in lista]

def mayor2(lista):
    return max(lista)

def menor02(lista):
    return min(lista)

def media(lista):
    return sum(lista) / len(lista)

def varianza(lista):
    media_lista = media(lista)
    return sum((x - media_lista) ** 2 for x in lista) / len(lista)

def desviacion_estandar(lista):
    return varianza(lista) ** 0.5