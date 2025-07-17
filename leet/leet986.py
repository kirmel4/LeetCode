class Solution:
    def intervalIntersection(self, firstList, secondList):
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] >= secondList[j][1]:
                j += 1
            elif secondList[j][0] >= firstList[i][1]:
                i+=1
            else:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                i+=1
                j+=1
        
        print(res)

s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
                
                