class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        num_neg = 0
        
        for arr in grid:
            for el in arr:
                if el < 0:
                    num_neg += 1
                    
        return num_neg
#         index = 0
        
#         num_neg = 0
        
#         for i in range(len(grid)):
#             while index < len(grid[i]):
#                 if grid[i][index] < 0:
#                     num_neg += 1
#                 index += 1
        
#             index = 0
            
#         return num_neg

    