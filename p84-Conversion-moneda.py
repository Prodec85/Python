# Conversion a pesos
import os; os.system('cls')

dias ={
    '1' : 20.50,  # Dolares
    'EUR' : 22.30,  # Euros
    'GBP' : 25.80,  # Libra esterlina
    'JPY' : 0.10 ,  # Yen Japones
    'CAD' : 16.20   # Dolar Canadiense
}

print('Conversion de diferentes monedas a pesos mexicanos')
print('Monedas:  ')
for m in dias.keys(): print (f' - {m}')
while True:
    moneda = input('Moneda ?').upper()
    if moneda in dias: break
cantidad = float(input('Cantidad?'))

resultado = cantidad * dias[moneda]
print(f'${cantidad:,.2f} {moneda} son ${resultado:,.2f} pesos.')