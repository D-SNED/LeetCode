class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # create total
        
        # while length of first row is > 0
            # create max_value
            
            # for row in grid:
                # if max(row) > max_value:
                    # max_value = max(row)
            # total += max_value
            
            
        total = 0
        
        while len(grid[0]) > 0:
            max_value = 0
            
            for row in grid:
                if max(row) > max_value:
                    max_value = max(row)
                row.remove(max(row))
            total += max_value
            max_value = 0
            
        return total
                    
            
        
        