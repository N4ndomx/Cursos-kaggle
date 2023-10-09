import pandas as pd

dataframe1= pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
dataframe2= pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
dataframe3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(dataframe1)
print(dataframe2)
print(dataframe3)
