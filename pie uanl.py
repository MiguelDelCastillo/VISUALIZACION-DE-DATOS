#Creación de Gráfica de Pie
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple

Datos = namedtuple("Anio",("Cantidad"))


Diccionario = {}

Diccionario[2015] = Datos(181033)
Diccionario[2016] = Datos(190169)
Diccionario[2017] = Datos(197381)
Diccionario[2018] = Datos(202039)
Diccionario[2019] = Datos(206640)

x = ['2015', '2016', '2017', '2018','2019']
y = [181033, 190169, 197381, 202039,206640]
distancia = [0,0,0,0,0.1]

plt.pie(Diccionario.items(), labels=Diccionario.keys(), explode=distancia)



plt.legend(Diccionario.keys())
plt.title('Número de estudiantes de la UANL')
#plt.xlabel('Año')
#plt.ylabel('Numero de estudiantes')
plt.grid(True)

plt.show()