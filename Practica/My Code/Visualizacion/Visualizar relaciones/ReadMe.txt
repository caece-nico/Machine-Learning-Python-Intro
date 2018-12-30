Visualizacion de datos entre dos variables numericas.

Cuando se visualizan estos datos hayq ue asegurarce que ambos son del tipo numerico.
El tipo de grafico mas coun el es scatter plor de la libreria de matplotlib.pyplot y seaborn cuando son millones.

ScatterPot Matplot lib

Este tipo de grafico lo podemos hacer con o sin transparencias.

import matplotlib.pyplot as plt

fig = plt.figure(figsize(7,6))
ax = fig.gca()
data.plot.scatter(x_col,y_col,ax=ax,alpha=1)

donde alpha es la atenuacion que e le da en caso de querer ver cuantos puntos se concentran.

si tenemos millones de datos usamos seaborn que combina histogramas con graficos de densidad.

import seaborn as sea

sea.set_style('whitegrid')
sea.jointplot(x_col,y_col,data = dataset, kind = 'kde')
plt.title()
plt.xlabel()
plt.ylabel()

este grafico tiene dos kind = ['kde','hex']