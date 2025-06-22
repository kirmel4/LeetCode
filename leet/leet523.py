class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        
        p = 0
        d = {0: -1}
        s = 0
        while p != len(nums):
            s+=nums[p]
            if s % k not in d:
                d[s % k] = p
            elif p - d[s % k] >= 2:
                return True
            p+=1
                
        return False
        
s = Solution()
print(s.checkSubarraySum(nums = [23,2,4,6,6], k = 7))