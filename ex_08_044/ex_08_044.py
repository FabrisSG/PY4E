'''Escribir un programa para abrir el archivo romeo.txt y leerlo línea
por línea. Para cada línea, dividir la línea en una lista de palabras
utilizando la función split. Para cada palabra, revisar si la palabra ya
se encuentra previamente en la lista. Si la palabra no está en la lista,
agregarla a la lista. Cuando el programa termine, ordenar e imprimir
las palabras resultantes en orden alfabético.

Ingresar nombre de archivo: romeo.txt

['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']'''

narchivo = input("Ingresa el nombre del documento:")
man_a = open(narchivo)
words = list()
for linea in man_a:
    linea = linea.rstrip()
    t = linea.split()
    for palabras in t:
        if palabras in words:
            continue
        else:
            words.append(palabras)

y = words.sort()
print(words)
