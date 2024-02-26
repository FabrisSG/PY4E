'''Ejercicio 5: Escribir un programa para leer a través de datos de una bandeja
de entrada de correo y cuando encuentres una línea que comience
con “From”, dividir la línea en palabras utilizando la función split.
Estamos interesados en quién envió el mensaje, lo cual es la segunda
palabra en las líneas que comienzan con From:

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Tendrás que analizar la línea From e imprimir la segunda palabra de
cada línea From, después tendrás que contar el número de líneas From
(no incluir From:) e imprimir el total al final. Este es un buen ejemplo
de salida con algunas líneas de salida removidas:'''

narchivo = input("Ingresa el nombre del archivo:")
man_a = open(narchivo)
contador = 0
for linea in man_a:
    linea = linea.rstrip()
    if linea.startswith("From:"):
        t = linea.split()
        y = t[1]
        contador = contador + 1
        print(y)
print("Hay", contador , "lineas en el archivo con la palabra From al inicio")
