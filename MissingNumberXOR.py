class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = i^result
        helping_xor=0
        for i in range(0, len(nums)+1):
            helping_xor=helping_xor^i
        result=result^helping_xor
        return result