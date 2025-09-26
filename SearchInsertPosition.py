class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        for i in nums:
            if i < target:
                pos=pos+1
            else:
                return pos
        return pos
            
        