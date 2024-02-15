class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) -1
        
        while lo < hi:
            middle = (lo + hi) // 2
            
            if nums[middle] > nums[hi]:
                lo = middle + 1
            else:
                hi = middle
                
        return nums[lo]
        
    
                
                
            
            
        
        