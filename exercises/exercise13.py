# For loop

# for i in range(0, 10, 2):
#     print(i)

# for i in range(10, 0, -2):    
#     print(i)

# Code optimization

# for i in range(10):
#     for j in range(10):
#         print(i, j)

# Complexity of the program
# Time complexity 
# Space complexity

n = 10
for i in range(n):
    print(i)

# Time complexity O(n+2)
# 1+ n+1

# T(n) = 1+n+1
# T(n) = n+2
#      = O(n+2)
#      = O(n) + O(2)
#      = O(n) + c
#      = O(n) + e  // when n is large number c become negligible 
#      = O(n)
         
#     n = 10, 20.. O(c) is important
#  n = 1000000 O(c) becomes negligible.

n = 10
m = 10
for i in range(n):
    for j in range(m):
        print(i, j)

# T(n, m) = O(n*m) + O(n) + O(m) + O(c)
#         = O(n*m) + O(n) + O(m)
#          = O(n*m)


