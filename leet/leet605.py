from typing import List
class Solution:
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
    #     if flowerbed[0] == 0 and flowerbed[1] == 0:
    #         n -= 1
    #     if flowerbed[-1] == 0 and flowerbed[-2] == 0:
    #         n -= 1
    #     if n > 0:
    #         for i in range(1, len(flowerbed) - 1):
    #             if flowerbed[i] == 0:
    #                 if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
    #                     flowerbed[i] = 1
    #                     n -= 1
    #             if n == 0:
    #                 return True
    #     else:
    #         return True
    #     return False
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_size = len(flowerbed)
        
        for i in range(flowerbed_size):
        
            prev = i == 0 or flowerbed[i-1] 
            fut = i == flowerbed_size-1 or flowerbed_size[i+1]

        return n <= 0
    
s = Solution()
print(s.canPlaceFlowers([0], 2))