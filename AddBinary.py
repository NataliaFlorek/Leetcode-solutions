class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int=int(a, base=2)
        b_int=int(b, base=2)
        result_int=a_int+b_int
        result=bin(result_int)
        return result[2:]