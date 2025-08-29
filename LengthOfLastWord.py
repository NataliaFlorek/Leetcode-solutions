class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        char_count=0
        for char in reversed(s):
            if char!=" ":
                char_count+=1
            else:
                break
        
        return char_count
