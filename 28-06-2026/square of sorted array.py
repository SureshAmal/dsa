# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


def squareSortSimple(nums: list[int]) -> list[int]:
    # that way we directly sort with squre it
    for i, num in enumerate(nums):
        nums[i] = num * num

    nums.sort()  # n*long(n)
    return nums


def squareSort(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [0] * n
    left = 0
    right = n - 1
    pos = n - 1

    # O(n)
    # take extra space n(list) + 4(pointers)
    while left <= right:
        lefsqr = nums[left] * nums[left]
        rightsqr = nums[right] * nums[right]

        if lefsqr > rightsqr:
            answer[pos] = lefsqr
            left += 1
        else:
            answer[pos] = rightsqr
            right -= 1
        pos -= 1

    return answer


print(squareSort([-7, -3, 2, 3, 11]))
