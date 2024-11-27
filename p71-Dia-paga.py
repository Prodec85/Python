# Muestra la paga según el día de la semana, usando dos listas.

import os; os.system("cls")

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingao']
paga = [100, 200, 300, 400, 500, 600, 700]

#n = 3
#print(dias[n], paba[n])


dia = ''
while True:
    dia = input('Dia ?')
    if dia in dias:
        break
print('Dia', dia)
pos = dias.index(dia)
print(f"La paga del día {dia} es de: ${paga[pos]}")
#print(f'La paga del día {dia} es de: $ {paga[pos]:.2}')