# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorele(l:list)->int:
    h = {}
    for v in l:
        h[v] = h.get(v,0) + 1;
        if h[v] > len(l) // 2: # for integer division use //
            return v
    return False


print(majorele([2,2,1,1,1,2,2]))
