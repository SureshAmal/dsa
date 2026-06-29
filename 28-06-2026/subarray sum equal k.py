# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

# Constraints:
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# [1,1,1] => [1],[1],[1] => [1,1],[1,1]
# contiguous subarray not random


def subArrayKBrut(nums: list[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == k:
                count += 1

    return count


def subArrayK(nums: list[int], k: int) -> int:
    index_sum = {0: 1}
    total = 0
    count = 0

    # prefix sum create a sum array
    for num in nums:
        total += num

        if total - k in index_sum:
            count += index_sum[total - k]

        index_sum[total] = index_sum.get(total, 0) + 1

    return count


print(subArrayK([1, 1, 1], 2))
