import pandas as pd
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
wine_country = wine_reviews.country
# Selct de sql
#print(wine_reviews.country)
wr = wine_reviews['country'][0] 
wr = wine_reviews.iloc[0]
wr = wine_reviews.iloc[:, 0]
wr = wine_reviews.iloc[:3, 0]
wr = wine_reviews.iloc[1:3, 0]
wr = wine_reviews.iloc[[0, 1, 2], [0, 1, 2]]
wr = wine_reviews.iloc[-5:]
wr = wine_reviews.loc[0, 'country']
wr = wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

wb = wine_reviews.country == 'Italy'
wr = wine_reviews.loc[wine_reviews.country == 'Italy']
wr = wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90),['country','points']]

wr = wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90),['country','points']]
wr = wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])]

wr = wine_reviews.loc[wine_reviews.price.notnull()] #Estos métodos le permiten resaltar valores que están (o no) vacíos (NaN).

#print(wine_reviews.head())
#print(wb)
print(wr)

