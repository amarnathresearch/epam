#Recursion

# dic = {'new':{'new':'epam'}}

# Fibonacci series

# 1 1 2 3 5 8 13 21 34 55 89..



# def fib(n):
#     # Base condition
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

def fib(n):
    # Base condition
    if n < 0:
        return 'invalid input'
    elif n <= 1:
        return 1
    return fib(n-2) + fib(n-1)


n = 5
ans = fib(n)
print(ans) 


# factorial using recursion
# n = 3

# 3*2*1

# n= 6
# 6*5*4*3*2*1

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

print(fact(3))

# Problem 3:
# Maze : Finding number of paths

# def maze(n, i, j):
#     if i == n-1 and j == n-1:
#         # count number path


# # Linked list

# # Classes and objects

# li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# class Node:
#     val = 0
#     nxt  => Node // Pointing to next node

# Create a linked list
# while loop



def npath(r,c):
    if(r==1 or c==1):
        return 1
    return npath(r-1,c) + npath(r,c-1)

r, c = 4, 4
print(npath(r,c))


