class Solution:
    def averageWaitingTime(self, customers) -> float:
        
        time_starts = [customers[0][0] + customers[0][1]]
        sum_waits = 0 
        
        for i in range(1, len(customers)):
            time_starts.append(max(time_starts[i-1], customers[i][0])  + customers[i][1])
        for i in range(len(customers)):
            sum_waits += (time_starts[i]- customers[i][0])
            
        return sum_waits / len(customers)
        
            
            
            
        
        
s = Solution()
print(s.averageWaitingTime(customers =[[5,2],[5,4],[10,3],[20,1]]))
        