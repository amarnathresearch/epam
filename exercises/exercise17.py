# Command line arguments
import sys
# print(sys.argv)
for arg in sys.argv:
    print(type(arg))


class Calculator:
    def __init__(self):
        print("Hello, im the constructor")

cal = Calculator()

class Calculator:
    
    def __init__(self, x, y):
        print("Hello, im the constructor")
        self.c = x + y

a, b = 10, 20
cal = Calculator(a, b)

print(cal.c)
    


class User:
    def __init__(self):
        print("An object is created")
    def setuser(self, name, email, reg_id):
        self.name = name
        self.email = email
        self.reg_id = reg_id

    def getuser(self):
        return self.name, self.email, self.reg_id

user1 = User()
user1.setuser('amarnath', 'xx@gmail.com', '123')

user2 = User()
user2.setuser('sivaram', '12@gmail.com', '124')

user3 = User()
user3.setuser('ramgopal', '13@gmail.com', '125')

print('user1', user1.getuser())
print('user2', user2.getuser())
print('user3', user3.getuser())

input_list = [('amarnath', 'xx@gmail.com', '123'), ('sivaram', '12@gmail.com', '124'), ('ramgopal', '13@gmail.com', '125')]
# print(input_list)

list_user_objects = []
for inp in input_list:
    user = User()
    user.setuser(inp[0], inp[1], inp[2])
    list_user_objects.append(user)

print(list_user_objects)

for li in list_user_objects:
    print("user details =>", li.getuser())
    

class Customer:
    def __init__(self):
        print("An customer is created")
    def setuser(self, name, email, reg_id):
        self.name = name
        self.email = email
        self.reg_id = reg_id

    def getuser(self):
        return self.name, self.email, self.reg_id
list_user_objects = []
for inp in input_list:
    # cust = Customer()
    # cust.setuser(inp[0], inp[1], inp[2])
    # Customer().setuser(inp[0], inp[1], inp[2])
    # list_user_objects.append(cust)
    list_user_objects.append(Customer())
    


print(list_user_objects)
# for li in list_user_objects:
#     print("user details =>", li.getuser())