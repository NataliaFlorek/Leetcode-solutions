class Solution:
    def romanToInt(self, s: str) -> int:
        map={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000, 
        }
        result=0
        previous=0
        for i in range(len(s)-1, -1, -1):
            for keys,values in map.items():
                if s[i]==keys:
                    if values < previous:
                        result-=values
                    else:
                        result+=values
                    previous = values
        return result
            
