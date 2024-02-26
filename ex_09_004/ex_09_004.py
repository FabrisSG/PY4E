'''Ejercicio 4: Agrega código al programa anterior para determinar quién
tiene la mayoría de mensajes en el archivo. Después de que todos los
datos hayan sido leídos y el diccionario haya sido creado, mira a través
del diccionario utilizando un bucle máximo (ve Capítulo 5: Bucles máximos y mínimos)
para encontrar quién tiene la mayoría de mensajes e
imprimir cuántos mensajes tiene esa persona ----- cwen@iupui.edu 5'''

contador = dict()
man_a = open("mbox-short.txt")
for linea in man_a:
    linea = linea.rstrip()
    if linea.startswith("From:"):
        s = linea.split()
        contador[s[1]] = contador.get(s[1],0)+1

bigcount = None
bigword = None

for k,v in contador.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v

print(bigword, bigcount)
