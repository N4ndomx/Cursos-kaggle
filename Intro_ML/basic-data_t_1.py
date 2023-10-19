import pandas as pd
# save filepath to variable for easier access
melbourne_file_path = '../melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
print(melbourne_data.describe())

#Los resultados muestran 8 números para cada columna en su conjunto de datos original. 
#El primer número, el recuento, muestra cuántas filas tienen valores no faltantes. 
#Los valores faltantes surgen por muchas razones. 
#Por ejemplo, el tamaño del segundo dormitorio no se recopilaría al inspeccionar una casa de 1 dormitorio. 
#Volveremos al tema de los datos faltantes. El segundo valor es la media, que es el promedio. 
#Debajo de eso, std es la desviación estándar, que mide qué tan dispersos numéricamente están los valores. 
#Para interpretar los valores mínimo, 25 %, 50 %, 75 % y máximo, imagine ordenar cada columna del valor más bajo al más alto. 
#El primer valor (el más pequeño) es el mínimo. Si recorre un cuarto de la lista, encontrará un número que es mayor que el 25% de los valores y menor que el 75% de los valores. 
#Ese es el valor del 25% (pronunciado "percentil 25").
# Los percentiles 50 y 75 se definen de manera análoga y el máximo es el número más grande.
