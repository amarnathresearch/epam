a = [10, 20]
print(a)


a = []
a.append(30)
a.append(40)
a.append(50)
print(a)

print(a[0])
print(a[1])
print(a[2])

a[1] = 60

a.append(80)

print(a)

a = [30, 40, 50]
b = [60, 70, 80]

c = a + b
print(c)

d = [30, 40, 50]
e = d

d[0] = 20

print(d)
print(e)

#Shallow copy

g = [30, 40, 50]
h = g.copy()
g[0] = 20

print(g)
print(h)






















