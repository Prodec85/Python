# Calcula mayor, menor, media, varianza y desviación estándar
import os;os.system('cls')
import q124_Funciones as f
lista_numeros = f.leer_arreglo()

media_valor = f.media(lista_numeros)
mayor_valor = f.mayor2(lista_numeros)
menor_valor = f.menor02(lista_numeros)
varianza_valor = f.varianza(lista_numeros)
desviacion_valor = f.desviacion_estandar(lista_numeros)

print(f"Lista de números: {lista_numeros}")
print(f"La media: {media_valor:.3f}")
print(f"Mayor de los datos: {mayor_valor}")
print(f"Menor de los datos: {menor_valor}")
print(f"Varianza: {varianza_valor:.3f}")
print(f"Desviación estándar: {desviacion_valor:.3f}")