# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import seaborn as sea
import pandas as pd
import matplotlib.pyplot as plt

arch = 'Automobile price data _Raw_.csv'

inter = pd.read_csv(arch)


""" 
creamos una funcion que permira visualizar la distribucion de variables categoricas
"""

def crear_bar_plot(data, columna):
    for col in columna:
        fig = plt.figure(figsize=(6,6))
        ax = fig.gca()
        totales = data[col].value_counts()
        totales.plot.bar(ax = ax, color = 'red')
        ax.set_title("Distibucion de totales para la columna "+ col)
        ax.set_xlabel(col)
        ax.set_xlabel("Number of autos")
        plt.show()
        
columna = ['make','body-style','num-of-cylinders']
crear_bar_plot(inter,columna)
    
    
    