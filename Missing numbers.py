class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = n * (n + 1) // 2   # sum of numbers from 0 to n
        array_sum = sum(nums)
        return total - array_sum
