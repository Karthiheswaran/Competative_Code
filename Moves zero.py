class Solution(object):
    def moveZeroes(self, nums):
        zero_count =nums.count(0)
        nums[:]=[x for x in nums if x!=0]+[0]*zero_count
