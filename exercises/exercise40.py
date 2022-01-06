import pandas as pd

dic  = [{'id':10, 'name':'amar', 'mobile':'989999'},{'id':20, 'name':'raj', 'mobile':'12345'}]

print(dic)

df = pd.DataFrame(dic)
print(df)

# Saving 
df.to_csv('sample.csv')

# Convert any list into data frames

