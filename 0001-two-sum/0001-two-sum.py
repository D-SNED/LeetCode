class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         index = 0
                   
        
#         while index < len(nums):
#             curr = nums[index] 
#             comp = target - curr
#             print(comp, curr)
#             for i in range(index + 1, len(nums)):
#                 if nums[i] == comp:
#                     return [index, i]
#             index += 1
#         return []
            
        d = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in d:
                return [d[diff], i]
            d[nums[i]] = i
                
        
        