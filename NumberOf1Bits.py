class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_b=bin(n)
        truncated_bin_b=bin_b[2:]
        counter=0
        print(truncated_bin_b)
        for b in truncated_bin_b:
            if(b=="1"):
                counter=counter+1

        return counter