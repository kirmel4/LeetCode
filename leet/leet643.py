class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        max_sum = -9999999
        curr_sum = 0
        counter = 0
        for i in range(len(nums)):
            counter += 1
            curr_sum += nums[i]            
            if counter == k:
                if curr_sum >= max_sum:
                    max_sum = curr_sum
            elif counter >= k:
                curr_sum = curr_sum - nums[i-k]
                if curr_sum >= max_sum:
                    max_sum = curr_sum
            else:
                continue
        return max_sum/k
s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))



        
            
