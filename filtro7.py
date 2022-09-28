import pandas as pd
tablaDatos=pd.read_csv('./Siembras.csv')
tablaCaramanta=tablaDatos[tablaDatos["Ciudad"]=="Caramanta"]
archivoHTML=tablaCaramanta.to_html()
archivoTEXTO=open("Caramanta.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
