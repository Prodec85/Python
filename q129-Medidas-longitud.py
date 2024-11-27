#Convierte de centímetros a pulgadas y pies a metros.
import os;os.system('cls')
import q124_Funciones as f

#Progrma principal
while True:
    print('Para convertir de pultadas a centímetros [1]')
    print('Para convertir de pies a metros          [2]')
    uni = int(input('Elije una opción: '))
    os.system('cls')
    if uni == 1:
        cc = f.inchtocc()    
        print(cc)
        print('')
    elif uni == 2:
        ft = f.metft()
        print(ft)
        print('')
    else:
        print('< El dado es incorrecto >')
        print('')