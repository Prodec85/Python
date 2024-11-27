# Crea una lista de números imparse de 1 a n y suma, promedia y busca números en la lista
import os;
num = []
div=[]
suma=0
sum=0
bus=0
pos=0

import os;
while True:
    os.system("cls")
    num.clear()
    n = int(input("A qué número deseas llegar? "))
    for i in range(1,n+1,2):
        num.append(i)     
    print(num)
    for x in range(len(num)):
        suma=suma+(num[x])
    print(f'La suma de los números es: {suma}')
    print(f'El promedio de los números es: {suma/(len(num))}')
    for z in range(len(num)):
        if (num[z])%3==0:
            div.append(num[z])
            sum=sum+(num[z])
    print(f'Hay {len(div)} números divisibles entre 3 y son {div} que sumados dan: {sum}' )
    bus=int(input('Qué elemento buscas? '))
    if bus in num:
        pos=num.index(bus)
        print(f'{bus} sí está en la lista en la posición {pos+1}. ')

    else:
        print(f'{bus} No está en la lista ')    
    
    
    if input("\nDeseas continuar (S/N)").upper().startswith("N"):break
print("\nProceso terminado")