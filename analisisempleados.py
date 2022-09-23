import pandas as pd
tablaEmpleados=pd.read_csv('./empleados.csv')
#print(tablaEmpleados)
#print(tablaEmpleados.to_string())

#quiero tener todos los datos de analista 1tablaAnalistas1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
#archivoHTML=tablaAnalistas1.to_html()
#archivoTEXTO=open("datosanalistas1.html","w")
#archivoTEXTO.write(archivoHTML)
#archivoTEXTO.close()

#quiero tener todos los datos de analista 2
tablaAnalistas2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaAnalistas2.to_html()
archivoTEXTO=open("datosanalistas2.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

#quiero tener analistas  menores de 30 años que ganen mas de 5 millones 500


