# Classes and objects

class Animals:
    def name(self, x):
        self.x = x

animal = Animals()
print(animal)

x = 'dog'
animal.name(x)
print(animal.x)


class A:
    c = 0
    def add(self, x, y):
        self.c = x + y


obj1 = A()
obj1.add(10, 20)
print(obj1.c)

obj2 = A()
obj2.add(30, 40)
print(obj2.c)

obj1 = None



class Calc:
    c = {}  
    def add(self, x, y):
        self.c['add'] = x + y

    def sub(self, x, y):
        self.c['sub'] = x - y

    def mul(self, x, y):
        self.c['mul'] = x * y

    def div(self, x, y):
        self.c['div'] = x/y


cal1 = Calc()
cal1.add(10, 20)
cal1.sub(10, 20)
cal1.mul(10, 20)
cal1.div(10, 20)

print(cal1.c['add'])


print(cal1.c['div'])
