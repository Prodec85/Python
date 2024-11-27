# Da día con letra en respuesta a número dado por el usuario
import q124_Funciones as f
import os;os.system('cls')
dias={ 1:'Domingo',2:'Lunes',3:'Martes',4:'Miércoles',5:'Jueves',6:'Viernes',7:'Sábado'}
while True:
    nums=f.leerdatos2()
    if nums > 0 and nums<8:
        print(dias[nums])