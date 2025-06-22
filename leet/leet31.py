class Solution:
    def nextPermutation(self, nums) -> None:
        
        def reverse_sublist(lst, start, end):
            while start < end:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1
        bp = -1
        p = len(nums) - 1
        while p >0 :
            if nums[p-1] < nums[p]:
                bp = p-1
                break
            else:
                p-=1
            
        if bp == -1:
            reverse_sublist(nums, 0, len(nums)-1)
            return nums
        else:
            p = len(nums) - 1
            while p >0 :
                if nums[p] > nums[bp]:
                    id = p
                    break
                else:
                    p-=1

            t = nums[bp]
            nums[bp] = nums[id]
            nums[id] = t
            reverse_sublist(nums, bp+1, len(nums)-1)
            
            return nums
s = Solution()
print(s.nextPermutation([3,2,1]))            
        
            
            
        