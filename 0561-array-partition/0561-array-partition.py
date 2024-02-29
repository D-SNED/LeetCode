class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        l = sorted(nums)
        
        total = 0
        for i in range(0, len(l), 2):
            total += l[i]
            
        return total
            
            