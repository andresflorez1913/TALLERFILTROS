import pandas as pd
tablaDatos=pd.read_csv('./Siembras.csv')
tablaFiltro1=tablaDatos[tablaDatos["ciudad"]=="Andes"]
archivoHTML=tablaFiltro1.to_html()
archivoTEXTO=open("Filtro1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()


