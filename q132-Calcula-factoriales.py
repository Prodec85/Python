import os;os.system('cls')
import q124_Funciones as f

lista_numeros = f.leer_arreglo()

lista_factoriales = f.factoriales_lista(lista_numeros)

print(f"La lista de números originales: {lista_numeros}")
print(f"La lista con los factoriales: {lista_factoriales}")