class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        total = 0
        for i in range(0, len(nums)):
            total=nums[i]
            result.append(i)
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    result.append(j)
                    return result
            result.clear()
            total=0                    
                   

        
        