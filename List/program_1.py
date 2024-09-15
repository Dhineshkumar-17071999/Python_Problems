'''
1. Write a Python program to sum all the items in a list.
2. Write a Python program to multiply all the items in a list.
3. Write a Python program to get the largest number from a list.
4. Write a Python program to get the smallest number from a list.
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Write a Python program to sum all the items in a list.
print(sum(lst))
sum = 0
for i in lst:
    sum += i
print(sum)

# 2. Write a Python program to multiply all the items in a list
import math
print(math.prod(lst))
mul = 1
for i in lst:
    mul *= i
print(mul)

# 3. Write a Python program to get the largest number from a list.
print(min(lst))

# 4. Write a Python program to get the smallest number from a list.
print(max(lst))