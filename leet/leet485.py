from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count +=1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 0
        
        return max(max_count, curr_count)
    
s = Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))