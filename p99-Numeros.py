# Operaciones entre conjuntos de números
import os; os.system("clear")

num_A = {50, 60, 70, 80, 90, 100, 200}
num_B = {60, 90, 100, 300, 400, 500}
num_C = {10, 20, 60, 90, 70, 100, 600, 700}

print('Conjunto A:', num_A)
print('Conjunto B:', num_B)
print('Conjunto C:', num_C)


union_A_B = num_A | num_B
union_B_C = num_B | num_C
diferencia_A_C = num_A - num_C
diferencia_simetrica_B_C = num_B ^ num_C
interseccion_B_C = num_B & num_C

print('\nUnión de A y B (A | B):', union_A_B)
print('Unión de B y C (B | C):', union_B_C)
print('Diferencia de A y C (A - C):', diferencia_A_C)
print('Diferencia simétrica de B y C (B ^ C):', diferencia_simetrica_B_C)
print('Intersección de B y C (B & C):', interseccion_B_C)


print('\n¿A es subconjunto de B?', num_A.issubset(num_B))
print('¿C es subconjunto de A?', num_C.issubset(num_A))
print('¿100 está en A?', 100 in num_A)
print('¿60 está en A, y en B y en C?', 60 in num_A and 60 in num_B and 60 in num_C)
print('¿900 no está en C?', 900 not in num_C)