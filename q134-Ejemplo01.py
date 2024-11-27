# Creamos una clase empleado con atributos y métodos

# Código de clase 
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):  
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    
# Programa principal
import os;os.system('cls')
emp01 = Empleado('Carlos Castañeda', 35)  # Creamos una instancia 
emp02 = Empleado('Juan Perez', 66)

print('\nDatos del empleado 1')
print(f'Nombre   : {emp01.nombre}')
print(f'Edad     : {emp01.edad}')
print(f'Empleado : {emp01}')
emp01.edad = 40
print(f'Empleado : {emp01}')

print('\nDatos del empleado 2')
print(f'Nombre   : {emp02.nombre}')
print(f'Edad     : {emp02.edad}')
print(f'Empleado : {emp02}')
emp01.edad = 40
print(f'Empleado : {emp02}')