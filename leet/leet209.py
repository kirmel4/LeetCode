class Solution:
    def minSubArrayLen(self, target, nums):
        l = 0
        r = 0
        min_len = 1000001
        curr_sum = nums[0]
        while l != len(nums):
            if curr_sum >= target:
                min_len = min(r-l +1, min_len)
                curr_sum -= nums[l]
                l += 1
            else:
                if r != len(nums) -1:
                    r += 1
                    curr_sum += nums[r]
                else:
                    return min_len
        if min_len == 10001:
            return 0
        return min_len
s = Solution()
print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))

            
            
            
                
                        

                
            
        
        