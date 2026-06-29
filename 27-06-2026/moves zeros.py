# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def movezeros(l:list)->None:
    # if u do help(list) in python, u will find the method remove
    for key,v in enumerate(l):
        if key<=len(l) and v == 0:
            l.remove(v)
            l.append(v)



# my solution work but not great solution for complexity O(n2)

def movezeros1(l:list) -> None:
    index = 0
    # move all the elements to left
    for i in range(len(l)):
        if l[i] != 0:
            l[index] = l[i]
            print(index,l[i])
            index += 1

    # add zeros to the end
    while index < len(l):
        l[index]=0
        index +=1

l = [1,0,2,0,3,0,4]
movezeros1(l)
print(l)
