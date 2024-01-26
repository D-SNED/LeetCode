class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        # return array [index of row with most ones, number of ones]
        # if multiple subarrays have most 1's return lower indexed subarray
        
        # iterate over each row
            # append sum(row) to row_totals list
            
        num_ones = 0
        index = 0
            
        for iteration, row in enumerate(mat):
            count = row.count(1)
            
            if count > num_ones:
                num_ones = count
                index = iteration
                
        return [index, num_ones]
            
        
        
#         row_totals = []
       
        
#         for i in range(len(mat)):
#             row_totals.append(sum(mat[i]))
        
#         _max = max(row_totals)
            
#         for i in range(len(row_totals)):    
#             if len(row_totals) > 0 and row_totals[i] == _max:
#                 return [i, _max]
#         return [0, 0]
        
        
        
        