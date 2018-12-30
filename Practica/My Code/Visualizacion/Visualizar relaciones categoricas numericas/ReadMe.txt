Para graficar la relacion que existe entre variables categoricas como 'Tipo de combustible' o 'cantidad de puertas' con variables
del tipo numerico podemos usar la libreria seaborn y sus componentes BOXPLOT y VIOLINPLOT.

BOXPLOT. 

Nos muestra informacion de como una variable categorica (eje x) se distribuye a travez de una variable numerica (eje y)
La columna y_col deberia del fija como y_col = 'price'

import seaborn as sea

sea.set_style('whitegrid')
sea.boxplot(x_col, y_col, data = dataset)
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()

VIOLINPLOT

sea.violinplot(x_col, y_col, data = dataset)