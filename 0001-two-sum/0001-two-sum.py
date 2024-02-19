class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index = 0
        curr = nums[index]            
        
        while index < len(nums):

            comp = target - curr
            print(comp, curr)
            for i in range(index + 1, len(nums)):
                if nums[i] == comp:
                    return [index, i]
            index += 1
            curr = nums[index]
        return []
            
            
                
        
        