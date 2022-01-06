# Read iris.csv
# setosa sepal width mean = 5.006

# classify the entire dataset

# lower limit 4.5 and upper limit can be 5.5

# Filter the iris data with respect to mean of the given sepal width
import pandas as pd

df = pd.read_csv('iris.csv')

print(len(df))
cnt = 0
cnttemp = 0
for i in range(len(df)):
    if df.loc[i]['sepal_length'] > 4.5 and df.loc[i]['sepal_length'] < 5.5:
        
        print(df.loc[i])
        cnt += 1
        if df.loc[i]['species'] == 0:
            cnttemp += 1
            
        
print(cnt)
print(cnttemp)


# JSON file => dataframe
# Dictionaries
# process the dictionary