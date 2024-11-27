# Da el mes y número de días por mes dependiendo del número indicado por el usuario.
import os; os.system("cls")
mes=['Enero', 'Febrero', 'Marzo','Abril', 'Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre', 'Diciembre']
dia=[31,28,31,30,31,30,31,31,30,31,30,31]
r = 0
while True:
    num = int(input("Qué número de mes deseas? "))
    r = num-1
    if r >=0 and r <=11:
        print(f"El mes de {mes[r]} tiene {dia[r]} días.")
    else:
        print('El número no está entre 1 y 12')


    if input("Deseas continuar (S/N)").upper().startswith("N"):break