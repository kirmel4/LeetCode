# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution:
    def intersection(self, nums1, nums2 ):
        
        d = {}
        res = []
        for num in nums1:
            if num not in d:
                d[num] = 1
        for num in nums2:
            if num in d:
                res.append(num)
                del d[num]
        return res
                                
s = Solution()
print(s.intersection( nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
        
        