class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        ref = [num + 1 for num in range(0, len(grid) ** 2)]
        
        missing_num = None
        double_num = None
        
        d = {}
        
        for row in grid:
            for num in row:
                if num not in d:
                    d[num] = 0
                d[num] += 1
                
        print(d)
                
        for key in d:
            if d[key] > 1:
                double_num = key
        
        for num in ref:
            if num not in d:
                missing_num = num
                
        return [double_num, missing_num]