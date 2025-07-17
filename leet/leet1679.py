class Solution:
    def maxOperations(self, nums, k) -> int:
        
        d = {}
        count = 0
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for num in nums:
            if d[num] > 0:
                if k - num in d:
                    if d[k -num] > 0:
                        d[num] -= 1
                        d[k -num] -= 1
                        if d[num] >=0:
                            count += 1
        print(count)
s = Solution()
print(s.maxOperations(nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k = 2))
                
            
        
        
        
        
s = Solution()
print(s.maxOperations())
        