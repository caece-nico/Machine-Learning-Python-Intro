En estos ejemplos se crean scatterplots usando seaborn para ver graficos con alta dimencionalidad. de 3d, 4D y 5D.

Seaborn no tiene una funcion que crea estos graficos sino que hay que crear uno por uno iterando por figura o color y luego se unen en un grafico para cada uno.

datos: 

shape_col indica la variable categorica por la que vamos a crear formas ['+','*','o,'x']
size_col indica la variable por la que le vamos a dar un tañano a las variables, generalmente es numerico
normalizador es una constante que usaremos para estabilar el tamaño de los graficos 
color_col es una variable categorica por la que vamos a dar color a los graficos.
alpha indica el rado de atenuacion.

1 ) 

Ejemplo de scatterplot 3D. shape

import seaborn as sea

def crea_scatter_3D(data,x_col,y=col=XX,shape_col=XX):
    shape = ['','','',''] // declaramos las figuras del grafico
    unique_cat = data[shape_col].unique() // traemos las categorias unicas
    
    for col in x_col: iteramos por columna que pasamos a la funcion
        sea.set_style(whitegrid) 
        for idx,cat in enumerate(unique_cat): iteramos por categoria
            tmp = data[data[shape_col]==cat] // para cada categoria creamos una temporal con los datos a graficar
            sea.regplot(col,y_col,temp,marker=shape[idx],label=cat,scatter_kws{'alpha':alpha},fit_reg=False,color='') 
                        // creamos el grafico y en la siguiente iteracion se une. si tiene tres  categorias se ejecuta 3 veces.
        plt.legend()
        plt.....()

2) 

Ejemplo de scatterplot 4D. Shape + Size

def crea_scatter_4D(data,x_col, y_col='', shape_col = '', size_col = '', normalizador = 0.000008, alpha = 0.3):
    shape = ['','','','']
    unique_cat = data[shape_col].unique()
    
    for col in x_col:
        sea.set_style('whitegrid')
        for idx, cat in enumerate(unique_cat):
            temp = data[data[shape_col]==cat]
            sea.regplot(col, y_col, temp, marker = shape[idx], label = cat, 
                        scatter_kws={'alpha':alpha, 's':normalizador*temp[size_col]**2}, fit_reg = False, color = '')
            plt.legend()
            plt.title/xlabel/ylabel()
            plt.show()
            
3) 

Ejemplo ScatterPlot en 5D con variable shape, size y color.

Este es el ejemplo mas complejo porque tienen una doble iteracion por propiedades una por shape o categorias y la otra por color.
 
def crea_scatter_5D(dataset, x_col, y_col, shape_col = '', size_col = '', color_col = '', normalizer = 0.0000xx, , alpha = 0.xx,):
    shape = ['','','','','']
    color = ['','','','','']
    
    unique_shape = data[shape_col].unique()
    unique_color = data[color_col].unique()
    
    for col in x_col:
        sea.set_style('whitegrid')
        for idx_cat, cat in enumerate(unique_shape):
            for idx_color, color_r in enumerate(unique_color):
                temp = data[data([shape_col]==cat & [color_col]==color_r)
                sea.regplot(col,y_col,temp, marker=[idx_cat], label = (cat  +' ' + color_r),
                            scatter_kws={'alpha':xxx,'s':normalizador*temp[size_col]**2},fit_reg=False, color = color[idx_color])
        plt.legend()/xlabel/ylabel/titel
        plt.show()
        
 