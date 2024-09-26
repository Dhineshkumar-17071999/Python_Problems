'''

Write a Python program to find all the pairs in a list whose sum is equal to a given value.
'''

def sum_pair(lst, given_value):
    result = []
    for i,x in enumerate(sorted(lst)):
        for y in (lst[i+1:]):
            if x+y == given_value:
                result.append([x,y])

    return result

lst1 = [1,2,3,4,5,6,7,8,9]
print(sum_pair(lst1, 10))