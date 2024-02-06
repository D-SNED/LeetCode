class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for index, num in enumerate(nums):
            new_targ = target - num
            
            if new_targ in dict:
                return [dict[new_targ], index]
            dict[num] = index
                
        
        