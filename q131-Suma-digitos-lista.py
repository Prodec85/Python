import os;os.system('cls')
import q124_Funciones as f

lista_numeros = f.leer_arreglo()

lista_sumas = f.suma_digitos_lista(lista_numeros)

print(f"La lista de números original: {lista_numeros}")
print(f"La lista con las sumas de dígitos de los números: {lista_sumas}")