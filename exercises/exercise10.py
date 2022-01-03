#file operations

f = open('data.txt', "r")
print(type(f))
data = f.readlines()
print(data)
print(type(data))
print(data[0])
print(data[1])
print(data[2])
print(data[3])
f.close()

#Assignment
#Replace word 'You' with 'us'

f = open('data1.txt', 'a')
f.write('Hello world')
f.close()


f = open('data.txt','r')
print(type(f))
data = f.read()
print(data)


data = data.replace('You', 'us')

f = open('data.txt','w')

f.write(data)

f.close()


