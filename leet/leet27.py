from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
                k+=1
        for i in range(len(nums)):
            if nums[i] == None:
                for j in range(i, len(nums)):
                    if nums[j] != None:
                        nums[i] = nums[j]
                        nums[j] = None
                        break
        print(nums)
        return len(nums) - k
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))