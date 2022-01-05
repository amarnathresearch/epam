def div(xval, yval):
    cval = 0
    try:
        cval = xval/yval
    except Exception as e:
        print("exception")
    
    return cval

a = 10
b = 0
c = div(a, b)
print(c)
# ZeroDivisionError: division by zero

try:
    f = open("test.txt", "w")
    f.write("exception handling")
except IOError:
    print("cannot find file for reading the data")
else:
    print("Content written in the file successfully")
    f.close()


try:
    f = open("test100.txt", "r")
    f.write("Data ")
except FileNotFoundError:
    print("File is not present")
else:
    f.close()

a = 10
b = 0
try:
    c = a/b
    f = open("test100.txt", "r")
    f.write(f"Data {c}")
except FileNotFoundError:
    print("File is not present")
except ZeroDivisionError:
    print("division error")
else:
    f.close()

# finally

a1, b1, c1 = 0
try:
    a1 = 10
    b1 = 20
    c1 = a/b

except FileNotFoundError:
    print("File is not present")
except ZeroDivisionError:
    print("division error")
else:
    f.close()
finally:
    print("==>finally block executed")
print(c1)

# User - Defined Exceptions
