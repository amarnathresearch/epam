f = open('data2.txt')
numbers = f.read()
# print(numbers)
print(type(numbers))
print(numbers.split('\n'))
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])

# can we remove \n

print(numbers.split('\n')[0])

key = 'COMPLEX'

# Assignment - find the files, where the key is the present
# string3.txt & string4.txt

# open file string.txt
# uppercase
# find () >= 0 the key is fi

# if conditional
# open file string2.txt
# uppercase
# find() >= 0 


# if conditional
# open file string3.txt
# uppercase
# find() >= 0 

# if conditional
# open file string4.txt
# uppercase
# find() >= 0 

# f = open('string.txt', 'r')


key='COMPLEX'
f=open("string.txt")
f1=open("string2.txt")
f2=open("string3.txt")
f3=open("string4.txt")
data=f.read()
data1=f1.read()
data2=f2.read()
data3=f3.read()

key=key.lower()

if data.lower().find(key)>=0:
    print("in file string")
elif data1.lower().find(key)>=0:
    print("in file string1")
elif data2.lower().find(key)>=0:
    print("in file string2")
elif data3.lower().find(key)>=0:
    print("in file string3")
else:
    print("not found")
f.close()
f1.close()
f2.close()
f3.close()


node = {'node':{'node':{'node':{'node':{'node':{'node':['node', {'node':{'node':'epam'}}]}}}}}}
print(node)