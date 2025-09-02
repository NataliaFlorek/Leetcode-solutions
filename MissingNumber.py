class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low = min(nums)
        high = len(nums)
        sum_nums = sum(nums)
        what_should_be=[x for x in range(low, high+1)]
        sum_what_should_be=sum(what_should_be)
        missing_num=sum_what_should_be-sum_nums
        print(nums)
        print(sum_nums)
        print(what_should_be)
        print(sum_what_should_be)
        return missing_num