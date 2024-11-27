# Crea una lista de ciudades y separa las que comienzan con vocales
import os; os.system("cls")
ciudades=[]
num = 0
cdc=[]
cdv=[]

while True:
    ciudad = input('Introduce nomre de una ciudad (introduce $ para terminar)  ')
    if ciudad !='$':
        ciudades.append(ciudad)
       
    else:
        break
print('Ciudades :', ciudades)
ciudades.sort()
print(f'Las {(len(ciudades))} ciudades en orden alfabético son:', ciudades)
num = (len(ciudades))
for x in range(num):
    cd=ciudades[x]
    if (cd).startswith("a"):
        cdv.append(cd)
    elif (cd).startswith("e"):
        cdv.append(cd)      
    elif (cd).startswith("i"):
        cdv.append(cd)      
    elif (cd).startswith("o"):
        cdv.append(cd)      
    elif (cd).startswith("u"):
        cdv.append(cd)      
    else:
        cdc.append(cd)
print(f"Hay {(len(cdc))} ciudades inician con consonante y son:  {cdc}")
print(f"Hay {(len(cdv))} ciudades inician con vocal y son:  {cdv}")