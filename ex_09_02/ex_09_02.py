'''Ejercicio 2: Escribir un programa que clasifica cada mensaje de correo
dependiendo del día de la semana en que se recibió. Para hacer esto
busca las líneas que comienzan con “From”, después busca por la tercer
palabra y mantén un contador para cada uno de los días de la semana.
Al final del programa imprime los contenidos de tu diccionario (el orden
no importa).'''
d = dict()
man_a = open("mbox-short.txt")
for linea in man_a:
    linea = linea.rstrip()
    if linea.startswith("From "):
        linea = linea.split()
        d[linea[2]] = d.get(linea[2],0)+1
print(d)
