#------------------------------------
#Ajuste lineal por mínimos cuadrados
#Valente Vázquez
#------------------------------------

#----Bibliotecas----
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def lineal(archivo, ordenada, tit, titX, titY):
    data = pd.read_csv(archivo)
    n = len(data.axes[0]) #Número de pares de datos

    #----Cálculo por mínimo cuadrados----
    sumaX = 0
    sumaY = 0
    sumaX2 = 0
    sumaY2 = 0
    sumaXY = 0
    phi = 0

    for i in range(0, n): #Sumas---
        sumaX += data['X'][i]
        sumaY += data['Y'][i]
        sumaX2 += data['X'][i]**2
        sumaY2 += data['Y'][i]**2
        sumaXY += (data['X'][i])*(data['Y'][i])

    if ordenada == False:
        m = sumaXY/sumaX2 #pendiente
        b = 0 #ordenada
        for i in range(0, n):
            phi += (data['Y'][i]-m*data['X'][i]-b)**2
        cons = (1/(n*sumaX2-sumaX**2))*(phi/(n-2))
        dm = np.sqrt(n*cons) #Error pendiente
        db = 0 #Error ordenada
    else:
        m = (n*sumaXY-sumaX*sumaY)/(n*sumaX2-sumaX**2) #pendiente
        b = (sumaY-m*sumaX)/n #ordenada
        for i in range(0,n):
            phi += (data['Y'][i]-m*data['X'][i]-b)**2
        cons = (1/(n*sumaX2-sumaX**2))*(phi/(n-2))
        dm = np.sqrt(n*cons) #Error pendiente
        db = np.sqrt(sumaX2*cons) #Error ordenada

    r = sumaXY/np.sqrt(sumaX2*sumaY2) #Coeficiente de correlación
    r2 = r**2 #Coeficiente de determinación

    #----Impresión de datos----
    rd = 3 #Redondeo de números
    pendiente = str(round(m,rd))+" +- "+str(round(dm,rd))
    ordenada = str(round(b,rd))+" +- "+str(round(db,rd))
    coef_r = str(round(r,rd))
    coef_r2 = str(round(r2,rd))
    recta = "y = ("+pendiente+")x"+" + ("+ordenada+")"
    print("Pendiente: ", pendiente)
    print("Ordenada al origen: ", ordenada)
    print("Coeficiente de correlación: ", coef_r)
    print("Coeficiente de determinación: ", coef_r2)
    print("Ecuación de la recta: ", recta)

    #----Graficar----
    postext = 2 #Posición del texto dentro de la gráfica
    y = m*data['X']+b #Recta ajuste
    # plt.plot(data['X'],data['Y'], "d")
    plt.errorbar(data['X'], data['Y'], yerr=data['eY'], xerr=data['eX'], fmt="k.") #Graficar puntos
    plt.plot(data['X'], y, "b") #graficar ajuste lineal
    if m <= 0: #Posición texto recta
        postext = 1
    plt.legend(["Ajuste: "+recta+", $r^2$: "+coef_r2,"Datos obtenidos"], fontsize='x-small',loc=postext) #Etiquetas
    plt.grid()
    plt.title(tit), plt.xlabel(titX), plt.ylabel(titY)
    plt.show()

#----Leer datos de archivo----
archivo = "LeyOhm.csv"
titulo = "Ley de Ohm"
ejeX = "Intensidad de Corriente [A]"
ejeY = "Diferencia de Potencial [V]"
lineal(archivo, True, titulo, ejeX, ejeY) #False para obligar a b = 0, True para calcular b
