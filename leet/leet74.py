class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        while len(matrix) != 1:
            idx_middle = len(matrix) // 2
            if target < matrix[idx_middle][0]:
                matrix = matrix[:idx_middle]
            else:
                matrix = matrix[idx_middle:]
        target_list = matrix[0]
        while len(target_list) != 1:
            idx_middle = len(target_list) // 2
            if target < target_list[idx_middle]:
                target_list = target_list[:idx_middle]
            else:
                target_list = target_list[idx_middle:]
        return target_list[0]
    
s = Solution()
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target= 6))
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]