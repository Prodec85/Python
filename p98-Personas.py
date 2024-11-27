# Operaciones entre conjuntos de nombres

import os; os.system("clear")

nombres_A = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
nombres_B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}

print(nombres_A, nombres_B)

print('\nUnión:')
print('A unión B : ', nombres_A | nombres_B)

print('\nIntersección:')
print('A intersección : ', nombres_A & nombres_B)

print('\nDiferencia:')
print('A diferencia B : ', nombres_A - nombres_B)

print('\nDiferencia simétrica:')
print('A dif simétrica B : ', nombres_A ^ nombres_B)

print('\nProbar por subconjuntos:')
print('{"Pablo", "Mateo"} es subconjunto de B:', {'Pablo', 'Mateo'}.issubset(nombres_B))

print('\nProbar superconjuntos:')
print('A es superconjunto de {"Reynaldo", "Angelica"}:', nombres_A.issuperset({'Reynaldo', 'Angelica'}))

print('\nVerificar pertenencia o no pertenencia al conjunto:')
print('Pedro está en A:', 'Pedro' in nombres_A)
print('Lilia no está en B:', 'Lilia' not in nombres_B)