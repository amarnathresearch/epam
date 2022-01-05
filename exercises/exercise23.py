import re

st = 'Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested.'

key = 'better'

# String operations

# li = st.split()
# print(li)
# count = 0
# for l in li:
#     if l == key:
#         count += 1
# print(count)

# li = st.split(key)
# print(len(li)-1)

st = 'Beautiful is Better than ugly. Explicit is beTter than implicit. Simple is betteR than complex. Complex is better than complicated. Flat is better than nested.'

key = 'better'

# li = st.split(key)
print(st.lower().count(key))
# print(len(li)-1)

email = 'amar1234@gmail.com'

# Valid email id @ 

email = '@amar1234gmail.com'

email = 'amar@gmail.amar1234@gmail.com.com'

email = 'amar.com@gmail.com'

email = 'amar.com@yahoo.com'

email = 'amar@redif@rediffmail.com'

email = 'amar@redif@rediffmail.com'


# minimum 8 characters
# maximum 20 characters
# Combination of upper case and lowercase
# It should contain special symbols
# It should not have patterns eg: 123 or abc or 321 

password = 'amarnath@1234' # It cannot be accepted
 
# import re
# regex='^[a-z0-9A-Z@]'
# pw='ry123AS@'
# if(re.search(regex,pw)):  
#     print("Valid pw")  
# else:  
#     print("Invalid pw")

# re.search
# re.findall
# re.compile
# re.match
# re.split
# re.sub

st = "Beautiful is Better than ugly. Explicit is beTter; than implicit. Simple is betteR' than complex. Complex is better, than complicated. Flat is ,better than nested."


key = 'better'



print(st.lower().count(key))

# regular expressions

# syntax
# search = re.search(pattern, string)

search = re.search("better", st)
print(search)

search = re.findall("better", st)
print(search)

# ^ : starting word
# $ : ending word
#  \ : escape character
# [] : grouping
# * : 0 or more occurances
# + : 1 or more occurances
# () : grouping
# ?  : 0 or 1 occurances
# . : each and every character

st = "Beautiful is Better than ugly. Explicit is beTter; than implicit. Simple is betteR' than complex. Complex is better, than complicated. Flat is ,better than nested."

match = re.search('Tt', st)
print(match)

st = "Beautiful is Better than ugly. Explicit is beTter; 10 than impli30cit. Simple is 44betteR' than complex100. Complex is better, than complicated. Flat is ,better than nested."

match = re.search('[0-9]', st)

match = re.findall('[0-9]', st)

print(match)

match = re.findall('[0-9]+', st)

print(match)

match = re.findall('\.', st)
print(match)


st = "Beautiful is Better than ugly. Explicit is beTter; 10-20 than impli30-33cit. Simple is 44-43betteR' than complex99-77. Complex is better, than complicated. Flat is ,better than nested."

match = re.findall('[0-9]', st)
print("solution =>", match)


# 10-20
# 30-33
# 44-43

match = re.findall('\d\d-\d\d', st)

print(match)

print(re.findall("[0-9][0-9]-[0-9][0-9]", st))


st = "Beautiful is Better than ugly. Explicit is beTter; 100-20 than impli30-337cit. Simple is 444-43betteR' than complex99-775. Complex is better, than complicated. Flat is ,better than nested 10-2."

match = re.findall('[0-9]+-[0-9]+', st)
print(match)
# print(re.findall("([0-9][0-9]-[0-9][0-9]|[0-9][0-9][0-9]-[0-9][0-9]|[0-9][0-9]-[0-9][0-9][0-9])", st))

st = "Beautiful is Better than ugly. Explicit is beTter; -20 than impli30-337cit. Simple is 444-43betteR' than complex99-775.34. Complex is better, than complicated. Flat is ,better than nested 10.2-2."

# -20
# 30-337
# 444-43
# 99-775.34
# 10.2-2

match=re.findall('[0-9]*-[0-9]*.[0-9]*',st)
print(match)


match=re.findall('[0.0-9]*-[0.0-9]*',st)
print(match)


match = re.findall('[0-9]*[.]*[0-9]*-[0-9]+[.]*[0-9]*', st)
print(match)

