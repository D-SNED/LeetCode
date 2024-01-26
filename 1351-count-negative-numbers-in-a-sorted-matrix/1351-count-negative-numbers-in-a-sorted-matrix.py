class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        num_neg = 0
        row_index = len(grid) - 1
        num_index = 0
        
        while row_index >= 0 and num_index < len(grid[0]):
            if grid[row_index][num_index] < 0:
                num_neg += len(grid[0]) - num_index
                row_index -= 1
            else:
                num_index += 1
                
        return num_neg
                
        
        
#         num_neg = 0
        
#         for arr in grid:
#             for el in arr:
#                 if el < 0:
#                     num_neg += 1
                    
#         return num_neg
    
#         index = 0
        
#         num_neg = 0
        
#         for i in range(len(grid)):
#             while index < len(grid[i]):
#                 if grid[i][index] < 0:
#                     num_neg += 1
#                 index += 1
        
#             index = 0
            
#         return num_neg

    