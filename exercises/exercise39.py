import pandas as pd

df = pd.read_csv('iris.csv')

print(df)

print(df[:1])
print(df[:2])
setosa = df[:50]
print(setosa)
versicolor = df[51:100]
print(versicolor)
virginica = df[101:150]
print(virginica)

print(df.loc[10])
print(df.loc[[10, 12, 15]])

print(df.info())

setosa = df.loc[df['species']==0]
# print(setosa)

setosa_sepal_length_mean = setosa['sepal_length'].mean()
setosa_sepal_width_mean = setosa['sepal_width'].mean()
print(setosa_sepal_length_mean)
print(setosa_sepal_width_mean)

versicolor = df.loc[df['species']==1]
versicolor_sepal_length_mean = versicolor['sepal_length'].mean()
versicolor_sepal_width_mean = versicolor['sepal_width'].mean()

print(versicolor_sepal_length_mean)
print(versicolor_sepal_width_mean)

virginica = df.loc[df['species']==2]
virginica_sepal_length_mean = virginica['sepal_length'].mean()
virginica_sepal_width_mean = virginica['sepal_width'].mean()

print(virginica_sepal_length_mean)
print(virginica_sepal_width_mean)


versicolor_sepal_length_median = versicolor['sepal_length'].median()

print(versicolor_sepal_length_median)

