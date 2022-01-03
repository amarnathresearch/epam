#Tuples

a = [10, 20, 30, 40]
print(len(a))

b = [50, 60, 70]

a.append(b)
print(len(a))
print(len(a[4]))

c = (10, 20, 30)
print(c)

#c.add(50)
#print(c)
#c[0] = 50
#print(c)

d = (60, 70, 80)

print(c+d)

e = list(c+d)
print(e)
f = tuple(e)
print(f)

print(len(f))

g = tuple([60])
print(g)

g = tuple(['amar', 20])
print(g)

ans=(30,)
print(type(ans))

ans = (30)
print(type(ans))

ans = ({'id':1, 'name':'amar'},)
print(ans)












