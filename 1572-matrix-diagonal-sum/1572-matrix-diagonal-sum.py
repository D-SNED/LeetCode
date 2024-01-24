class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        pdig_total = 0
        sdig_total = 0
        
        dig_index = 0
        
        
        for i in range(len(mat)):
            pdig_total += mat[i][dig_index]
            dig_index += 1
            
        dig_index = len(mat) - 1
        
        for i in range(len(mat)):
            sdig_total += mat[i][dig_index]
            dig_index -= 1
        
        if len(mat) % 2 == 1:
            return pdig_total + sdig_total - mat[len(mat) // 2][len(mat) // 2]
        else:
            return pdig_total + sdig_total
                
    
                    