class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        
        for i in range(len(grid) - 2):
            sub_arr = []
            for j in range(len(grid) - 2):
                if len(sub_arr) < len(grid) - 2:
                    sub_arr.append(max(grid[0 + i][0 + j], grid[0 + i][1 + j], grid[0 + i][2 + j], grid[1 + i][0 + j], grid[1 + i][1 + j], grid[1 + i][2 + j], grid[2 + i][0 + j], grid[2 + i][1 + j], grid[2 + i][2 + j]))
            result.append(sub_arr)
                
        return result
            
             