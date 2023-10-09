import pandas as pd

serie =pd.Series([1, 2, 3, 4, 5])
serie2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(serie)
print (serie2)
