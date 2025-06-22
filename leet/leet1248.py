class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        
        l = 0
        r = 0
        odd = 0
        count_arr = 0
        for r in range(len(nums)):
            odd += nums[r] % 2
            while odd > k :
                if nums[l]%2 !=0:
                    odd -=1
                l+=1
            count_arr += r - l + 1
        return count_arr

                
s =Solution()
print(s.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k =2) - s.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k =1))
                