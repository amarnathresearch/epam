a = [10, 20, 30]

a.append(40)

print(a)

a.append(10)

print(a)

b = set(a)
print(b)

b.add(50)
print(b)
b.add(50)
print(b)


c = [10, 20, 30, 40, 40, 10, 50, 100, 20]
d = set(c)
print(d)
d = list(d)
print(d)

c = [10, 20, 30, 20.3, 4.2]
print(c)
c = [10, 20, 30, 20.3, 4.2, 'epam', 'india']
print(c)

c = [10, 20, 30]
d = [40, 50, 60]

c.append(d)

e = [70, 80, 90]
d.append(e)

f = {'epam', 'india', 110, 120}

e.append(f)

print(c)





















