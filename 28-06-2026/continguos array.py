# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Example 3:
# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


# First of all what is contiguous means
# one by one
# so we have to count the sequence of contiguous 0 and ones


def contiguousArrayLength(nums: list[int]) -> int:
    count = 0
    max_length = 0
    table = {}
    for index, num in enumerate(nums, 1):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count in table:
            max_length = max(max_length, index - table[count])
        else:
            table[count] = index

    return max_length


print(contiguousArrayLength([0, 1, 1, 1, 1, 1, 0, 0, 0]))
