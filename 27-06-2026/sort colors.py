# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.


# 🤣 works but not right solution
def sortColorBuild(num: list) -> list:
    sort = sorted(num)  # this is (n)log(n)
    return sort


def sortColor(num: list) -> list:
    li = {}
    answer = []
    for key, v in enumerate(num):
        li[v] = li.get(v, 0) + 1
    for k in sorted(li):  # uses (n)log(n)
        answer += [k] * li[k]
    return answer


# Right answer want Dutch National Flag Algo
# but Answer I found uses the 0,1,2 until them no other option extra 3
def sortColors(nums):
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


num = [2, 0, 2, 1, 1, 0]
sortColors(num)
print(num)
