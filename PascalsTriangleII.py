class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[]
        for i in range(0, rowIndex+1):
            if i==0:
                result.append([1])
            elif i==1:
                result.append([1,1])
            else:
                res=[]
                for j in range(0, i+1):
                    if j==0 or j==i:
                        res.append(1)
                        print(res)
                    else:
                        res.append(result[i-1][j]+result[i-1][j-1])
                result.append(res)

        return result[rowIndex]