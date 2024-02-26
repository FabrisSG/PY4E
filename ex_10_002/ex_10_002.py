'''Ejercicio 2: Este programa cuenta la distribución de la hora del día
para cada uno de los mensajes. Puedes extraer la hora de la línea
“From” buscando la cadena horaria y luego dividiendo la cadena en
partes utilizando el carácter colon. Una vez que hayas acumulado las
cuentas para cada hora, imprime las cuentas, una por línea, ordenadas
por hora tal como se muestra debajo
Ingresa un nombre de archivo: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''
man_a = open("mbox-short.txt")
d = dict()
for linea in man_a:
    if linea.startswith("From "):
        linea = linea.rstrip()
        linea = linea.split()
        o = linea[5]
        o = o.split(":")
        tt = o[0]
        d[tt] = d.get(tt, 0) + 1
lst = list()
for key, val in d.items():
    newtup = (key,val)
    lst.append(newtup)
lst = sorted(lst, reverse = False)
for (key,val) in lst:
    print(key,val)
