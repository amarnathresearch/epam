import re
f = open('sample.txt', 'r')

# print()
st = f.read()
match = re.findall('\d*-\d*-\d*', st)
print(match)

match=re.findall('[0-9][0-9][0-9] ',st)
print(match)

match = re.findall('\d+ ', st)
print(match)


# # \b 

# st = 'Hi how are you. I can hear you. Hope you are good'
# # \b
# match = re.findall('^h', st)
# print(match)

# Extract email from the text

match = re.findall('[a-z]+@[a-z]+.com', st)

print(match)

emails = re.findall("([a-z]+@[a-z]+.com)", st)
print(emails)

names = re.findall("\n[a-zA-z]+ [a-zA-z]+", st)
print(names)

zipcodes = re.findall("\d\d\d\d\d", st)
print(zipcodes)
# ['.@0-9a-z']

# Text Analysis Data Science (Text Engineering or Text Mining)
# Text Classification tasks - Emotion analysis or Sentimental Analysis

# Reviews -> How many people liked or not liked
# Movie review Text preprocessing -> Regular expressions.
