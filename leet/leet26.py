from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                nums[i] = None
                k += 1
        for i in range(len(nums)):
            if nums[i] == None:
                for j in range(i, len(nums)):
                    if nums[j] != None:
                        nums[i] = nums[j]
                        nums[j] = None
                        break
        return len(nums) - k
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))