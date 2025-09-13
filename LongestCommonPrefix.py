class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  
            return ""
        if strs[0] == "":  
            return ""
        for i in range(len(strs[0])):
            for pos in strs[1:]:
                if len(pos)<=i or pos[i]!=strs[0][i]:
                    return strs[0][:i]
            
        return strs[0]
        
            
                