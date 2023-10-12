import pandas as pd
#pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("../winemag-data-130k-v2.csv", index_col=0)

re=reviews.points.describe() #Este método genera un resumen de alto nivel de los atributos de la columna dada. 
#Es consciente del tipo, lo que significa que su salida cambia según el tipo de datos de la entrada.
# El resultado anterior sólo tiene sentido para datos numéricos

# Para datos de cadena
re=reviews.taster_name.describe()

#Si desea obtener alguna estadística resumida simple en particular sobre una columna
re = reviews.points.mean()

#Para ver una lista de valores únicos
re = reviews.taster_name.unique()


#Para ver una lista de valores únicos y con qué frecuencia ocurren en el conjunto de datos
re = reviews.taster_name.value_counts()

#Mapas
#Un mapa es un término, tomado de las matemáticas,
# para una función que toma un conjunto de valores 
# y los "mapea" a otro conjunto de valores.

#En la ciencia de datos, a menudo tenemos la necesidad de crear nuevas representaciones a partir de datos existentes,
# o de transformar datos del formato en el que se encuentran ahora al formato en el que queremos que estén más adelante. 
#Los mapas son los que se encargan de este trabajo, lo que los hace extremadamente importantes para realizar el trabajo.

# map() es el primero y un poco más simple. Por ejemplo, supongamos que quisiéramos resignificar las puntuaciones que recibieron los vinos a 0.

review_points_mean = reviews.points.mean()
re=reviews.points.map(lambda p: p - review_points_mean)

#es el método equivalente si queremos transformar un DataFrame completo llamando a un método personalizado en cada fila.

#def remean_points(row):
 #   row.points = row.points - review_points_mean
  #  return row

#re =reviews.apply(remean_points, axis='columns')


#Pandas proporciona muchas operaciones de mapeo comunes integradas. 
#Aquí hay una forma más rápida de cambiar el significado de nuestra columna de puntos

review_points_mean = reviews.points.mean()
re =reviews.points - review_points_mean


#combinar información de país y región en el conjunto de datos sería hacer lo siguiente
re = reviews.country + " - " + reviews.region_1

#Estos operadores son más rápidos que map() o apply() porque utilizan aceleraciones integradas en pandas. 
#Todos los operadores estándar de Python (>, <, ==, etc.) funcionan de esta manera. 
#Sin embargo, no son tan flexibles como map() o apply(), que pueden hacer cosas más avanzadas, como aplicar lógica condicional, 
#que no se puede hacer solo con sumas y restas.

print(re)

