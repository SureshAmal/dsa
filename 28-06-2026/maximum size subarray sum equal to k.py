# You are given an integer array nums and an integer k. Your task is to find the maximum length of a contiguous subarray whose elements sum to exactly k. If no such subarray exists, return 1.
# A subarray is a contiguous sequence of elements within an array. For example, in the array [1, 2, 3, 4], some subarrays include [1, 2], [2, 3, 4], and [3], but [1, 3] is not a subarray because the elements are not contiguous.

# The problem asks you to:
# Find all possible contiguous subarrays of nums
# Check which ones have a sum equal to k
# Return the length of the longest such subarray
# If no subarray sums to k, return 0

# For example:
# If nums = [1, -1, 5, -2, 3] and k = 3, the subarray [1, -1, 5, -2] sums to 3 and has length 4, which would be the answer.
# If nums = [2, 3, 4] and k = 10, no subarray sums to 10, so the answer would be 0.


# let try the bruth force approach with O(n2)
def maxSizeSubbrute(nums: list[int], k: int) -> int:
    n = len(nums)
    maxL = 1
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                maxL = max(maxL, j - i + 1)
    return maxL


def maxSizeSub(nums: list[int], k: int) -> int:
    index_sum = {0: -1}
    comulative_sum = 0
    target_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        comulative_sum += num
        target_sum = comulative_sum - k
        if target_sum in index_sum:
            sub_len = i - index_sum[target_sum]
            max_length = max(max_length, sub_len)
        else:
            index_sum[comulative_sum] = i
    return max_length


print(maxSizeSub([1, -1, 5, -2, 3], 5))
