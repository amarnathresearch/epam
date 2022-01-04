# functions - modularity

# function definition with two arguments
def add(x, y):
    c = x + y
    return c

print(add(10, 15))



c = add(x = 10, y = 20)
print(c)

c = add(10, y = 20)
print(c)

# c = add(x = 10, 20)
# print(c)

# c = add(a = 10, b = 20)
# print(c)

a = 10
b = 20
c = add(a, b)
print(c)

def add(x, y):
    print(id(x))
    print(id(y))

    c = x + y
    print(id(c))

    return c

c = add(x=10, y=20)


print(id(c))

# Get the address of 

def greater(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return -1


x = 10
y = 10

print(greater(x, y))

def greater(n):
    for i in range(n):
        print(i)

greater(10)


# def add(a, b):
#     def mul(a, b):
#         c = a * b
#         return c
#     c = mul(a, b)
#     return c

# x = 10
# y = 20
# c = add(x, y)
# print(c)

# def add(a, b):
#     def mul(a, b):
#         c = a * b
#         return c
    
# x = 10
# y = 20
# c = mul(x, y)
# print(c)

# 
dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}}}

print(dic)

# for value in dic.values():
#     print("value")
#     # if value == 'epam': 
#     #     print("true", value)

# def ans(dic):
#     if type(dic) is not dict:
#         print (dic)
#     ans(dic['new'])
# # dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}}}
# ans(dic)


# for k,v in dic.items():
#     print(k, v)
#     if v=='epam':
#         print(v)

# def ans(dic):
#     if type(dic) is not dict:
#         return (dic)
#     return ans(dic['new'])
# dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}}}
# print(ans(dic))

# Use while loop ??

dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}}}

while(type(dic) is dict):
    dic=dic['new']
else:
    print ('value', dic)

i = 0


dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}}}

# iteration 1
dic = {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}}

# iteration 2

dic = {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}

# iteration 3

dic = {'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}

# iteration 4

dic = {'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}

# iteration 5

dic = {'new':{'new':{'new':{'new':{'new':'epam'}}}}}

# iteration 6

dic = {'new':{'new':{'new':{'new':'epam'}}}}

# iteration 7

dic = {'new':{'new':{'new':'epam'}}}

# iteration 8

dic = {'new':{'new':'epam'}}

# iteration 9

dic = {'new':'epam'}

# iteration 10 

dic = 'epam'

dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}}}

while (type(dic)== dict):
    dic=dic['new']
    print(f"iteration {i} : {dic}")
    i += 1
print(dic)


# While and for

l = []

dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'epam'}}}}}}}}}}

l.append(dic)
dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'india'}}}}}}}}}}
l.append(dic)
dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'train'}}}}}}}}}}
l.append(dic)

dic = {'new': {'new': {'new':{'new':{'new':{'new':{'new':{'new':{'new':{'new':'myanatomy'}}}}}}}}}}
l.append(dic)

print(l)
key = 'myanatomy'

# Search myanatomy in the list of dictionaries

# for loop - iterating the lists
# while loop inside the for loop


for i in range(len(l)):
    while (type(l[i])== dict):
        l[i]=l[i]['new']
    if l[i].lower()==key:
        print("present in ",i+1, 'dic')

# def ans(dic):
#     if type(dic) is not dict:
#         return(dic)
#     return ans(dic['new'])
# for i in l:
#     if ans(i)=="myanatomy":
#         print(True)

