#String operations
'''
a = 10
b = 20
c = a+b
print(c)
'''

string1 = 'Epam India'

str_list = string1.split()
print(str_list[0])

print(string1.split()[0])
print(string1.split()[1])

string2 = 'Epam India'
print(len(string2))

string3 = string2[5:]
print(string3)

string3 = string2[:-5]
print(string3)

string3 = string2[:-1]
print(string3)

string3 = string2[1:-1]
print(string3)

string4 = 'epam india'
print(string4.upper())

string4 = 'EPAM INDIA'
print(string4.lower())

print(string4.title())

string5 = 'Beautiful is better than ugly. Explicit is better than implicit.'

key = 'ugly'
ind = string5.find(key)
print(ind)

key = 'epam'
ind = string5.find(key)
print(ind)


string5 = 'Beautiful is better than ugly. Explicit is better than implicit.'

#replace ugly with bad

print(string5.replace('ugly', 'bad'))

print(string5)
print(string5.index('ugly'))
#print(string5.index('epam'))


#find & index
#find will return -1 if the word is not available
#index will throw exception if the word is not available

string6 = '12345a'
print(string6.isdigit())















