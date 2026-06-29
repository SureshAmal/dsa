# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingno(l:list)->int:
    s = set(l)
    for v in range(l[-1]+1):
        if v not in s:
            return v

    return -1

print(missingno([0,1,2,3,5,7,8]))
