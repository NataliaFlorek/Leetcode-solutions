class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #boyer-moore majority vote algorithm
        counter=0
        for num in nums:
            if counter==0:
                m=num
                counter+=1
            elif m==num:
                counter+=1
            else:
                counter-=1
        return m
            
