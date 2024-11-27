# Eliminar elemntos por cuatro métodos..
import os; os.system('cls')
muni={'Apozol':1863, 'Calera':1868, 'Fresnillo':1554, 'Guadalupe':1821, 'Jalpa':1824, 'Jerez':1824, 'Loreto':1931,
'Mazapil':1824, 'Momax':1857.}
print(muni)
print()
del muni['Apozol']
print(muni)
print()
muni.pop('Fresnillo')
print(muni)
print()
muni.popitem()
print(muni)
print()
muni.clear()
print(muni)