# Procesar un pedido de pizza usando diccionarios en python
import os; os.system('cls')

ings = {
    'T' : 1.5,
    'P' : 3.5,
    'C' : 3.74,
    'A' : 0.40
}
st = 0
base = 15
tot = 0
des = 0
pedido= input('Que ingredientes deseas para tu pizza? ').upper()

for ing in pedido:
    if ing in 'TPCA':
        st += ings[ing]
print(pedido)

st = st + base
if st >=20:
    des = st * 0.05
    tot = st - (des)
else:
    des = 0
    tot = st
print(f'El subtotal es ${st:.2f}')
print(f'El descuento es ${des:.2f}')
print(f'El total es ${tot:.2f}')
