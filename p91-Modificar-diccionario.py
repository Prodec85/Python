# Modificar diccionario por dos métodos..
import os; os.system('cls')
paises={'Argentina':100, 'Brasil':200, 'Colombia':300,'Chile':400,'Ecuador':500,'Bolivia':600,'Jamaica':700}
print(paises)
print()


paises['Brasil']=250
paises['Chile']=450

print(paises)
print()

paises.update({'Bolivia':650})
paises.update({'Jamaica':750})
print(paises)