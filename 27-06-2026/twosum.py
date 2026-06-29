# from given array find the sum of two number that match the target

def twosum(l:list,target:int)->int:
    h = {};

    for key,value in enumerate(l):
        n = target - value
        
        if n in h:
            return (h[n],key)

        h[value] = key

    return none





sol = twosum([1,3,5,2],8)
print(sol)
