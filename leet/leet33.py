class Solution:
    def search(self, nums, target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1

        
# Input: nums = [4,5,6,7,0,1,2], target = 0
# [6,7,0,1,2,3,4, 5]
# Output: 4

s = Solution()
print(s.search(nums = [3,1], target = 1))