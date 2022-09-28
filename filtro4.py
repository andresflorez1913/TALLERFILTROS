import pandas as pd
tablaDatos=pd.read_csv('./Siembras.csv')
print(tablaDatos[(tablaDatos["evento"]>250)& (tablaDatos["Ciudad"]=="Santa Fe de Antioquia")])
