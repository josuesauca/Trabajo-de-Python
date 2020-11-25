""" 
2.17 [EX02-017] La American Time Use Survey que se presentó al 
comienzo del capítulo destacó el uso del tiempo de un día de la
semana promedio para estudiantes de universidad de 
tiempo completo.


Categoría                               Horas
=============================================
Dormir                                  8.3
Ocio y deportes                         3.9
Actividades educativas                  3.2
Trabajo y actividades relacionadas      3.0
Comer y beber                           1.0
Viajar                                  1.5
Aseo                                    0.8
Otro                                    2.3
=============================================
Total                                   24.0
=============================================

"""

# Importamos los paquetes a usar

import pandas as pd
import matplotlib.pyplot as plt

#Cargamos la Hoja de Excel que deseamos usar

hoja_excel = "C:\Segundo Ciclo\Teoria de la Distribucion y Probabilidad\Graficas Estadisticas\EjerciciosExtra\Ejercicio.xlsx"


#Con la funcion read_excel leemos la hoja de datos cargada
read_file = pd.read_excel(hoja_excel)


#Almacenamos los valores de categoria en la varible valores
valores = read_file[['Categoria',"Horas"]]

#Dibujarmos el diagrama de barras con la funcion bar 
valores.plot.bar(x ="Categoria",y ="Horas",rot = 10,color = "C1")

categoria = read_file["Categoria"].tolist()

horas = read_file["Horas"].tolist()

plt.title("Uso tiempo promedio día semana para estudiantes universitarios")


#Imprimimos un mensaje en el eje y
plt.ylabel("Conteo")


#Obtener los Valores de la Frecuencia Absoluta

Frec_rel_val =  read_file["Horas"].values

#Creamos un arreglo unidimensonal para guardar un arreglo

acum = []

#Inicializamos las varible donde guardaremos la suma de los valores de las horas

suma_horas = 0

# En este ciclo for vamos a añadir a la variable suma horas los valores de la suma 

for i in Frec_rel_val:
    suma_horas= suma_horas + i
    print(suma_horas)
    acum.append(suma_horas)

read_file["Horas"] = acum

#Dibujamos el Diagrama de dispersion

plt.scatter(categoria,acum)

#Mostramos las Graficas Cargadas
plt.show()



# Valores Porcentuales

#Cargamos la Hoja de Excel que deseamos usar

hoja_excel = "C:\Segundo Ciclo\Teoria de la Distribucion y Probabilidad\Graficas Estadisticas\EjerciciosExtra\Ejercicio.xlsx"


#Con la funcion read_excel leemos la hoja de datos cargada
read_file = pd.read_excel(hoja_excel)

#Leemos los valores de Horas

valores = read_file[['Categoria',"Horas"]]


# Valores porcentuales de la frecuencia
Frec_valor_porcentual = read_file["Horas"].values

Frec_valor_porcentual

#Creamos un arreglo unidimensonal para guardar un arreglo
acum = []

for i in Frec_valor_porcentual:
    
    i = (i/24) * 100 
    acum.append(i)

read_file["Horas"] = acum

acum

#Dibujamos el Diagrama de dispersion

plt.scatter(categoria,acum)

#Mostramos las Graficas Cargadas

plt.show()
plt.clf()


# Valores Porcentuales Acumulados

#Cargamos la Hoja de Excel que deseamos usar

hoja_excel = "C:\Segundo Ciclo\Teoria de la Distribucion y Probabilidad\Graficas Estadisticas\EjerciciosExtra\Ejercicio.xlsx"

#Con la funcion read_excel leemos la hoja de datos cargada
read_file = pd.read_excel(hoja_excel)

#Leemos los valores de Horas

valores = read_file[['Categoria',"Horas"]]

# Valores porcentuales de la frecuencia
Frec_valor_porcentual_acumulado = read_file["Horas"].values


#Creamos un arreglo unidimensonal para guardar un arreglo
acum = []

suma = 0 

for i in Frec_valor_porcentual_acumulado:
    
    suma = suma + (i/24) * 100 
    acum.append(suma)

read_file["Horas"] = acum

acum

#Dibujamos el Diagrama de dispersion

plt.scatter(categoria,acum)

#Mostramos las Graficas Cargadas

plt.show()
plt.clf()

