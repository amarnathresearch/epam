# To sort a given series

# Use looping statements

# Donot use build-in functions

l=[4,8,2,1,6,9]
l = ['amar', 'epam', 'myanatomy', 'india']
l = [.5, -.2, .6]
length=len(l)
i=l[0]
j=l[0]
for i in range(length-2):           #iteration       #treat i as index using range
    for j in range(length-2-i):     #in each iteration
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

k=[1,5,7,2,4,5,15,45,8]
k = ['amar', 'epam', 'myanatomy', 'india']
k = [.5, -.2, .6]
for i in range(len(k)):
    for j in range(i):
        if(k[i]<k[j]):
            temp=k[i]
            k[i]=k[j]
            k[j]=temp
print(k)


x = [10,50,60,70,5]
x = ['amar', 'epam', 'myanatomy', 'india']
x = [.5, -.2, .6]
for i in range(len(x)):
    for j in range(len(x)):
        if(x[i]>=x[j]):
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)

# Ascending order
# Descending order
# Integer order / Floating point sort
# Is there any boundary conditions
# Positive numbers or negative numbers
# string sorting?

# l = ['amar', 'epam', 'myanatomy', 'india']
# Descending order

# Inbuild function available

x = [.5, -.2, .6]
print(sorted(x))

# Radix sort or bubble sort, insertion sort, merge sort, quick sort, heap sort, //20 sorting algorithms available

# Merge sort or quick sort = O(n*log(n))
# Radix sort = O(n*d) < O(n*log(n))

n = 10
i = 0
while i < 10:
    print(i)
    i += 1

